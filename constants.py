import tweepy
API_KEY = "3LZMqTNyz316RJ7ktyCuDbHvl"
API_SECRET_KEY = "Pya7iCoAvWRvi8kgASrjOt3uqMbmJtstidlSTRqPQTFEpF72kP"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANyM3gEAAAAAzAGMA4j00lAguvtSBXHcZuppP6s%3DMezLC3tbz4LkSBwqvpcD4TQFqKxZkujYpAcCEbez1vN2oig0tN"
ACCESS_TOKEN = "1956070348182421504-0yNIDqQnTbxNnRnBdTlNZdPgbTWrND"
ACCESS_TOKEN_SECRET = "ZfztwzZwC8vbQqLMtbfRsjM4cV28BSS6wk3lZG0MxbhTZ"

twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    wait_on_rate_limit=True,
)