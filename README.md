# Trading SQL Optimization Lab 
## Dataset: use stock market dataset on kaggle. This a historical daily prices of nasdaq-trades stoke and ETLs 
This datasets contain historical daily prices for all tickers currently trading on nasdaq 
[LINK](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset)

The date for every symbol is saved in CSV format with common fields:
    Date - specifies trading date
    Open - opening price
    High - maximum price during the day
    Low - minimum price during the day
    Close - close price adjusted for splits
    Adj Close - adjusted close price adjusted for both dividends and splits.
    Volume - the number of shares that changed hands during a given day

Info of meta data (in symbols_valid_meta.csv file): https://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs 
    Symbol: The one to four or five character identifier for each Nasdaq-listed security.
    Security Name: Company issuing the security.
    Listing Exchange: The listing stock exchange or market of a security. 
        Allowed values are:
        A = NYSE MKT
        N = New York Stock Exchange (NYSE)
        P = NYSE ARCA
        Z = BATS Global Markets (BATS)
        V = Investors' Exchange, LLC (IEXG)
        Q = NASDAQ

    Market Category: The category assigned to the issue by Nasdaq based on Listing Requirements. Values:
        Q = Nasdaq Global Select Market℠
        G = Nasdaq Global Market℠
        S = Nasdaq Capital Market
    ETF: Identifies whether the security is an exchange traded fund (ETF). Possible values: 
        Y = Yes, security is an ETF
        N = No, security is not an ETF (in this case, i defined it is stock)
    Round Lot Size: Indicates the number of shares that make up a round lot for the given security. Allow up to 6 digits.
    Test Issue: Indicates whether or not the security is a test security. Values: Y = yes, it is a test issue. N = no, it is not a test issue.
    Financial Status: Indicates when an issuer has failed to submit its regulatory filings on a timely basis, has failed to meet Nasdaq's continuing listing standards, and/or has filed for bankruptcy. Values include:
        D = Deficient: Issuer Failed to Meet Nasdaq Continued Listing Requirements
        E = Delinquent: Issuer Missed Regulatory Filing Deadline
        Q = Bankrupt: Issuer Has Filed for Bankruptcy
        N = Normal (Default): Issuer Is NOT Deficient, Delinquent, or Bankrupt.
        G = Deficient and Bankrupt
        H = Deficient and Delinquent
        J = Delinquent and Bankrupt
        K = Deficient, Delinquent, and Bankrupt
    CQS Symbol: Identifier of the security used to disseminate data via the SIAC Consolidated Quotation System (CQS) and Consolidated Tape System (CTS) data feeds. Typical identifiers have 1-5 character root symbol and then 1-3 characters for suffixes. Allow up to 14 characters. 
    NASDAQ Symbol: Identifier of the security used to in various Nasdaq connectivity protocols and Nasdaq market data feeds. Typical identifiers have 1-5 character root symbol and then 1-3 characters for suffixes. Allow up to 14 characters.
    NextShares: 


Summary: check data -> create schema (create database postgres docker -> create 2 dim-fact table )


