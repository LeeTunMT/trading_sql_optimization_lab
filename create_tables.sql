CREATE TABLE dim_symbol (
    symbol VARCHAR(6) PRIMARY KEY,
    security_name TEXT,
    listing_exchange CHAR(1),
    market_category CHAR(1),
    is_etf BOOLEAN,
    round_lot_size INTEGER,
    is_test_issue BOOLEAN,
    financial_status CHAR(1),
    cqs_symbol VARCHAR(6),
    nasdaq_symbol VARCHAR(6),
    nextshares BOOLEAN
    );

CREATE TABLE ticket_daily_price (
    symbol VARCHAR(6) NOT NULL,
    date DATE NOT NULL,
    open DECIMAL(14,4),
    high DECIMAL(14,4),
    low DECIMAL(14,4),
    close DECIMAL(14,4),
    adj_close DECIMAL(14,4),
    volume BIGINT,
    
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES dim_symbol(symbol) ON DELETE CASCADE
);