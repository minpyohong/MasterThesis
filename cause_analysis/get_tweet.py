import ast
from datetime import datetime , timedelta
import time
import pandas as pd
import numpy as np
import GetOldTweets3 as got

header = ['crypto','gubun','datetime','username','retweets','favorites','hashtags','text']
# cryptoprice_set = pd.DataFrame(columns=headername)
# total_cryptoprice_set = pd.DataFrame(columns=headername)

tweetSet = pd.DataFrame(columns=header)
data = pd.read_csv('./BTC_up_period.csv', error_bad_lines=False)
query = 'bitcoin'

for i in data.index:
    gubun = data.loc[i, 'gubun']
    if gubun == 'up':
        # start_time = "2017-01-04"
        # end_time = "2017-01-05"
        start_time = datetime.strptime(data.loc[i, 'from_time'], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(data.loc[i, 'time'], "%Y-%m-%d %H:%M:%S")
        start_date = data.loc[i, 'from_time'][0:10]
        end_date = start_time + timedelta(days=1)
        end_date = str(end_date)[0:10]
    else:
        start_time = datetime.strptime(data.loc[i, 'time'], "%Y-%m-%d %H:%M:%S")
        end_time = start_time + datetime.timedelta(days=1)

    print(start_time, ' ', type(start_time))
    print(end_time, ' ', type(end_time))
    print(end_date, ' ', type(end_date))

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query) \
        .setSince(start_date) \
        .setUntil(end_date) \
        .setMaxTweets(-1)

    tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    num = 0

    for tweet_contents in tweet:

        if start_time <= tweet_contents.date and end_time >= tweet_contents.date:
            num = num + 1
            tweetSet.loc[num, 'gubun'] = 'up'
            tweetSet.loc[num, 'username'] = tweet_contents.username
            tweetSet.loc[num, 'datetime'] = tweet_contents.date
            tweetSet.loc[num, 'retweets'] = tweet_contents.retweets
            tweetSet.loc[num, 'favorites'] = tweet_contents.favorites
            tweetSet.loc[num, 'hashtags'] = tweet_contents.hashtags
            tweetSet.loc[num, 'text'] = tweet_contents.text


tweetSet.to_csv('./data/tweet_up_BTC1.csv')

