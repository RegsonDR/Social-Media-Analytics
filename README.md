# Social-Media-Analytics-COMP61332
 

## Repository Contents
* `main.ipynb` contains all the code, from obtaining twitter tweets to the sentimental analysis. This jupyter file contains comments and notes to explain each block and what is being done.
* `raw_tweets_general_large.csv` - These tweets are stored in a csv from the `main.ipynb`, this is used instead of trying to obtain the tweets fresh from the API. In order to avoid API limits.
* `preprocessed_tweets.csv` - Preprocessed version of the tweets from `raw_tweets_general_large.csv`.
* `raw_tweets_celeb.csv` - Tweets done by celebrities.
* `raw_tweets_celeb_replies.csv` - Replies to the celebrity's tweets. 
* `preprocessed_tweets_celeb.csv` -  Proprocessed version of `raw_tweets_celeb.csv` & `preprocessed_tweets_celeb.csv`.
* `get_tweets_large.py` & `get_tweets_celebs.py` - Daemon scripts to obtain tweets info and store into the following CSVs: `raw_tweets_general_large.csv`, `raw_tweets_celeb.csv` & `raw_tweets_celeb_replies.csv`.
* `bokeh_plot.png` - Clustering of the 12 LDA Topics.
* `topic-modelled.html` - Terms revolving the topics for modelling.

## Questions we are looking to answer about the Farmers Protest in India:
1. What are the main concerns or topics that are being discussed related to farmers protest in India.
2. What are the general reaction or sentiment of the crowd towards each topic.
3. Which all celebrities voiced out their opinions about the issue? 
4. How does the public feel towards celebrities?
