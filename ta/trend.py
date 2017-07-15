# -*- coding: utf-8 -*-
import pandas as pd
from pandas.stats import moments
import numpy as np

def _wilder_sum(s, n):
    s = s.dropna()
    nf = (n - 1) / n
    ws = [np.nan]*(n - 1) + [s[n - 1] + nf*sum(s[:n - 1])]
    for v in s[n:]:
        ws.append(v + ws[-1]*nf)
    return Series(ws, index=s.index)

def _ema(s, n, wilder=False):
    """
    https://github.com/FreddieWitherden/ta/blob/master/ta.py
    """
    span = n if not wilder else 2*n - 1
    return moments.ewma(s, span=span)


def macd(df, n_fast=12, n_slow=26, n_sign=9):
    """
    MACD, MACD Signal and MACD difference
    https://github.com/femtotrader/pandas_talib/blob/master/pandas_talib/__init__.py
    """
    EMAfast = pd.Series(pd.ewma(df['Close'], span=n_fast, min_periods=n_slow - 1))
    EMAslow = pd.Series(pd.ewma(df['Close'], span=n_slow, min_periods=n_slow - 1))
    MACD = pd.Series(EMAfast - EMAslow, name='MACD_%d_%d' % (n_fast, n_slow))
    MACDsign = pd.Series(pd.ewma(MACD, span=n_sign, min_periods=n_sign - 1), name='MACD_sign_%d_%d' % (n_fast, n_slow))
    MACDdiff = pd.Series(MACD - MACDsign, name='MACD_diff_%d_%d' % (n_fast, n_slow))
    return pd.DataFrame([MACD, MACDsign, MACDdiff]).transpose()

def rsi(df, n=14):
    """
    Relative strength index (RSI)
    https://github.com/FreddieWitherden/ta/blob/master/ta.py
    """
    diff = df['Close'].diff()
    which_dn = diff < 0

    up, dn = diff, diff*0
    up[which_dn], dn[which_dn] = 0, -up[which_dn]

    emaup = pd.ewma(up, n)
    emadn = pd.ewma(dn, n)

    return 100 * emaup/(emaup + emadn)

def adx(df, n=14):
    """
    Average directional movement index
    https://github.com/FreddieWitherden/ta/blob/master/ta.py
    """
    cs = df['Close'].shift(1)
    tr = df['High'].combine(cs, max) - df['Low'].combine(cs, min)
    trs = pd.rolling_sum(tr, n)

    up = df['High'] - df['High'].shift(1)
    dn = df['Low'].shift(1) - df['Low']

    pos = ((up > dn) & (up > 0)) * up
    neg = ((dn > up) & (dn > 0)) * dn

    # dip = 100 * _wilder_sum(pos, n) / trs
    # din = 100 * _wilder_sum(neg, n) / trs

    dip = 100 * pd.rolling_sum(pos, n) / trs
    din = 100 * pd.rolling_sum(neg, n) / trs

    dx = 100 * np.abs((dip - din)/(dip + din))
    adx = pd.ewma(dx, n)

    # return DataFrame(dict(adx=adx, dip=dip, din=din))
    return pd.DataFrame([adx, dip, din]).transpose()



def vortex(df, n=14):
    """
    Vortex Indicator
    https://github.com/FreddieWitherden/ta/blob/master/ta.py
    """
    dfs = df.shift(1)

    tr = df['High'].combine(dfs['Close'], max) - df['Low'].combine(dfs['Close'], min)
    trn = moments.rolling_sum(tr, n)

    vmp = np.abs(df['High'] - dfs['Low'])
    vmm = np.abs(df['Low'] - dfs['High'])

    vip = moments.rolling_sum(vmp, n) / trn
    vin = moments.rolling_sum(vmm, n) / trn

    return pd.DataFrame([vin, vip]).transpose()
