## btctrading

Time Series Forecast with Bitcoin value, to detect upward/down trends with Machine Learning Algorithms.

It's presented how Classification Problem multiclass [UP, KEEP, DOWN]

## Install and run:

- pip install -r requirements.txt
- jupyter notebook

## Results:

XGBoost, period=30-min, PERCENT_UP=0.01, PERCENT_DOWN=0.01, without 'prev_columns':

- Accuracy: 0.951995560283
- Coefficient Kappa: 0.659794212904
- Confussion Matrix:
[[19545    72   109]
 [  390   489    67]
 [  359    41   551]]

LogisticRegression, period=Hourly, PERCENT_UP=0.015, PERCENT_DOWN=0.015, with 'prev_columns':

Accuracy: 0.934394168371
Coefficient Kappa: 0.317203847389
Confusion Matrix:

Predicted      0    1    2  __all__
Actual                             
0          10328   30   37    10395
1            335   94    4      433
2            330    2   89      421
__all__    10993  126  130    11249

## TODO:

- Simulator validation
- Tune parameters of xgboost.
- Add features -> Global Indicators (EUR/USD, S&P500, etc).
- Add different algorithms or ideas (LSTM, Reinforcement Learning, Q-Learning).
- Alert System (email).

----

by: Lecrin Technologies

http://lecrintech.com

We are glad receving any contribution, idea or feedback.
