---
id: Twitter_API
aliases: []
tags:
  - coding
  - apis
dg-publish: true
---
## Twitter API

### Developer Apps
1. [Developer apps portal page](https://developer.twitter.com/en/portal/projects-and-apps)
2. [[OAuth 2.0]]

Accessing the Twitter API and Twitter Ads API requires a set of authentication credentials, also known as keys and tokens, that you must pass with each request. These credentials can come in different forms depending on the type of authentication that is required by the specific endpoint that you are using.

>[!NOTE] API Key and Secret 
> API Key and Secret(==Consumer Key and secret==) :  the most fundamental credentials required to access the Twitter API , These credentials act as the u==sername and password== for your Twitter App, and are used by the Twitter API to understand which App requests are coming from.These credentials can be used by [authentication endpoints](https://developer.twitter.com/en/docs/authentication/api-reference) to generate additional credentials, such as [user Access Tokens and Secrets](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens), and [Bearer Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens). You also need to use these credentials along with Access Tokens and other authorization parameters to [authorize requests](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request) that require OAuth 1.0a User Context authentication

> [!NOTE] Access Token and Secret
> **[Access Token and Secret](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens):** In general, ==Access Tokens represent the user that you are making the request on behalf of.== The ones that you can generate via the developer portal represent the user that owns the App. You will use these to authenticate requests that require [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). If you would like to make requests on behalf of another user, you will need to use the 3-legged OAuth flow for them to authorize you.

>[!NOTE] Client ID and Client Secret
>**[Client ID and Client Secret](https://developer.twitter.com/content/en/docs/authentication/oauth-2-0/user-access-token):** These credentials are used to obtain a user Access Token with OAuth 2.0 authentication. Similar to OAuth 1.0a, the user Access Tokens are used to authenticate requests that provide private user account information or perform actions on behalf of another account but, with fine-grained scope for greater control over what access the client application has on the user.

> [!NOTE] App only Access Token
>  **[App only Access Token](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0/bearer-tokens):** You will use this token when making requests to endpoints that responds with information publicly available on Twitter

```python
import base64
import os

import requests
import tweepy
from cryptocmd import CmcScraper
from requests_oauthlib import OAuth1

def halving_time():
    TARGET_BLOCK = 840000
    current_block = get_current_btc_block()
    if TARGET_BLOCK == current_block:
        post_twitter()

def get_current_btc_block():
    watcher_guru_url = "https://api.watcher.guru/bitcoinhalving/predictions"
    current_status = requests.get(watcher_guru_url).json()
    return current_status["current"]["block_number"]

def post_twitter():
    # FIXME: remove the API Keys from This method
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    # Authenticate
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    # Twitter API v2 endpoint for posting a tweet
    url = "https://api.twitter.com/2/tweets"

    # Twitter API v2 endpoint for uploading media
    upload_url = "https://upload.twitter.com/1.1/media/upload.json"

    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

    def upload_video():
        video_path = "video.mp4"
        # Read video data
        with open(video_path, "rb") as video_file:
            video_data = video_file.read()

        # Upload the video
        upload_headers = {"Content-Type": "video/mp4"}
        upload_response = requests.post(
            upload_url, data=video_data, headers=upload_headers, auth=auth
        )

        print(upload_response.json())

        exit(1)
        # Get the media ID from the response
        # try:
        #     media_id = upload_response.json()["media_id_string"]
        # except KeyError:
        #     print("Error: Invalid response from media upload endpoint")
        #     print(upload_response.text)
        # # exit(1)

        media_id = upload_response.json()["data"]["media_id"]

        # Twitter API v2 endpoint for posting a tweet
        tweet_url = "https://api.twitter.com/2/tweets"

        # Tweet text
        tweet_text = "This is a tweet with a video."

        # Request payload
        payload = {"text": tweet_text, "media": {"media_ids": [media_id]}}

        # Make the POST request
        response = requests.post(tweet_url, auth=auth, json=payload)

        # Check the response
        if response.status_code == 201:
            print("Tweet with video posted successfully!")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    def upload_image():

        # Image file path

        image_path = "./../images/cat.jpg"

        # Read image data
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        # Upload the image
        upload_headers = {"Content-Type": "application/octet-stream"}
        upload_response = requests.post(
            upload_url, data=image_data, headers=upload_headers, auth=auth
        )
        print(upload_response.json())
        # Get the media ID from the response
        media_id = upload_response.json()["data"]["media_id"]
        print(media_id)
        exit(0)
        # Twitter API v2 endpoint for posting a tweet
        # tweet_url = "https://api.twitter.com/2/tweets"

        # Tweet text
        tweet_text = "Hello, world! This is a tweet with an image."

        # Request payload
        payload = {"text": tweet_text, "media": {"media_ids": [media_id]}}

        # Tweet text
        tweet_text = "This is second tweet"

        # Request payload
        payload = {"text": tweet_text}

        # Make the POST request
        response = requests.post(url, auth=auth, json=payload)

        # Check the response
        if response.status_code == 201:
            print("Tweet posted successfully!")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    upload_image()

post_twitter()

```

### How to acquire an API Key and Secret

1. [Sign up for a Twitter developer account](https://developer.twitter.com/en/apply-for-access)
2. Create a [Twitter App](https://developer.twitter.com/en/docs/apps) within the [developer portal](https://developer.twitter.com/en/docs/developer-portal). Note that if you would like to use [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/early-access), you must add your Twitter App to a [Project](https://developer.twitter.com/en/docs/projects).
