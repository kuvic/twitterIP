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
import socket

def tweet(hostname = ''):
    '''Just the hostname as argument.
    If called from bash it can be called without arguments'''    
    # SETTINGS - location of settings files
    homedir = os.path.expanduser('~')
    twitteripdir = '.twitterip'
    path = os.path.join(homedir,twitteripdir)
    
    if hostname == '':
        # set hostname from host
        hostname = socket.gethostname()
    
    # check and get data from settings files
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
    
    # if not exit with code 1
    except:
        print ("EXITING! Settings files not found or not readable.")
        print ("Make sure APP_KEY and others exist in",path)
        return 1
    
    # make twitter object
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    # get ip address of router using external site PHP code
    getipRequest = ur.Request(getipSite)
    getipResponse = ur.urlopen(getipRequest)
    getip = (getipResponse.read().decode('utf-8'))
    
    # get time from system
    getTime = int(time())

    # compose tweet text
    tweet_text = hostname + ":" + getip + ":" + str(getTime)
    
    # actually tweet at last
    twitter.update_status(status=tweet_text)
    return 0

if __name__ == "__main__":
    # if call with arguments then get hostname from arguments
    if len(sys.argv)>1:
        host = sys.argv[1]
    # else get hostname from system
    else: 
        host = ''

    # tweet it - object evaluated - tweeting and returning!
    if tweet(host) == 1:
        sys.exit(1)

