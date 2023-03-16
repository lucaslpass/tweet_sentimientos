import snscrape.modules.twitter as sn_twitter


  
def extraer_tweets(  cont, entero ):
        
    tweets=[]
    for tweet in sn_twitter.TwitterSearchScraper("#PiensoEnTi").get_items():
        if len(tweets)== cont:
            break
        if entero == 1:     
            tweets.append(tweet)
        else:
            tweets.append([ tweet.id, tweet.date, tweet.content, tweet.username])
    return tweets   

print(extraer_tweets(3,1),"\n")