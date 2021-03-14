from dotenv import load_dotenv
import json
import requests
import os

# Load API details from .env
load_dotenv()
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# This is a wrapper for the search api: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
def search_tweets(search_query, optional={}):
    if not search_query:
        return "Search query is required!"
    query_string = "q={}".format(search_query)

    DEFAULT_PARAMETERS = {"lang": "en", "result_type": "recent", "count": "1"}
    final_parameters = {**DEFAULT_PARAMETERS, **optional}

    # Add any other optional parameters (if supported by api)
    QUERY_OPTIONS = ["geocode", "lang", "locale", "count",
                "until", "since_id", "max_id", "include_entities", "result_type"]
    for parameter in final_parameters:
        if parameter not in QUERY_OPTIONS:
            return "Invalid parameters passed: {}".format(parameter)
        query_string += '&{}={}'.format(parameter, final_parameters[parameter])

    # Send request
    payload = {}
    headers = {'Authorization': 'Bearer {}'.format(TWITTER_BEARER_TOKEN)}
    search_url = "https://api.twitter.com/1.1/search/tweets.json?" + query_string
    response = requests.request(
        "GET", search_url, headers=headers, data=payload)
    # Use json.dumps to beautify the json output for debugging reasons
    return json.dumps(response.json(), sort_keys=True, indent=1)
