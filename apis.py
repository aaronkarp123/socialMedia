# importing the module
import tweepy
import re
import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time

# authentication
auth = None

def setup(filename):
	#read and store key information
	keyfile = open(filename, "r")
	data = keyfile.read().split('\n')
	keys = []
	for i in range(len(data)-1):
		keys.append(re.findall('"([^"]*)"', data[i])[0])
	consumer_key = keys[0]
	consumer_secret = keys[1]
	access_token = keys[2]
	access_token_secret = keys[3]
	usr = keys[4]
	psw = keys[5]
	return consumer_key, consumer_secret, access_token, access_token_secret, usr, psw

def tweet(text, url, consumer_key, consumer_secret, access_token, access_token_secret):
	#set up twitter authentication
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	status = text
	if (url is not None):
		status = api.update_with_media(url, text)
	api.update_status(status = status)

def insta(text, url, usr, psw):
	print(usr + "  --  " + psw)
	command = "instapy -u " + usr + " -p " + psw + " -f " + url + " -t '" + text + "'"
	print(command)
	os.system(command)

def main():
	consumer_key, consumer_secret, access_token, access_token_secret, usr, psw = setup("keys.txt")
	options = input("Type (tweet, insta, both): ")
	text = input("Text: ")
	media = input("Media file (y or n): ")
	filename = None
	if (media == "y"):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	if (options == "insta" or options == "both"):
		if (filename == None):
			print("Error: Must select media for Instagram")
			return
	if (options == "tweet" or options == "both"):
		try:
			tweet(text, filename, consumer_key, consumer_secret, access_token, access_token_secret)
		except Exception as e:
			print(e)
		
	if (options == "insta" or options == "both"):
		try:
			insta(text, filename, usr, psw)
		except Exception as e:
			print(e)
		

if __name__ == "__main__":
    main()