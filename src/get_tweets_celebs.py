
import pandas as pd
import tweepy
# CSV Names
RAW_CSV_NAME = "raw_tweets_celebs.csv"
RAW_CSV_REPLIES_NAME = "raw_tweets_celebs_replies.csv"

# Twitter API Credentials
CONSUMER_KEY = "hnGPJx6xBsudTgwOAxd0UNGUW"
CONSUMER_SECRET = "JcxhisQeF19hlEHRdeBifU3aL4R9DP9BWEMjYJ7MtnGcWaxn0p"
ACCESS_KEY = "1249286455530123264-5LbTPxHcE8Hl3CHhWztOsycMGEViHT"
ACCESS_SECRET = "4vdHhFP3odtZSUAKkK6GgPm7Vl03EHwvbP7cRTLFmQbFf"

# Connect to API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

USE_OLD_CSV = True

# Obtain the celeb tweets
if not USE_OLD_CSV:
    # Query the API
    search_term = "FarmersProtest"
    max_items = 100
    result_type = "popular"
    lang = "en"

    response = tweepy.Cursor(api.search, q=search_term+"-filter:retweets min_retweets:1000 since:2020-09-01 filter:verified",
                             result_type=result_type, lang=lang, tweet_mode="extended").items(max_items)

    # Extract only the required keys from the response
    tweets = [
        [tweet.id,
            tweet.created_at,
            tweet.full_text,
            tweet.retweet_count,
            tweet.favorite_count,
            tweet.user.screen_name,
            tweet.user.followers_count,
            tweet.user.verified,
            tweet.author.location
         ] for tweet in response]

    # Store as CSV for later
    tweets_df = pd.DataFrame(data=tweets, columns=["id", "created_at", "text", "retweet_count", "favorite_count",
                                                   "user_screen_name", "user_followers_count", "user_verified", "country"])
    tweets_df.to_csv(RAW_CSV_NAME, quotechar='"',
                     encoding='utf8', index=False, header=True)

tweets_df = pd.DataFrame(columns=["related_id", "id", "created_at", "text", "retweet_count", "favorite_count",
                                                "user_screen_name", "user_followers_count", "user_verified", "country"])                                                
tweets_df.to_csv(RAW_CSV_REPLIES_NAME, quotechar='"', encoding='utf8', index=False, header=True)

# Get the replies for these tweets
count = 1
raw_tweets = pd.read_csv(RAW_CSV_NAME, quotechar='"', encoding='utf8')
for tweet_id, name in zip(raw_tweets["id"], raw_tweets['user_screen_name']):
    print(count)
    count+=1
    for tweet in tweepy.Cursor(api.search, q='to:'+name, tweet_mode="extended", result_type='recent', timeout=999999).items(500):
        if hasattr(tweet, 'in_reply_to_status_id_str') and (tweet.in_reply_to_status_id_str == str(tweet_id)):
            tweets_df = pd.DataFrame(data=[[
                tweet_id,
                tweet.id,
                tweet.created_at,
                tweet.full_text,
                tweet.retweet_count,
                tweet.favorite_count,
                tweet.user.screen_name,
                tweet.user.followers_count,
                tweet.user.verified,
                tweet.author.location
            ]])
            tweets_df.to_csv(RAW_CSV_REPLIES_NAME, quotechar='"', mode='a', encoding='utf8', index=False, header=False)
