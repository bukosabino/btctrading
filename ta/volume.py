# -*- coding: utf-8 -*-
import pandas as pd
from pandas.stats import moments

# TODO: Close, High, Low, etc. parametriced..

def acc_dist_roc(df, col_volume='Volume_BTC', n=2):
    """
    Accumulation/Distribution ROC
    https://github.com/femtotrader/pandas_talib/blob/master/pandas_talib/__init__.py
    """
    ad = (2 * df['Close'] - df['High'] - df['Low']) / (df['High'] - df['Low']) * df[col_volume]
    ad.fillna(0.0, inplace=True) # float division by zero
    M = ad.diff(n - 1)
    N = ad.shift(n - 1)
    ROC = M / N
    ROC.fillna(0.0, inplace=True) # float division by zero
    result = pd.Series(ROC)
    return result

def acc_dist_index(df, col_volume='Volume_BTC'):
    """
    Accumulation/Distribution Index
    https://en.wikipedia.org/wiki/Accumulation/distribution_index
    """
    clv = ( (df['Close'] - df['Low']) - (df['High'] - df['Close']) ) / ( df['High'] - df['Low'] )
    clv.fillna(0.0, inplace=True) # float division by zero
    ad = clv * df[col_volume]
    ad = ad + ad.shift(1)
    return pd.Series(ad)

def chaikin_money_flow1(df, col_volume='Volume_BTC'):
    """
    Chaikin Oscillator
    https://github.com/femtotrader/pandas_talib/blob/master/pandas_talib/__init__.py
    """
    ad = (2 * df['Close'] - df['High'] - df['Low']) / (df['High'] - df['Low']) * df[col_volume]
    return pd.Series(pd.ewma(ad, span=3, min_periods=2) - pd.ewma(ad, span=10, min_periods=9))

def chaikin_money_flow2(df, col_volume='Volume_BTC', n=20):
    """
    Chaikin Money Flow
    https://efxto.com/indicador-chaikin-money-flow
    """
    clv = ( (df['Close'] - df['Low']) - (df['High'] - df['Close']) ) / ( df['High'] - df['Low'] )
    clv.fillna(0.0, inplace=True) # float division by zero
    mf = clv * df[col_volume]
    return pd.Series(pd.rolling_mean(mf, n))

def chaikin_money_flow3(df, col_volume='Volume_BTC', n=20):
    """
    Chaikin Money Flow
    https://github.com/FreddieWitherden/ta/blob/master/ta.py
    """
    clv = (2 * df['Close'] - df['High'] - df['Low']) / (df['High'] - df['Low'])
    clv.fillna(0.0, inplace=True) # float division by zero
    return pd.Series(moments.rolling_sum(clv*df[col_volume], n) / moments.rolling_sum(df[col_volume], n))

def money_flow_index(df, col_volume='Volume_BTC', n=14):
    """
    Money Flow Index
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:money_flow_index_mfi
    https://en.wikipedia.org/wiki/Money_flow_index
    """
    # 1 typical price
    tp = ( df['High'] + df['Low'] + df['Close'] ) / 3.0
    # 2 money flow
    mf = tp * df[col_volume]
    # 3 positive and negative money flow with n periods
    df['1_Period_Positive_Money_Flow'] = 0.0
    df.loc[df['Up_or_Down'] == 1, '1_Period_Positive_Money_Flow'] = mf
    df['1_Period_Negative_Money_Flow'] = 0.0
    df.loc[df['Up_or_Down'] == 2, '1_Period_Negative_Money_Flow'] = mf
    n_positive_mf = pd.rolling_sum(df['1_Period_Positive_Money_Flow'], n)
    n_negative_mf = pd.rolling_sum(df['1_Period_Negative_Money_Flow'], n)
    # 4 money flow index
    mr = n_positive_mf / n_negative_mf
    # delete intermediate columns
    df.drop('1_Period_Positive_Money_Flow', axis=1, inplace=True)
    df.drop('1_Period_Negative_Money_Flow', axis=1, inplace=True)

    return ( 100 - ( 100 / (1 + mr) ) )

def on_balance_volume(df, col_volume='Volume_BTC'):
    """
    On-balance volume
    https://en.wikipedia.org/wiki/On-balance_volume
    """
    df['OBV'] = 0
    df.loc[df.Close < df.Close.shift(1), 'OBV'] = 0 - df['Volume_BTC']
    df.loc[df.Close > df.Close.shift(1), 'OBV'] = df['Volume_BTC']
    return df['OBV']

def on_balance_volume_mean(df, col_volume='Volume_BTC', n=10):
    """
    On-balance volume mean
    https://github.com/femtotrader/pandas_talib/blob/master/pandas_talib/__init__.py
    """
    df['OBV'] = 0
    df.loc[df.Close < df.Close.shift(1), 'OBV'] = 0 - df['Volume_BTC']
    df.loc[df.Close > df.Close.shift(1), 'OBV'] = df['Volume_BTC']
    return pd.Series(pd.rolling_mean(df['OBV'], n))

def force(df, col_volume='Volume_BTC', n=2):
    """
    Force Index
    https://github.com/femtotrader/pandas_talib/blob/master/pandas_talib/__init__.py
    """
    return pd.Series(df['Close'].diff(n) * df[col_volume].diff(n))
