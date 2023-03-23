


import datetime 

import snscrape.modules.twitter as sn_twitter
import pandas as pd



class Tweet_mx:
    
    def __init__(self ,hashtag = "" , user_name = "" ,since = '', until = "", geocode = "",retweet = "" , replies = "" , path = "",folder = "") :
        
        self.querry     =    ""
        self.path       =    path
        self.folder     =    folder   
        self.hashtag    =    hashtag
        self.lang       =    "es-mx"
        self.user_name  =    user_name
        self.since      =    since
        self.until      =    until
        self.geocode    =    geocode
        self.retweet    =    retweet
        self.replies    =    replies
    
    def set_folder(self,folder):
        self.folder=folder
    def set_hashtag(self,hashtag):
        self.hashtag=hashtag    
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
    
    def get_folder(self):
        return self.folder
    def get_hashtag(self):
        return self.hashtag    
    def get_user_name(self):
        return self.user_name
    def get_since(self):
        return self.since  
    def get_until(self):
        return self.until
    def get_lang(self):
        return self.lang
    def get_geocode(self):
        return self.geocode       
    def get_retweet(self):
        return self.retweet
    def get_replies(self):
        return self.replies    
    def get_querry(self):
        self.set_querry()
        return self.querry
    def get_path(self):
        self.set_path()
        return self.path
    
    def set_querry(self): 

        q  = self.get_hashtag() 
        q += f" lang:{self.get_lang()}"      
        if self.get_user_name() !='': 

            q += f" from:{self.get_user_name()}"              

        if self.get_until() =='': 

            self.set_until(datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d')) 

        q += f" until:{self.get_until()}" 

        if self.get_since() =='': 

            self.set_since(datetime.datetime.strftime(datetime.datetime.strptime(self.until, '%Y-%m-%d') -  datetime.timedelta(days=1), '%Y-%m-%d') ) 
        else:  
            q += f" since:{self.get_since()}"
        
        if self.get_geocode() !="":    
            q+=f' geocode:{self.get_geocode()}'      
   
        q += f" exclude:retweets" 
     
        q += f" exclude:replies" 

        self.querry = q   
     
    def set_path( self):
        path=self.get_folder()
        path+=f'{self.get_hashtag()}_{self.get_until()}.csv'
        self.path = path
        
   
   
    def extraer_tweets( self, cont, entero ):
        
        tweets=[]
        
        for i,tweet in enumerate  (sn_twitter.TwitterSearchScraper(self.get_querry()).get_items()):
        
            if i== cont:
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