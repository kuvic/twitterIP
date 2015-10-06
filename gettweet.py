'''
Created on Mar 7, 2014

@author: sotiris
'''
## testing
import os.path
import sys
from twython import Twython

class tweets:
    """ creates list of tweets from user home"""
    def __init__(self):
        """input is twitter object and number of tweets to get from home timeline"""
        # settings for oauth files
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
        except:
            print ("EXITING! Settings files not found or not readable.")
            print ("Make sure APP_KEY and others exist in",path)
            sys.exit(1)

        # mow that we have the settings lets create twitter object
        self.twitterObject = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    def getTweets(self,n):
        """after class object is initialized getTweets is called
        to retrieve tweets from twitter object"""
        self.tweetList = self.twitterObject.get_home_timeline(count=n)
        self.numberOfTweets = n
        self.splittedTweets = []
        for t in self.tweetList:
            text = t['text'].split(':')		# warning, split is different on v3.4
            self.splittedTweets.append(text)

    def tweetIp(self, n):
        """get ip of nth tweet"""
        return self.splittedTweets[n][1]

    def tweetName(self, n):
        return self.splittedTweets[n][0]

    def tweetTime(self, n):
        return self.splittedTweets[n][2]

    def tweetIps(self):
        """return all ips in list"""
        ipList = []
        for i in self.splittedTweets:
            if len(i)==3:
                ipList.append(i[1])
        return ipList

    def tweetNames(self):
        """return all computer names in list"""
        nameList = []
        for i in self.splittedTweets:
            if len(i)==3:
                nameList.append(i[0])
        return nameList

    def tweetIpOf(self, computer):
        for i in self.splittedTweets:
            if i[0] == computer:
                return i[1]
            





if __name__ == "__main__":
    
    # Create class object
    A = tweets()
    # call function to get tweets and create list
    A.getTweets(10)
    # get IP of macserver - TODO CHANGE TO SYS ARG
    print (A.tweetIpOf('macserver'))
    print (A.tweetNames())
