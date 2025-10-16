from typing import TextIO

import tweepy
import json
from run_prompt import execute_gemini
API_KEY = "hyyZYLt2v6Wz3ScjtWyNEnMZd"
API_SECRET_KEY = "2FgiUdao7y30HM9VtzAvu5c1Ku2jTqb51HMl6x0ETldB5ylFZT"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANyM3gEAAAAA3GRXyGoccYLqNe%2F7V%2ByfMTQr1Y4%3DOl667eRvEF8Wjael2bduoXAIk9FJievSWJyjkOUoclMJAYIlJq"
ACCESS_TOKEN = "1956070348182421504-lHDMQwOfXhJGXVCxxctogYVjdPttmW"
ACCESS_TOKEN_SECRET = "I8cnPo6pE0Z80eFVDLvboUZHtBuevogVyn3ZaLr1wBh93"

if __name__ == "__main__":
    try:
        twitterClient = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            wait_on_rate_limit=True,
        )

        user = twitterClient.get_user(username="sundarpichai")

        user_id = user.data.id

        # get tweets
        tweets  = twitterClient.get_users_tweets(
            user_id,
            max_results=50,
            tweet_fields=['created_at', 'public_metrics', 'text']
        )

        # save the tweets to json file
        with open("extracted_tweets.json", "w") as json_file:
            # [].map(e=>e.toString())
            json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



