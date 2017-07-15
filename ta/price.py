# -*- coding: utf-8 -*-
import math
import pandas as pd
from sklearn.metrics import log_loss, cohen_kappa_score, accuracy_score, confusion_matrix, hinge_loss, classification_report
from pandas_ml import ConfusionMatrix
from datetime import datetime

import settings


def ACCDIST(df, n):
    """
    Accumulation/Distribution ROC
    """
    ad = (2 * df['Close'] - df['High'] - df['Low']) / (df['High'] - df['Low']) * df['Volume_BTC']
    M = ad.diff(n - 1)
    N = ad.shift(n - 1)
    ROC = M / N
    result = pd.Series(ROC, name='Acc/Dist_ROC_' + str(n))
    return result

def ACCDIST2(df, col_volume):
    """
    Accumulation/Distribution Index
    https://en.wikipedia.org/wiki/Accumulation/distribution_index
    """
    clv = ( (df['Close'] - df['Low']) - (df['High'] - df['Close']) ) / ( df['High'] - df['Low'] )
    clv.fillna(0.0, inplace=True) # float division by zero
    ad = clv * col_volume
    ad = ad + ad.shift(1)
    return pd.Series(ad)
