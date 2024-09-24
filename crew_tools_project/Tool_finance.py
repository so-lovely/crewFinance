
import yfinance as yf

"""def alphavantage_get_stock_data(symbol:str):
    load_dotenv()
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={os.environ.get('ALPHAVANTAGE_API_KEY')}'
    response = requests.get(url)
    data = response.json()
    # Convert data to a string summary
    summary = f"Daily prices for {symbol}: {data['Time Series (Daily)']}"
    return summary"""

#1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
def yf_get_stock_data(ticker:list[str], interval:str):
    data = yf.download(tickers=ticker,interval=interval)
    return data

