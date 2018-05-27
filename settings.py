from datetime import date

NTESTS = 1
PREV_DAYS = 10
PERCENT_UP = 0.01
PERCENT_DOWN = 0.01
PERIOD = 'Hourly' # [5-min, 15-min, 30-min, Hourly, 2-hour, 6-hour, 12-hour, Daily, Weekly]
MARKET = 'bitstampUSD'

# DATE START
YEAR_START = 2011
MONTH_START = 9
DAY_START = 13
DATE_START = date(YEAR_START, MONTH_START, DAY_START)

# DATE END
DATE_END = date.today()

URL_DATA_BASE = 'http://bitcoincharts.com/charts/chart.json?'
