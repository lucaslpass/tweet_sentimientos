from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from Base_d import Bd
import os
import time
bd=Bd()
bd.set_user("lVC$4")
bd.set_host("localhost")
bd.set_datebase("tweet_mx")
bd.set_passwoord("anes%ar&t$noc") 
def format_time(seconds):
    # Calcular horas, minutos y segundos
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    # Crear una cadena de formato para mostrar la hora
    time_format = "{:02d}:{:02d}:{:02d}".format(h, m, s)
    return time_format



total_tweets1 = bd.count_tweets_score_null()

actual=0
processed_tweets = 1
start_time = time.time()
while bd.get_first_tweet_score_null()!= None:
    start_time1 = time.time()
    
    

    total_tweets = bd.count_tweets_score_null()

    tweet=bd.get_Id_tweet(bd.get_first_tweet_score_null())
    os.system('clear')

    # Cálculo de tiempo estimado restante en minutos
    
 
    print("procesados",actual,"de",total_tweets1,"restantes:",total_tweets," //",tweet[0],"//",tweet[3])
    # Imprimir progreso y tiempo estimado restante en minutos
    if actual>0:
 
        print(f"Tiempo transcurrido: {format_time(int(time.time() - start_time))}")

        print(f"Tiempo restante    : {format_time(int(media))}")




    
    print(tweet[2])
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
    os.system('clear')

    actual+=1
    elapsed_time_t=(time.time() - start_time1)
    elapsed_time  = time.time() - start_time
    estimated_time_remaining_sec = (elapsed_time / actual) * (total_tweets)
    estimated_time_remaining_sec_t = (  elapsed_time_t) *  (total_tweets )
    
    media =( (estimated_time_remaining_sec + estimated_time_remaining_sec_t) / 2)
    
  
 
    os.system('clear')
print("fin")