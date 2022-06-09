"""File stock_plot_v1.py ---------------------------
Does the minimum to plot the closing price
of two fixed stocks. Depends on file stock_load.py
"""
import matplotlib.pyplot as plt
import numpy as np
from stock_load import load_stock


def do_plot(stock_df, name_str):
    """Do Plot function.
    Use stock_df, a stock data frame read from the web.
    """
    makeplot(stock_df, "Close", "closing price")
    plt.title(name_str + " Stock Price")
    plt.show()


def makeplot(stock_df, field, my_str):
    column = getattr(stock_df, field)
    column = np.array(column, dtype="float")
    plt.plot(stock_df.Date, column, label=my_str)
    plt.legend()


def do_duo_plot(stock1_df, stock2_df, name1, name2):
    makeplot(stock1_df, "Close", name1)
    makeplot(stock2_df, "Close", name2)
    plt.title(name1 + " vs. " + name2)
    plt.show()


if __name__ == "__main__":
    # stock1_df = load_stock("MSFT")
    # stock2_df = load_stock("AAPL")
    # do_duo_plot(stock1_df, stock2_df, 'MSFT', 'AAPL')

    stock1_df = load_stock("IBM")
    stock2_df = load_stock("DIS")
    do_duo_plot(stock1_df, stock2_df, "IBM", "Disney")
