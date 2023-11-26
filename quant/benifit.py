# 从2020-01-23开始，如果每月的第一个交易日买入1手股票，每年最后一个交易日卖出所有股票，到今天为止，我的收益如何？

# 可以使用resample函数
# df_monthly = df.resample("M").first()
# df_yearly = df.resample("A").last()

import pandas as pd
import numpy as np
import mplfinance as mpf
import datetime
import calendar
from stock_action import buy_stock, sell_stock, account, sell_all_stock
import time

# init stock account 
stock_account = account("zhicong_wallet", 0, 100000)
print("我的钱包余额：", stock_account.wallet_balance)

# get stock data
df = pd.read_csv("/Users/zhangzhicong/Downloads/Inspur_data.csv", encoding="gbk", index_col="date", parse_dates=True)

print("我进入股市，从2020-01-23开始，每月的第一个交易日买入1手股票，每年最后一个交易日卖出所有股票")
init_date = df.index[0]
prev_date = init_date
for date in df.index:
    if date.month > prev_date.month:
        stock_amount_buy = 100
        buy_stock(stock_account, stock_amount_buy, df.loc[date].open)
        print(f"购买{stock_amount_buy}股后钱包余额：{stock_account.wallet_balance}")
        print(f"现在持有 {stock_account.stock_total_amounts} 股")
    if date.year > prev_date.year:
        # formate from pandas timestamp to python datetime, then it can use python datetime method
        today = date.to_pydatetime()
        # use python datetime method
        f_today = today.strftime("%Y-%m-%d")
        print(f"今天是{f_today},是新的一年的第一个交易日，现在的开盘价：{df.loc[date].open}")
        print(f"现在我持有 {stock_account.stock_total_amounts} 股")
        print("卖出所有的stock")
        sell_all_stock(stock_account, df.loc[date].open)
        print(f"钱包余额：{stock_account.wallet_balance}")
        print(f"现在持有 {stock_account.stock_total_amounts} 股")
    prev_date = date

print("最后我的钱包余额：", stock_account.wallet_balance)