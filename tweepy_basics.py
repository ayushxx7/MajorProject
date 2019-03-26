import tweepy

consumer_key = "iqor2ni478MD0Ata0e8QjPaHw"
consumer_secret = "JOYSFgbVbblUk3sksgQrdQg2Qxqa636mCEp63bM2cnbzmypSZU"
access_token = "2908245252-VByUAQba8B9Z5x24aLlZB3Wv1FHQsEtXiGrUtOc"
access_token_secret   = "odvzxR949GLXFQLf9df7Yk8n3GTiBl5dSD5I0S5VJMG4x"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)