import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl():
    
    twitter_handle="JustinTrudeau"

    access_key="8u2oVAzRmYPzFJI9EZZa6aSgC"
    access_secret="nOUIhMG4osHxtN15uJ8MTuspBmUCQ91x46PCLt1ePKE7Wbn0TX"
    consumer_key="100182855-JfDRqnZeWDE9zQZ4pJePWBm1G8XkQ37OsCnF1ger"
    consumer_secret="8MaRQFurK1HmSE2HpcwHtiSHWqbT9lUNYuCvWSCROikSC"

    #Twitter authentication

    auth= tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    #Creating an API object
    api = tweepy.API(auth)

    tweets= api.user_timeline(screen_name='@'+twitter_handle,count=200,include_rts=False,tweet_mode ='extended')
    #print(tweets)

    tweet_list=[]

    for tweet in tweets:
        text=tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text': text,  
                        'favorite_count': tweet.favorite_count,
                        'retweet_count': tweet.retweet_count,
                        'created_at': tweet.created_at}

        tweet_list.append(refined_tweet)
    df=pd.DataFrame(tweet_list)
    df.to_csv('s3://marc-airflow-youtube-bucket/tweets.csv')