import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from openpyxl import Workbook
from pandas.tseries import offsets
# import xlsxwriter
register_matplotlib_converters()

upperPrice = 15000.00 # 상한값 만원 단위

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')

temp_heder = ['date','btc_change','bch_change']
btc_bch_diffset = pd.DataFrame(columns=temp_heder)


f = pd.read_csv('Bitcoin_data.csv',sep=',', thousands=',' , parse_dates=['date'],date_parser=dateparse)
f1 = pd.read_csv('Ethereum_data.csv',sep=',', thousands=',' , parse_dates=['date'],date_parser=dateparse)
f2 = pd.read_csv('BitcoinCash_data.csv',sep=',', thousands=',' , parse_dates=['date'],date_parser=dateparse)

f['change'] = pd.to_numeric(f['change'].str.replace("%",""))
f1['change'] = pd.to_numeric(f1['change'].str.replace("%",""))
f2['change'] = pd.to_numeric(f2['change'].str.replace("%",""))

ts = f[['date','price','change']].sort_values(['date'])
ts1 = f1[['date','price','change']].sort_values(['date'])
ts2 = f2[['date','price','change']].sort_values(['date'])


ts['price'] = np.log(ts['price'])
ts1['price'] = np.log(ts1['price'])
ts2['price'] = np.log(ts2['price'])


startDate = ts['date'].min()
endDate = ts['date'].max()
monthDate = startDate +pd.DateOffset(months=6)


while monthDate <= endDate :
    ts_btc = ts.loc[(ts['date'] >= startDate) & (ts['date'] <= monthDate), :]
    ts_eth = ts1.loc[(ts1['date'] >= startDate) & (ts1['date'] <= monthDate), :]
    ts_bch = ts2.loc[(ts2['date'] >= startDate) & (ts2['date'] <= monthDate), :]


    ts_be = pd.concat([ts_btc['date'],ts_btc['change'],ts_bch['change']],axis=1, keys=['date','btc_change','bch_change'])

    # print(ts_be)

    bch_plus = ts_be.loc[ (ts_be['btc_change'] < 0) & (ts_be['bch_change'] >=0)]
    btc_plus = ts_be.loc[ (ts_be['btc_change'] > 0) & (ts_be['bch_change'] <= 0)]
    # print("###################",monthDate,"###################")

    bch_plus = bch_plus.loc[ (bch_plus['bch_change'] - bch_plus['btc_change']) > 5 ]
    btc_plus = btc_plus.loc[ (btc_plus['btc_change'] - btc_plus['bch_change']) > 5 ]

    btc_bch_diffset = pd.concat([btc_bch_diffset, bch_plus], axis=0)
    btc_bch_diffset = pd.concat([btc_bch_diffset, btc_plus], axis=0)

    #btc_eth_diffset.append(eth_plus)
    #btc_eth_diffset.append(btc_plus)

    bch_plus_ts = ts_bch.loc[ts_bch['date'].isin(bch_plus['date'])]  # 최고 상승 지점
    btc_plus_ts = ts_btc.loc[ts_btc['date'].isin(btc_plus['date'])]  # 최고 하강 지점

    plt.plot(ts_btc['date'].values, ts_btc['price'].values,'c--')
    plt.plot(ts_bch['date'].values, ts_bch['price'].values * 1.2, 'r--')
    #plt.plot(ts_bch['date'].values, ts_bch['price'].values * 1.2, 'r--')
    plt.plot(btc_plus_ts['date'].values, btc_plus_ts['price'].values ,'g^')
    plt.plot(bch_plus_ts['date'].values, bch_plus_ts['price'].values * 1.2 ,'b^')

    plt.title(startDate.strftime('%Y-%m'))
    plt.xlabel('time')
    plt.ylabel('price')
    plt.legend(['Bitcoin','Bitcoin Cash','btc plus','bch plus',])

    plt.show()


    startDate = monthDate
    if monthDate == endDate :
        break
    monthDate = startDate +pd.DateOffset(months=6)
    monthDate = (lambda x : endDate if x > endDate else x)(monthDate)

btc_bch_diffset.sort_values(['date'])
# btc_eth_diffset['upcrypto'] = (lambda x : x if x > 0.00 else 0)(btc_eth_diffset['btc_change'])
btc_bch_diffset['upcrypto'] = ['BTC' if x > 0.00 else 'BCH' for x in btc_bch_diffset['btc_change']]
btc_bch_diffset['gap'] = abs(btc_bch_diffset['btc_change'] - btc_bch_diffset['bch_change'])

#print(" Result ")
#print(btc_eth_diffset)

writer =  pd.ExcelWriter('./excel/btc_bch_diffset.xlsx',engine='xlsxwriter')

btc_bch_diffset.to_excel(writer, sheet_name='Sheet_name_3')

writer.save()