import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

load_dotenv()

META_PATH = "dataset/symbols_valid_meta.csv"
DB_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@" \
         f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

engine = create_engine(DB_URL)

def setup_metadata():
    df = pd.read_csv(META_PATH)
    
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    
    bool_map = {"Y": True, "N": False}
    for col in ["etf", "test_issue", "nextshares"]:
        df[col] = df[col].map(bool_map)
        
    df = df.rename(columns={"etf": "is_etf", "test_issue": "is_test_issue"})
    
    df = df.drop_duplicates(subset=["symbol"])

    df = df.drop(columns=["nasdaq_traded"], errors="ignore")
    df["round_lot_size"] = df["round_lot_size"].fillna(0).astype(int)
    
    try:

        df.to_sql("dim_symbol", engine, if_exists="append", index=False)
        print("fetched data successfully!")
    except Exception as e:
        print(f"Big ERROR: {e}")

if __name__ == "__main__":
    setup_metadata()