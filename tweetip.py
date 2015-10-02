#!/usr/bin/python3
'''
Created on Mar 7, 2014

@author: sotiris 2
'''
## testing
from twython import Twython
import urllib.request as ur
from time import time
import os.path
import sys

homedir = os.path.expanduser('~')
twitteripdir = '.twitterip'
path = os.path.join(homedir,twitteripdir)

try:
    with open(os.path.join(path,'APP_KEY'),'r') as f:
        APP_KEY = f.read().strip()  # Customer Key here
    with open(os.path.join(path,'APP_SECRET'),'r') as f:
        APP_SECRET = f.read().strip()  # Customer Key here
    with open(os.path.join(path,'OAUTH_TOKEN'),'r') as f:
        OAUTH_TOKEN = f.read().strip()  # Customer Key here
    with open(os.path.join(path,'OAUTH_TOKEN_SECRET'),'r') as f:
        OAUTH_TOKEN_SECRET = f.read().strip()  # Customer Key here
    with open(os.path.join(path,'ipsite_url'),'r') as f:
        getipSite = f.read().strip()

except:
    print ("EXITING! Settings files not found or not readable.")
    print ("Make sure APP_KEY and others exist in",path)
    sys.exit(1)

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

getipRequest = ur.Request(getipSite)
getipResponse = ur.urlopen(getipRequest)
getip = (getipResponse.read().decode('utf-8'))

getTime = int(time())
if len(sys.argv)>1:
    hostname = sys.argv[1]
else: 
    hostname = 'pi'

tweet = hostname + ":" + getip + ":" + str(getTime)

# print (tweet)

twitter.update_status(status=tweet)
