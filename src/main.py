from twitter_api import twitter_search

# Get 2 covid19 related tweets
print(twitter_search("covid19", {"count":2}))