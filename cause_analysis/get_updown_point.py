import ast
import requests
import json
from datetime import datetime , timedelta
import time
import pandas as pd
import numpy as np

headername = ['crypto','date','time','high','low','open','close','gap','from_time','to_time']

cryptoprice_set = pd.DataFrame(columns=headername)
total_cryptoprice_set = pd.DataFrame(columns=headername)

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#crypto = 'BCH'
#crypto = 'ETH'
crypto = 'BTC'

#datelist = ['2017-08-18','2018-02-08','2018-12-20','2019-04-02','2019-10-25','2020-01-14'] # BCH Up
#datelist = ['2017-08-04','2018-01-16','2018-11-27','2019-02-24','2019-07-14','2020-03-12'] # BCH down
#datelist = ['2017-03-16','2017-12-12','2018-04-12','2018-12-28','2019-04-02','2019-10-25','2020-03-13'] # ETH up
#datelist = ['2017-03-18','2017-12-22','2018-01-16','2018-09-05','2019-02-24','2019-09-24','2020-03-12'] # ETH down
#datelist = ['2017-01-04','2017-07-20','2018-04-12','2018-12-20','2019-04-02','2019-10-25','2020-03-13']  # BTC up
datelist = ['2017-01-11','2017-09-14','2018-01-16','2018-11-19','2019-06-27','2019-07-16','2020-03-12']  # BTC down

for date in datelist :

    datestr = date
    yyyy = int(datestr[0:4])
    mm = int(datestr[5:7])
    dd = int(datestr[8:10])

    print(yyyy)
    print(mm)
    print(dd)

    dt = datetime(yyyy, mm, dd, 23, 23)
    print("Unix Timestamp: ",(time.mktime(dt.timetuple())))
    targetTime = (time.mktime(dt.timetuple()))

    url = "https://min-api.cryptocompare.com/data/v2/histohour?fsym="+crypto+"&tsym=USD&limit=24&aggregate=1&toTs="+str(targetTime)

    response_Json = requests.get(url=url,headers=newHeaders)

    jsonFile = response_Json.json()

    jsonData = jsonFile['Data']['Data']

    datarow = []

    for entry in jsonData:
        ptime = entry.pop('time')

        ptime = datetime.fromtimestamp(
            int(ptime)
        ).strftime('%Y-%m-%d %H:%M:%S')

        phigh = entry.pop('high')
        plow = entry.pop('low')
        popen = entry.pop('open')
        pclose = entry.pop('close')

        datarow.append(crypto)
        datarow.append(datestr)

        datarow.append(ptime)
        datarow.append(phigh)
        datarow.append(plow)
        datarow.append(popen)
        datarow.append(pclose)
        datarow.append(((pclose - popen) / popen) * 100)
        datarow.append(ptime) # 임시로 ptime을 입력함
        datarow.append(ptime)

        cryptoprice_set = cryptoprice_set.append(pd.Series(datarow, index=headername), ignore_index=True)
        datarow = []


    # maxgap_set = cryptoprice_set[cryptoprice_set['gap']==cryptoprice_set['gap'].max()]
    maxgap_set = cryptoprice_set[cryptoprice_set['gap'] == cryptoprice_set['gap'].min()]
    maxgap_set['from_time'] = datetime.strptime(maxgap_set.iloc[0]['time'],'%Y-%m-%d %H:%M:%S') + timedelta(hours=-6)
    maxgap_set['to_time'] = datetime.strptime(maxgap_set.iloc[0]['time'],'%Y-%m-%d %H:%M:%S') + timedelta(hours=+6)

    total_cryptoprice_set = pd.concat([total_cryptoprice_set,maxgap_set], axis=0, ignore_index=False)

    maxgap_set.drop(headername,axis=1,inplace=True)
    cryptoprice_set.drop(headername,axis=1,inplace=True)

#total_cryptoprice_set['gubun'] = 'up'
total_cryptoprice_set['gubun'] = 'down'

total_cryptoprice_set.to_csv('./data/'+crypto+'_'+total_cryptoprice_set.iloc[0]['gubun']+'_'+'period.csv')
