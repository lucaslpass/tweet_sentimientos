


import datetime 

import snscrape.modules.twitter as sn_twitter



class Tweet_mx:
    
    def __init__(self ,text = "" , user_name = "",geocode = "" ,since = "", until = "", retweet = "" , replies = "" ) :
        
        self.querry= ""
        self.text  =text
        self.lang  = ":es"
        self.user_name = user_name
        self.geocode = geocode
        self.since =since
        self.until = until
        self.retweet = retweet
        self.replies = replies
    
    def set_text(self,text):
        self.text=text    
    def set_user_name(self,user_name):
        self.user_name=user_name    
    def set_geocode(self,geocode):
        self.user_name=geocode     
    def set_since(self,since):
        self.since=since  
    def set_until(self,until):
        self.until=until
    def set_retweet(self,retweet):
        self.retweet=retweet
    def set_replies(self,replies):
        self.replies=replies
    
    def get_text(self):
        return self.text    
    def get_user_name(self):
        return self.user_name
    def get_geocode(self):
        return self.geocode       
    def get_since(self):
        return self.since  
    def get_until(self):
        return self.until
    def get_retweet(self):
        return self.retweet
    def get_replies(self):
        return self.replies    
    def get_querry(self):
        self.set_querry()
        return self.querry
    
    def set_querry(self): 

        q  = self.text 
        q += self.lang    
        if self.user_name !='': 

            q += f" from:{self.user_name}" 
        if self.geocode != '':
            mxdf ='19.42847 ,  -99.12766, 500km'
            q+= f"geocode:{mxdf}"
        else:
            q+= f"geocode:{self.geocode}"             

        if self.until =='': 

            self.until = datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d') 

        q += f" until:{self.until}" 

        if self.since =='': 

            self.since = datetime.datetime.strftime(datetime.datetime.strptime(self.until, '%Y-%m-%d') -  datetime.timedelta(days=1), '%Y-%m-%d') 
        q += f" since:{self.since}" 
    
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
        return tweets    