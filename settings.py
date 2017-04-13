from datetime import date

QUANDL_KEY = "YOUR_KEY_HERE"
URL_DATA = 'https://www.quandl.com/api/v3/datasets/BCHARTS/BITSTAMPUSD/data.csv?order=asc'
PATH_DATA = 'data/BCHARTS-BITSTAMPUSD.csv'
NTESTS = 200
PREV_DAYS = 10
PERCENT_UP = 0.05
PERCENT_DOWN = 0.05


MARKET_NAME = 'bitstampUSD'

# DATE START
YEAR_START = 2017
MONTH_START = 4
DAY_START = 8
DATE_START = date(YEAR_START, MONTH_START, DAY_START)

# DATE END
DATE_END = date.today()

URL_DATA = 'http://bitcoincharts.com/charts/chart.json?'+'m='+MARKET_NAME+'&r=1&i=1-min&e'
URL_DATA = 'http://bitcoincharts.com/charts/chart.json?m='+MARKET_NAME
URL_DATA = 'http://bitcoincharts.com/charts/chart.json?m=bitstampUSD&r=1&i=1-min'
URL_DATA = 'http://bitcoincharts.com/charts/chart.json?m=bitstampUSD&r=1'
