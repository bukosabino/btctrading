## btctrading

Time Series Forecast with Bitcoin value, to detect upward/down trends with Machine Learning Algorithms.

It's presented how Classification Problem multiclass [UP, KEEP, DOWN]

## Install and run:

- git clone https://github.com/bukosabino/btctrading.git
- cd btctrading
- pip install -r requirements.txt
- jupyter notebook

## Results:

XGBoost, period=30-min, PERCENT_UP=0.01, PERCENT_DOWN=0.01, without 'prev_columns':

- Accuracy: 0.951995560283
- Coefficient Kappa: 0.659794212904
- Confussion Matrix:

| KEEP | UP | DOWN |
| --------- | --------- | ----------------- |
| 19545 | 72 | 109 |
| 390 | 489 | 67 |
| 359 | 41 | 551 |

LogisticRegression, period=Hourly, PERCENT_UP=0.015, PERCENT_DOWN=0.015, with 'prev_columns':

- Accuracy: 0.934394168371
- Coefficient Kappa: 0.317203847389
- Confusion Matrix:

| KEEP | UP | DOWN |
| --------- | --------- | ----------------- |
| 10328 | 30 | 37 |
| 335 | 94 | 4 |
| 330 | 2 | 89 |

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
