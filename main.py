from sys import api_version
import tweepy
import time

token_file_name = 'Tokens_kp.txt'  #Add your file name
all_keys = open(token_file_name, 'r').read().splitlines()

api_key = all_keys[0] 
api_secret = all_keys[1]
access_token = all_keys[2]
access_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key,api_secret)
authenticator.set_access_token(access_token,access_secret)

api = tweepy.API(authenticator, wait_on_rate_limit= True)
time.sleep(600)
#api.create_friendship(screen_name = 'AshTee42')
#api.update_status('There must be a reason why I am posting a tweet for the first time! #randomthought')
api.retweet(1363352214559891456)

