import tweepy
import csv
import pandas as pd
import snscrape.modules.twitter as sntwitter

consumer_key = 'hnGPJx6xBsudTgwOAxd0UNGUW'
consumer_secret = 'JcxhisQeF19hlEHRdeBifU3aL4R9DP9BWEMjYJ7MtnGcWaxn0p'
access_token = '1249286455530123264-5LbTPxHcE8Hl3CHhWztOsycMGEViHT'
access_token_secret = '4vdHhFP3odtZSUAKkK6GgPm7Vl03EHwvbP7cRTLFmQbFf'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

RAW_CSV_NAME = "raw_tweets_general_large.csv"
tweets_df = pd.DataFrame(columns=["id", "date", "content", "username"])
tweets_df.to_csv(RAW_CSV_NAME, quotechar='"', encoding='utf8', index = False, header=True)

maxTweets = 100000
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#FarmersProtest' + '-filter:retweets min_retweets:1 since:2020-09-01 until:2021-03-31').get_items()):
    if i > maxTweets:
        break
    print(i)
    tweets_df = tweets_df = pd.DataFrame(data=[[tweet.id, tweet.date, tweet.content, tweet.username]])
    tweets_df.to_csv(RAW_CSV_NAME, quotechar='"', mode='a', encoding='utf8', index=False, header=False)
