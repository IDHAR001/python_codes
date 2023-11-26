# 使用pandas包计算股票历史数据的5日均线和60日均线

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpl
from calculate_cross import caculate_golden_cross_date, caculate_death_cross_date
from stock_action import buy_stock, sell_stock, account, sell_all_stock

df = pd.read_csv("/Users/zhangzhicong/Downloads/Inspur_data.csv", encoding="gbk", index_col="date", parse_dates=True)

# df['close'].rolling(5).mean() rolling方法简单粗暴

def caculate_ma(day):
    day_list = []
    ma_list = []
    for i in range(1, df.shape[0]+1):
        day_list.append(df.iloc[i-1].close)
        # print(f"day list: {day_list}")
        total = sum(day_list)
        ma_list.append(total/day)
        if len(day_list) > day - 1:
            day_list.pop(0)
    return ma_list
    # print(f"{day}日均线列表：{ma_list}")


ma5 = caculate_ma(5)
ma60 = caculate_ma(60)


df["ma5"] = ma5
df["ma60"] = ma60

# 使用matplotlib包可视化历史数据的收盘价和两条均线

plt.title("Inspur Candlestick Charts")
# plt.plot(df.index, ma5, "-", color="orange", label="5日均线")
# plt.plot(df.index, ma60, "-", color="red", label="60日均线")
# plt.plot(df.index, df.close, "-", color="green", label="收盘价")
df[['close','ma5','ma60']].plot()
# plt.show()

# 分析输出所有金叉和死叉的日期


golden_cross_date_list = []
death_cross_date_list = []
ma5_list = []
ma60_list= []
caculate_golden_cross_date(df, golden_cross_date_list, ma5_list, ma60_list)
caculate_death_cross_date(df, death_cross_date_list, ma5_list, ma60_list)
# print(f"金叉的日期为：{golden_cross_date_list}")
# print(f"死叉的日期为：{death_cross_date_list}")

# Have bug here
# plt.plot(golden_cross_date_list, ma5_list, "o", color="yellow", label="金叉")
# plt.plot(death_cross_date_list, ma5_list, "o", color="black", label="死叉")
# plt.show()

# 假如我从2020年1月23日开始，初始资金100000元，金叉尽量买入，死叉全部卖出，则到今天为止，我的炒股收益如何？

golden_cross_df = df.loc[golden_cross_date_list]
# print(f"golden: {golden_cross_df}")
death_cross_df = df.loc[death_cross_date_list]
# print(f"death: {death_cross_df}")

cross_df = pd.merge(golden_cross_df, death_cross_df, how="outer", left_index=True, right_index=True)
# print(cross_df)

# init stock account 
stock_account = account("zhicong_wallet", 0, 100000)
print("我的钱包余额：", stock_account.wallet_balance)

print("我进入股市，从2020年1月23日开始，初始资金100000元，金叉尽量买入，死叉全部卖出")
unit_amount = 100
for date in cross_df.index:
    if date in golden_cross_df.index:
        stock_amount_buy = stock_account.wallet_balance//(unit_amount*df.loc[date].open) * 100
        print(f"今天是{f_today}，金叉，现在的开盘价：{df.loc[date].open}")
        print("尽量买入")
        buy_stock(stock_account, stock_amount_buy, df.loc[date].open)
        print(f"购买{stock_amount_buy}股后钱包余额：{stock_account.wallet_balance}")
        print(f"现在持有 {stock_account.stock_total_amounts} 股")
    if date in death_cross_df.index:
        # formate from pandas timestamp to python datetime, then it can use python datetime method
        today = date.to_pydatetime()
        # use python datetime method
        f_today = today.strftime("%Y-%m-%d")
        print(f"今天是{f_today}，死叉，现在的开盘价：{df.loc[date].open}")
        print(f"现在我持有 {stock_account.stock_total_amounts} 股")
        print("卖出所有的stock")
        sell_all_stock(stock_account, df.loc[date].open)
        print(f"钱包余额：{stock_account.wallet_balance}")
        print(f"现在持有 {stock_account.stock_total_amounts} 股")

if stock_account.stock_total_amounts == 0:
    print("今天我的钱包余额：", stock_account.wallet_balance)
else:
    stock_price = stock_account.stock_total_amounts*df.loc[df.index[-1]].open
    print (f"今天我的钱包余额：{stock_account.wallet_balance}，持有{stock_account.stock_total_amounts}股，折算为今天的市场价{stock_price}，总和{stock_price + stock_account.wallet_balance}")