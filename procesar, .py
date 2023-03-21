from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from Base_d import Bd
import os

tweet_words = []

bd=Bd()
bd.set_user("lVC$4")
bd.set_host("localhost")
bd.set_datebase("tweet_mx")
bd.set_passwoord("anesartnoc")
hashtags= bd.get_hashtags()
inicios=[]
limits=[]
inicio=0
total=0
actual=0
i=0
j=0

for hashtag in hashtags:
    primero=bd.get_first_tweet_hastag(hashtag)
    inicios.append(primero)
    cantidad=bd.count_tweets(hashtag)
    total+=cantidad
    cantidad+=primero

    limits.append(cantidad)
print(len(limits))

while inicio < limits[i]  :
    
    inicio=j+inicios[i]
 
    tweet = bd.get_tweet(inicio, hashtags[i])
    actual+=1

    print("procesando",actual,"de",total , tweet)

    if tweet[3]== None:
        tweet_proc = " ".join(tweet[1])
        tweet_proc = " ".join(tweet[2])
        # load model and tokenizer
        roberta = "cardiffnlp/twitter-roberta-base-sentiment"
        model = AutoModelForSequenceClassification.from_pretrained(roberta)
        tokenizer = AutoTokenizer.from_pretrained(roberta)
        labels = ['Negative', 'Neutral', 'Positive']
        # sentiment analysis
        encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
        # output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
        output = model(**encoded_tweet)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        l = labels[2]
        s = scores[2]
        bd.update(tweet[0],l,s)
    j+=1
    inicio+=j
    
    if inicio > limits[i]:
        if i > 1-len(limits):
            i+=1
        inicio=0
        j=0
    os.system('clear')