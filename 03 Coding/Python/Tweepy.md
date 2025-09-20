---
id: Tweepy
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
#### Example 

```python
import tweepy

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

```

1. **By X dev Platform**

```bash
pip install requests tweepy requests_oauthlib flask

```

```python 
import base64
import hashlib
import os
import re
import requests
import tweepy
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template

```

3. To start, you will need to set up your application as a Flask app. After that, you will need to set a secret key for your app.

```python
app = Flask(__name__)
app.secret_key = os.urandom(50)

```

5. **By Project Raspberry pi**

```python
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "Hello World!"
twitter.update_status(status=message)
print("Tweeted: " + message)

```

3. **By Geeks for Geeks** 

```python
# importing the module`

import tweepy

# personal details`

consumer_key = "xxxxxxxxxxxxxxxx"

consumer_secret = "xxxxxxxxxxxxxxxx"

access_token = "xxxxxxxxxxxxxxxx"

access_token_secret = "xxxxxxxxxxxxxxxx"

# authentication of consumer key and secret`

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret`

`auth.set_access_token(access_token, access_token_secret)`

`api` `=` `tweepy.API(auth)`

`# update the status`

api.update_status(status="Hello Everyone !")

```

#errror
 You currently have access to a subset of Twitter API v2 endpoints and limited v1.1 endpoints (e.g. media post, oauth) only. If you need access to this endpoint, you may need a different access level. You can learn more here: https://developer.twitter.com/en/portal/product
 
[[Twitter API]]
## References
1. https://developer.twitter.com/en/docs/tutorials/tweeting-media-v2
2. https://docs.tweepy.org/en/stable/
3. https://www.google.com/amp/s/www.geeksforgeeks.org/tweet-using-python/amp/
4. 