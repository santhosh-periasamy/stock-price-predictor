import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
  

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)  
api = tweepy.API(auth) 

def clean_tweet(self, tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

def get_tweet_sentiment(self, tweet):  
    analysis = TextBlob(self.clean_tweet(tweet)) 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'

def get_tweets(self, query, count = 10):  
                           
    tweets = [] 
 
    fetched_tweets = api.search(q = query, count = count) 

    for tweet in fetched_tweets:  
        parsed_tweet = {} 
        parsed_tweet['text'] = tweet.text  
        parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text) 

        if tweet.retweet_count > 0: 
            if parsed_tweet not in tweets: 
                tweets.append(parsed_tweet) 
        else: 
            tweets.append(parsed_tweet) 

    return tweets 

ticker = "MSFT"
hashtag = "#" + ticker
tweets = get_tweets(query = hashtag, count = 200) 

ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']  
ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 

ntweets_percentage = (len(ptweets)/len(tweets))*100 
ptweets_percentage = (len(ntweets)/len(tweets))*100 
  
if(ptweets_percentage > 50):
    print(ticker + " is expected to increase in value")
else:
    print(ticker + " is expected to decrease in value")
          