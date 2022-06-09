import pandas_datareader.data as web
import requests


def load_stock(ticker_str):
    """Load stock function.
    Given a string, ticker_str, load information
    for the indicated stock, such as 'MSFT,' into a
    Pandas
    data frame (df) and return it.
    """
    proxies = {"https": "http://127.0.0.1:58591"}
    headers = {
        "Accept": "application/json",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "none",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://cssspritegenerator.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
        + "AppleWebKit/537.11 (KHTML,like Gecko) "
        + "Chrome / 23.0.1271.64 "
        + "Safari / 537.11",
    }

    with requests.Session() as s:
        s.headers = headers
        s.proxies.update(proxies)

    df = web.DataReader(ticker_str, "yahoo", session=s)
    df = df.reset_index()
    return df


# Get a data frame (stock_df) and print it out.
if __name__ == "__main__":
    stock_df = load_stock("MSFT")  # 'msft' also Ok.
    print(stock_df)
    print(stock_df.columns)
