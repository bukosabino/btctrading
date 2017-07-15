# -*- coding: utf-8 -*-
import pandas as pd
from pandas.stats import moments

#todo: adaptar
def atr(df, n):
    """
    Average True Range
    """
    i = 0
    TR_l = [0]
    while i < len(df) - 1:  # df.index[-1]:
    # for i, idx in enumerate(df.index)
        # TR=max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l)
    result = pd.Series(pd.ewma(TR_s, span=n, min_periods=n), name='ATR_' + str(n))
    return out(SETTINGS, df, result)

# bollinger bands
