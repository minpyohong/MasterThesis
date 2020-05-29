import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from pandas.tseries import offsets

register_matplotlib_converters()

upperPrice = 15000.00 # 상한값 만원 단위

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')

#f = pd.read_csv('Ethereum1.csv',sep=',', thousands=',' , parse_dates=['date'],date_parser=dateparse)
f = pd.read_csv('Bitcoin_data.csv',sep=',', thousands=',' , parse_dates=['date'],date_parser=dateparse)
f1 = pd.read_csv('Ethereum_data.csv',sep=',', thousands=',' , parse_dates=['date'],date_parser=dateparse)
f2 = pd.read_csv('BitcoinCash_data.csv',sep=',', thousands=',' , parse_dates=['date'],date_parser=dateparse)

f['change'] = pd.to_numeric(f['change'].str.replace("%",""))
f1['change'] = pd.to_numeric(f1['change'].str.replace("%",""))
f2['change'] = pd.to_numeric(f2['change'].str.replace("%",""))

ts = f[['date','price','change']].sort_values(['date'])
ts1 = f1[['date','price','change']].sort_values(['date'])
ts2 = f2[['date','price','change']].sort_values(['date'])

#ts.apply(lambda x : np.log(upperPrice) if x['price'] > upperPrice else np.log(x['price']) , axis=1)
# ts['price'] = ts['price'].apply(lambda x : upperPrice if x > upperPrice else x)
# print(np.log(ts['price']))
ts['price'] = np.log(ts['price'])
ts1['price'] = np.log(ts1['price'])
ts2['price'] = np.log(ts2['price'])
#ts['date'] = pd.to_datetime(ts['date'])

#print(ts['date'].max())
#print(ts['date'].min())

startDate = ts['date'].min()
endDate = ts['date'].max()
#endDate = startDate +pd.DateOffset(months=2)
monthDate = startDate +pd.DateOffset(months=6)

#print(startDate)
#print(endDate)

while monthDate <= endDate :
    ts_btc = ts.loc[(ts['date'] >= startDate) & (ts['date'] <= monthDate), :]
    ts_eth = ts1.loc[(ts1['date'] >= startDate) & (ts1['date'] <= monthDate), :]
    ts_bch = ts2.loc[(ts2['date'] >= startDate) & (ts2['date'] <= monthDate), :]


    minus_point = ts_btc.loc[ts_btc['change'] < 0, 'change'].min()
    plus_point = ts_btc.loc[ts_btc['change'] >= 0, 'change'].max()


    bull_ts = ts_btc.loc[ts_btc['change'] == plus_point]   # 최고 상승 지점
    bear_ts = ts_btc.loc[ts_btc['change'] == minus_point]  # 최고 하강 지점

    plt.plot(ts_btc['date'].values, ts_btc['price'].values,'c--')
    plt.plot(ts_eth['date'].values, ts_eth['price'].values * 1.5, 'b--')
    plt.plot(ts_bch['date'].values, ts_bch['price'].values * 1.2, 'r--')
    #plt.plot(bull_ts['date'].values, bull_ts['price'].values ,'r^')
    #plt.plot(bear_ts['date'].values, bear_ts['price'].values ,'bv')
    plt.title(startDate.strftime('%Y-%m'))
    plt.xlabel('time')
    plt.ylabel('price')
    plt.legend(['bitcoin','ethereum','bitcoin cash'])
    plt.show()

    #print('Bull=========='+startDate.strftime('%Y-%m')+'===========')
    #print(bull_ts)₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     1
    #print('Bear=========='+startDate.strftime('%Y-%m')+'===========')
    #print(bear_ts)

    startDate = monthDate
    if monthDate == endDate :
        break
    monthDate = startDate +pd.DateOffset(months=6)
    monthDate = (lambda x : endDate if x > endDate else x)(monthDate)
    print(monthDate)

