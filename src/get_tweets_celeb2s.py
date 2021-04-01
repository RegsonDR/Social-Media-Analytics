
import pandas as pd
import tweepy
import snscrape.modules.twitter as sntwitter

# CSV Names
RAW_CSV_NAME = "raw_tweets_50_celeb.csv"
RAW_CSV_REPLIES_NAME = "raw_tweets_50_celeb_replies.csv"

# Twitter API Credentials
CONSUMER_KEY = "hnGPJx6xBsudTgwOAxd0UNGUW"
CONSUMER_SECRET = "JcxhisQeF19hlEHRdeBifU3aL4R9DP9BWEMjYJ7MtnGcWaxn0p"
ACCESS_KEY = "1249286455530123264-5LbTPxHcE8Hl3CHhWztOsycMGEViHT"
ACCESS_SECRET = "4vdHhFP3odtZSUAKkK6GgPm7Vl03EHwvbP7cRTLFmQbFf"

# Connect to API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets_df = pd.DataFrame(columns=["related_id", "id", "created_at", "text", "retweet_count", "favorite_count",
                                                "user_screen_name", "user_followers_count", "user_verified", "country"])                                                
tweets_df.to_csv(RAW_CSV_REPLIES_NAME, quotechar='"', encoding='utf8', index=False, header=True)

count = 1
raw_tweets = pd.read_csv(RAW_CSV_NAME, quotechar='"', encoding='utf8')
for tweet_id, name in zip(raw_tweets["id"], raw_tweets['username']):
    count+=1
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('to:'+name + ' filter:replies since:2020-09-01 until:2021-03-21').get_items()):
        if hasattr(tweet.quotedTweet, "id"):
            print("%s ) %s" % (count , i))
            if str(tweet_id)  == str(tweet.quotedTweet.id):
                tweets_df = pd.DataFrame(data=[[
                    tweet_id,
                    tweet.id,
                    tweet.date,
                    tweet.content,
                    tweet.retweetCount,
                    tweet.likeCount,
                    tweet.username,
                    tweet.user.followersCount,
                    tweet.user.verified,
                    tweet.user.location
                ]])
                tweets_df.to_csv(RAW_CSV_REPLIES_NAME, quotechar='"', mode='a', encoding='utf8', index=False, header=False)
                print("Added")