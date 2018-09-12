# importing the module
import tweepy
import re
import os

# personal information
consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""

usr = "ar"
psw = "da"

# authentication
auth = None

def setup(filename):
	#read and store key information
	keyfile = open(filename, "r")
	data = keyfile.read().split('\n')
	keys = []
	for i in range(len(data)):
		keys.append(re.findall('"([^"]*)"', data[i])[0])
	consumer_key = data[0]
	consumer_secret = data[1]
	access_token = data[2]
	access_token_secret = data[3]
	usr = data[4]
	psw = data[5]

	#set up twitter authentication
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

def tweet(text, url=None):
	api = tweepy.API(auth)
	status = text
	if (url is not None):
		status = api.update_with_media(url, text)
	api.update_status(status = status)

def insta(text, url):
	command = "instapy -u " + usr + " -p " + psw + " -f " + url + " -t '" + text + "'"
	os.system(command)

setup("keys.txt")