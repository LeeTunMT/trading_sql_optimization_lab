\copy dim_symbol(
    symbol,
    security_name,
    listing_exchange,
    market_category,
    is_etf,
    round_lot_size,
    is_test_issue,
    financial_status,
    cqs_symbol,
    nasdaq_symbol,
    nextshares
)
FROM '/absolute/path/symbols_valid_meta.csv'
DELIMITER ','
CSV HEADER;