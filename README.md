## btctrading

Time Series Forecast with Bitcoin value, to detect upward/down trends with Machine Learning Algorithms.

It's presented how Classification Problem multiclass [UP, KEEP, DOWN]

## Install and run:

- git clone https://github.com/bukosabino/btctrading.git
- cd btctrading
- pip install -r requirements.txt
- jupyter notebook

## Results:

XGBoost, period=Houly, PERCENT_UP=0.015, PERCENT_DOWN=0.015, without 'prev_columns':

- Accuracy: 0.973330962752
- Coefficient Kappa: 0.802703881133
- Confussion Matrix:

| KEEP | UP | DOWN |
| --------- | --------- | ----------------- |
| 10299 | 41 | 41 |
| 99 | 316 | 2 |
| 113 | 4 | 334 |

XGBoost, period=Hourly, PERCENT_UP=0.015, PERCENT_DOWN=0.015, without 'prev_columns':

- Accuracy: 0.958333333333
- Coefficient Kappa: 0.790502793296
- Confussion Matrix:

 | KEEP | UP | DOWN |
 | --------- | --------- | ----------------- |
 | 209 | 1 | 2 |
 | 5 | 7 | 67 |
 | 2 | 0 | 14 |

## TODO:

- Simulator validation
- Tune parameters of xgboost.
- Add features -> Global Indicators (EUR/USD, S&P500, etc).
- Add different algorithms or ideas (LSTM, Reinforcement Learning, Q-Learning).
- Alert System (email).
- More Technical analysis: https://en.wikipedia.org/wiki/Technical_analysis

----

by: Lecrin Technologies

http://lecrintech.com

We are glad receving any contribution, idea or feedback.
