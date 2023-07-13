# Allows you to send HTTP requests using Python.
import requests
# Provides first-class OAuth library support for requests.
from requests_oauthlib import OAuth1
# Provides a portable way of using operating system dependent functionality
import os

# lines: 9 - 12, Creating variables and assigning Keys, Tokens, and Secrets to them for passing
consumer_key = os.environ.get("Consumer_key")
consumer_secret = os.environ.get("Consumer_secret")
access_token = os.environ.get("Access_token")
access_token_secret = os.environ.get("Access_token_secret")

# Creating function "random_affirmation".
def random_affirmation():
    # Reaches out to endpoint.
    affirmation = requests.get("https://www.affirmations.dev/").json()
    # Returns "affirmation" from endpoint.
    return affirmation["affirmation"]

# Creating function "format_affirmation".
def format_affirmation(affirmation):
    # Formatting our affirmation in to a postable format.
    return {"text": "{}".format(affirmation) + "."}

# Creating function "connect_to_auth" that authenticates before posting said affirmation.
def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
    return url, auth

# Creating function "sendTweet", that posts our affirmation.
def sendTweet(event, context):
    affirmation = random_affirmation()
    payload = format_affirmation(affirmation)
    url, auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    request = requests.post(
        auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
    )