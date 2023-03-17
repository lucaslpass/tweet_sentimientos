


import datetime 

import snscrape.modules.twitter as sn_twitter
import pandas as pd



class Tweet_mx:
    
    def __init__(self ,text = "" , user_name = "" ,since = '', until = "", geocode = "",retweet = "" , replies = "" ) :
        
        self.querry= ""
        self.text  =text
        self.lang  = "es"
        self.user_name = user_name
        self.since =since
        self.until = until
        self.geocode = geocode
        self.retweet = retweet
        self.replies = replies
    
    def set_text(self,text):
        self.text=text    
    def set_user_name(self,user_name):
        self.user_name=user_name         
    def set_since(self,since):
        self.since=since  
    def set_until(self,until):
        self.until=until
    def set_geocode(self,geocode):
        self.geocode=geocode    
    def set_retweet(self,retweet):
        self.retweet=retweet
    def set_replies(self,replies):
        self.replies=replies
    
    def get_text(self):
        return self.text    
    def get_user_name(self):
        return self.user_name
    def get_since(self):
        return self.since  
    def get_until(self):
        return self.until
    def get_geocode(self):
        return self.geocode       
    def get_retweet(self):
        return self.retweet
    def get_replies(self):
        return self.replies    
    def get_querry(self):
        self.set_querry()
        return self.querry
    
    def set_querry(self): 

        q  = self.text 
        q += f" lang:{self.lang}"      
        if self.user_name !='': 

            q += f" from:{self.user_name}"              

        if self.until =='': 

            self.until = datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d') 

        q += f" until:{self.until}" 

        if self.since =='': 

            self.since = datetime.datetime.strftime(datetime.datetime.strptime(self.until, '%Y-%m-%d') -  datetime.timedelta(days=1), '%Y-%m-%d') 
        else:  
            q += f" since:{self.since}"
        
        if self.get_geocode() !="":    
            q+=f' geocode:{self.geocode}'      
   
        q += f" exclude:retweets" 
     
        q += f" exclude:replies" 

        self.querry = q   
     
    def extraer_tweets( self, cont, entero ):
        
        tweets=[]
        
        for tweet in sn_twitter.TwitterSearchScraper(self.get_querry()).get_items():
        
            if len(tweets)== cont:
                break
            if entero == 1:     
                tweets.append(tweet)
           
            else:
                tweets.append([ tweet.id, tweet.date, tweet.content, tweet.username])
        
        if entero == 1:
            tweets_df1 = pd.DataFrame(tweets)
        else:
            tweets_df1 = pd.DataFrame(tweets , columns=[ 'Tweet Id', 'Datetime', 'Tweet', 'Username'])      
        
        return  tweets_df1