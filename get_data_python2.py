# -*- coding: utf-8 -*-

import urllib, json
from datetime import timedelta, datetime
import csv

import settings

# Get and write data
def get(path_file='data/datas.csv', period='Hourly', market='bitstampUSD'):

    print "Loading....."
    header = ["Timestamp", "Open", "High", "Low", "Close", "Volume_BTC",
                "Volume_Currency", "Weighted_Price"]

    with open(path_file, 'wb') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)

        period_to_call = False

        # 1 API CALL
        if period == 'Weekly' or period == 'Daily' or period == '12-hour':

            url = settings.URL_DATA_BASE + 'm='+ market + \
            '&i=' + period + '&c=1' + '&s=' + settings.DATE_START.isoformat()+ \
            '&e=' + settings.DATE_END.isoformat()

            # print url
            response = urllib.urlopen(url)
            data = json.loads(response.read())
            for d in data:
                writer.writerow(d)

        elif period == '6-hour' or period == '2-hour':
            period_to_call = 365 # 1 API CALL per year
        elif period == 'Hourly' or period == '30-min' or period == '15-min':
            period_to_call = 30 # 1 API CALL per month
        elif period == '5-min':
            period_to_call = 7 # 1 API CALL per week
        else:
            period_to_call = 1 # 1 API CALL per day

        if period_to_call:
            delta = settings.DATE_END - settings.DATE_START
            i = 0
            while i <= delta.days:
                try:
                    date_start = settings.DATE_START + timedelta(days=i)
                    date_end = settings.DATE_START + timedelta(days=i+period_to_call)
                    url = settings.URL_DATA_BASE + 'm='+ market + \
                    '&i=' + period + '&c=1' + '&s=' + date_start.isoformat() + \
                    '&e=' + date_end.isoformat()
                    # print url
                    response = urllib.urlopen(url)
                    data = json.loads(response.read())
                    for d in data:
                        writer.writerow(d)
                except:
                    print 'Url not available (date): ' + url
                i += period_to_call + 1
                print str(i) + ' of ' + str(delta.days+1) + ' days loaded...'

    print "Last Timestamp: " + \
        datetime.fromtimestamp(int(data[-1][0])).strftime('%Y-%m-%d %H:%M:%S')


# get('data/datas.csv', period='1-min', market='bitstampUSD')
