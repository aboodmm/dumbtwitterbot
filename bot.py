import twitter
import os
import time
import random

ckey = os.environ["TWITTERAPI"]
csecret = os.environ["TWITTERSECRET"]
access = os.environ["TWITTERACCESS"]
access_secret = os.environ["TWITTERAXSECRET"]

tweetinterval = 60*3 # tweet every 3 minutes

api = twitter.Api(consumer_key=ckey,
						consumer_secret=csecret,
						access_token_key=access,
						access_token_secret=access_secret)

phraselist = []

phrases = open("phrases.txt", "r")

for line in phrases:
	print("Adding line: " + line)
	phraselist.append(line.rstrip())
	
phrases.close()

while True:
	chosen = random.choice(phraselist)
	print("Tweeting this: " + chosen)
	status = api.PostUpdate(chosen)
	time.sleep(tweetinterval)

print(phraselist)
