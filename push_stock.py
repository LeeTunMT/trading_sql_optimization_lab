import os
import pandas as pd
import csv
from io import StringIO
from sqlalchemy import create_engine
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

STOCKS_PATH = "dataset/stocks/"
ETFS_PATH = "dataset/etfs/"
DB_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@" \
         f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

engine = create_engine(DB_URL)

def psql_insert_copy(table, conn, keys, data_iter):
    """
    call back function optimized for to_sql using COPY syntax of PostgreSQL
    the speed faster many times than INSERT
    """
    # Take actual connection from SQLAlchemy
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join('"{}"'.format(k) for k in keys)
        table_name = f'"{table.name}"'
        if table.schema:
            table_name = f'"{table.schema}".{table_name}'

        sql = f'COPY {table_name} ({columns}) FROM STDIN WITH CSV'
        cur.copy_expert(sql=sql, file=s_buf)

def process_file(filepath):
    symbol = os.path.basename(filepath).replace(".csv", "")
    try:

        df = pd.read_csv(filepath)
        if df.empty: return None
        
        # normalized column's name
        df.columns = df.columns.str.lower().str.replace(" ", "_")
        df["symbol"] = symbol
        

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        
        float_cols = ["open", "high", "low", "close", "adj_close"]
        for col in float_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df["volume"] = pd.to_numeric(df["volume"], errors="coerce").fillna(0).astype('int64')
        
        # Clean data 
        df = df.dropna(subset=["date"])
        df = df.drop_duplicates(subset=["symbol", "date"])
        df = df[df["volume"] >= 0]
        
        # just take the columns match with DB schema
        valid_cols = ["symbol", "date", "open", "high", "low", "close", "adj_close", "volume"]
        return df[[c for c in valid_cols if c in df.columns]]
        
    except Exception as e:
        print(f"BIG ERROR {filepath}: {e}")
        return None

def upload_data():
    folders = [STOCKS_PATH, ETFS_PATH]
    
    for folder in folders:
        print(f"\n--- On going: {folder} ---")
        files = [f for f in os.listdir(folder) if f.endswith(".csv")]
        
        for file in tqdm(files):
            path = os.path.join(folder, file)
            df = process_file(path)
            
            if df is not None and not df.empty:
                try:
                    # method=psql_insert_copy is the key to speed up
                    df.to_sql(
                        "ticket_daily_price",
                        engine,
                        if_exists="append",
                        index=False,
                        method=psql_insert_copy
                    )
                except Exception as e:
                    continue 

if __name__ == "__main__":
    upload_data()
    print("\n--- DONE ---")