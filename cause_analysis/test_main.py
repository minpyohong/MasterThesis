#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

from cause_analysis import ConcurrentTweetManager

if sys.version_info[0] < 3:
    raise Exception("Python 2.x is not supported. Please upgrade to 3.x")

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))



import GetOldTweets3 as got



def test_Username():
    tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama')\
                                               .setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    assert tweet.username == 'BarackObama'

def test_QuerySearch():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#europe #refugees')\
                                               .setSince("2015-05-01")\
                                               .setUntil("2015-09-30")\
                                               .setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    assert tweet.hashtags.lower() == '#europe #refugees'

def test_MassFetchConcurrent():
    time1 = time.time()
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#europe #refugees')\
                                               .setSince("2015-05-01")\
                                               .setUntil("2015-09-30")\
                                               .setMaxTweets(200)
    tweets1 = ConcurrentTweetManager.getTweets(tweetCriteria, worker_count=5)
    print("Time Needed Concurrent: {} Secs".format((time.time() - time1)))

    time2 = time.time()
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#europe #refugees')\
                                               .setSince("2015-05-01")\
                                               .setUntil("2015-09-30")\
                                               .setMaxTweets(200)
    tweets2 = got.manager.TweetManager.getTweets(tweetCriteria)
    print("Time Needed Non Concurrent: {} Secs".format((time.time() - time2)))

    assert len(tweets1) == len(tweets2)

test_MassFetchConcurrent()