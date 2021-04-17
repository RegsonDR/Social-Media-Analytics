import pandas as pd
import tweepy  
# CSV Names
RAW_CSV_NAME = "raw_tweets_general_large.csv"

# Twitter API Credentials
CONSUMER_KEY = "hnGPJx6xBsudTgwOAxd0UNGUW"
CONSUMER_SECRET = "JcxhisQeF19hlEHRdeBifU3aL4R9DP9BWEMjYJ7MtnGcWaxn0p"
ACCESS_KEY = "1249286455530123264-5LbTPxHcE8Hl3CHhWztOsycMGEViHT"
ACCESS_SECRET = "4vdHhFP3odtZSUAKkK6GgPm7Vl03EHwvbP7cRTLFmQbFf"

# Connect to API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Query the API
search_term = "FarmersProtest"
max_items = 50000
result_type = "recent"
lang = "en"

# Do not include retweets, ensure tweet has 1 minimum retweet and is after September 2020        
response = tweepy.Cursor(api.search, q=search_term+"-filter:retweets min_retweets:1 since:2020-09-01",
                            result_type=result_type, lang=lang, tweet_mode="extended").items(max_items)

# Extract only the required keys from the response
tweets = [
    [tweet.created_at,
        tweet.full_text,
        tweet.retweet_count,
        tweet.favorite_count,
        tweet.user.screen_name,
        tweet.user.followers_count,
        tweet.user.verified,
        tweet.author.location
    ] for tweet in response]

# Store as CSV for later
tweets_df = pd.DataFrame(data=tweets, columns=["created_at", "text", "retweet_count", "favorite_count",
"user_screen_name", "user_followers_count", "user_verified","country"])
tweets_df.to_csv(RAW_CSV_NAME, quotechar='"', encoding='utf8', index = False, header=True)