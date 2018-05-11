## btctrading

This is my personal code to predict the Bitcoin value using Machine Learning / Deep Learning Algorithms.

We will consider our problem as:

* 1. Regression Problem.
* 2. Classification Multiclass Problem [UP, KEEP, DOWN].

Get data from https://bitcoincharts.com/charts, you can choose period, symbol and exchange market and save the datas in a csv file.


## Install and run:

```sh
> git clone https://github.com/bukosabino/btctrading.git
> cd btctrading
> virtualenv -p python3 virtualenvironment
> source virtualenvironment/bin/activate
> pip install -r requirements.txt
> jupyter lab
```


## TODO:

* Simulator validation (backtesting)
* Add features -> Global Indicators (EUR/USD, S&P500, etc).
* Add different algorithms or ideas (LSTM, Reinforcement Learning, Q-Learning).
* Alert System (email, twitter, telegram).

----

Developed by Bukosabino at Lecrin Technologies - http://lecrintech.com

Please, let us know about any comment or feedback.
