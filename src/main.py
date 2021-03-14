from twitter_api import search_tweets

# Get 2 covid19 related tweets
print(search_tweets("covid19", {"count":2}))