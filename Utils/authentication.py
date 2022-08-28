from Utils import credentials
import tweepy


def create_api():
    consumer_key = credentials.API_KEY
    consumer_secret = credentials.API_SECRET
    access_token = credentials.ACCESS_TOKEN
    access_token_secret = credentials.ACCESS_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    return api

