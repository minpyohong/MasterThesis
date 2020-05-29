import tweepy

consumer_key = 'zQffJRJiwnVspRyxJLDi2VivZ'
consumer_secret = '1AiYEIzGsj71QakoMcgnzqYB3N3e8BRPvT17HilpzXo7ndizZW'

# 트위터 Access Token
# 트위터 Access Token Secret

access_token = '1182273686272765953-3MWwYyHcngyC4pSz8WHhvkpu8bzx1W'
access_token_secret = 'F2o42kSDp8dOGFPeJInE7h9xMvCu2KHxUPsAewKM7m7Uu'
# 1차 인증: 개인 앱 정보
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


# 2차 인증: 토큰 정보
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성
api = tweepy.API(auth)

keyword = "BitCoin";     # 검색할 키워드

"""
tweets = api.search(keyword, count = 50) # 한 번에 15 트윗 검색 정보를 가져옴
# tweets = api.search(keyword, count=100) # 일반 계정으로는 최대 100개 최신 게시물을 가져올 수 있음
for num, tweet in enumerate(tweets):
    print(num, "]", tweet.text)
    print (tweet.favorite_count)
    print (tweet.retweet_count)
"""

results = []
for tweet in tweepy.Cursor(api.search, q=keyword, since='2018-12-20', until ='2019-12-22'  ,count=100).items():
    print(tweet.created_at)
    results.append(tweet)

print(len(results))