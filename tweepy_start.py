from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="vlSH1S0Ur83uGIdCHxnSq7UZF"
csecret="yN5KSSrZpRpQUH6FpzdFEiv3ZABaXLvFL3LBKnTSes0WLnK8hW"
atoken="744064694-dy5MWH1Ostm6BR2Bwj5CvtqvZAZK9OiWyL98TEfd"
asecret="mFuwQRLbpkIbH6ajSkA6oLUqntY0mhzmRo6xtnVwCdOl0"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["AmazonEcho"])