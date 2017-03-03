from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import csv
import sys
#consumer key, consumer secret, access token, access secret.
ckey="vlSH1S0Ur83uGIdCHxnSq7UZF"
csecret="yN5KSSrZpRpQUH6FpzdFEiv3ZABaXLvFL3LBKnTSes0WLnK8hW"
atoken="744064694-dy5MWH1Ostm6BR2Bwj5CvtqvZAZK9OiWyL98TEfd"
asecret="mFuwQRLbpkIbH6ajSkA6oLUqntY0mhzmRo6xtnVwCdOl0"
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

#emoji may give trouble when printing (not saving) so creating a translation table
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

f = open('tweepy_tweets.csv', 'w')
writer = csv.writer(f)
writer.writerow(["id","created_at","text"])

#for status in tweepy.Cursor(api.mentions_timeline).items():
# print(status)
#for page in tweepy.Cursor(api.mentions_timeline).pages():
# print(page)

alltweets = tweepy.Cursor(api.search, q='AmazonEcho').items()
for tweet in alltweets:
 #print(str(tweet).translate(non_bmp_map))
 outtweets = [tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
 writer.writerow(outtweets)
 print(outtweets)
f.close()