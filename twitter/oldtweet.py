import GetOldTweets3 as got
import datetime
import time

days_range = []

start = datetime.datetime.strptime("2017-03-15", "%Y-%m-%d")
end = datetime.datetime.strptime("2017-05-19", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))

print("=== 설정된 트윗 수집 기간은 {} 에서 {} 까지 입니다 ===".format(days_range[0], days_range[-1]))
print("=== 총 {}일 간의 데이터 수집 ===".format(len(days_range)))

# 수집 기간 맞추기
start_date = days_range[0]
end_date = (datetime.datetime.strptime(days_range[-1], "%Y-%m-%d")
            + datetime.timedelta(days=1)).strftime("%Y-%m-%d") # setUntil이 끝을 포함하지 않으므로, day + 1

#                                            #.setUsername("VitalikButerin")\coinbase
#                                            #.setUsername("Cointelegraph")\coinbase
#                                            #.setUsername("blockchain")\coinbase
#                                            #.setUsername("rogerkver")\coinbase
#                                            #.setUsername("CCNMarkets")\coinbase
#                                            #.setUsername("CCNMarkets")\coinbase


# 조셉루빈 ethereumJoseph
# 우지한 JihanWu
# 크레이크라이트 ProfFaustus
# 저스틴선 justinsuntron 1  2 million followers
# John McAfee 2 1 million
# 3 비탈릭 부테린
# 4 Charie Lee LTC Founder
# 도널드트럼프 realDonaldTrump
# Andreas M Antonopoulos
# Changpeng Zhao
# 엘론 머스크
# Joseph Poon
# Ian Grigg
# David Chaum

"""

https://news.bitcoin.com/35-most-influential-bitcoin-crypto-twitter/ 

2020.mar

1. Justic Sun - 2M
2. John McAfee - 1M
3. Vitalic Buterin - 892.7K
4. Charlie Lee. LTC's 831.3K
5. Naval - 776.3K
6, Marc Andreessen - 735.9K
7. Fred Wilson - 662.7K


"""

# 트윗 수집 기준 정의
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('bitcoin')\
                                           .setSince(start_date)\
                                           .setUntil(end_date)\
                                           .setUsername("officialmcafee")\
                                           .setMaxTweets(-1)

# 수집 with GetOldTweet3
print("Collecting data start.. from {} to {}".format(days_range[0], days_range[-1]))
start_time = time.time()

tweet = got.manager.TweetManager.getTweets(tweetCriteria)

print("Collecting data end.. {0:0.2f} Minutes".format((time.time() - start_time)/60))
print("=== Total num of tweets is {} ===".format(len(tweet)))
i=0
for tweet_contents in tweet :
    i = i+1
    #print(i)
    print(tweet_contents.text)