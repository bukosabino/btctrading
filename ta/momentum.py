# -*- coding: utf-8 -*-
import pandas as pd
from pandas.stats import moments

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
