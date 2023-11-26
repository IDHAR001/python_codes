import pandas as pd

def caculate_golden_cross_date(df, golden_cross_date_list, ma5_list, ma60_list):
    prev_date = df.index[0]
    for date in df.index:
        if df.loc[date].ma60 <= df.loc[date].ma5 and df.loc[prev_date].ma5 < df.loc[prev_date].ma60:
            golden_cross_date = date.to_pydatetime()
            golden_cross_date_list.append(golden_cross_date.strftime("%Y-%m-%d"))
            # ma5_list.append(df.loc[date].ma5)
            # ma60_list.append(df.loc[date].ma60)
        prev_date = date
    return golden_cross_date_list, ma5_list, ma60_list

def caculate_death_cross_date(df, death_cross_date_list, ma5_list, ma60_list):
    prev_date = df.index[0]
    for date in df.index:
        if df.loc[date].ma60 >= df.loc[date].ma5 and df.loc[prev_date].ma5 > df.loc[prev_date].ma60:
            death_cross_date = date.to_pydatetime()
            death_cross_date_list.append(death_cross_date.strftime("%Y-%m-%d"))
            # ma5_list.append(df.loc[date].ma5)
            # ma60_list.append(df.loc[date].ma60)
        prev_date = date
    return death_cross_date_list, ma5_list, ma60_list