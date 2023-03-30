import csv
import clean_t
import pandas as pd
from  Tweet_mx import Tweet_mx
from Base_d import Bd
import Path as pth
from transformers import pipeline 
import os
bd=Bd()
bd.set_user("lVC$4")
bd.set_host("localhost")
bd.set_datebase("tweet_mx")
bd.set_passwoord("anes%ar&t$noc")  

def analisis_sentimientos(tweet):
    classifier = pipeline('sentiment-analysis', 
    model="nlptown/bert-base-multilingual-uncased-sentiment")  
    results = classifier(tweet)
   
    return results
def guardar(hashtag,sub,total):
    archivo = f"/home/lucsa/Documentos/Nao_py_data_analyst/captura/backups/backup"+hashtag+".csv"
    f=open(archivo, newline='') 
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        result=analisis_sentimientos(row[0])
        n=result[0]['label']
        bd.update_into_tweetdb1(row[0],int(n[0]))
        os.system('clear')
        print(sub,'de',total)
        print(hashtag,i  )
    print("terminado")
    

def main():

    hashtags=["Checo","Akron","América","Chivas","Cisneros","Lara",
              "Pocho","Rayados","Romo","Mozo","Cabecita","Vega","Tigres","Andrada",
              "Chima","Pizarro","#ClasicoNacional","Rafa", "Puente","Pumas","Norma Piña",
              "San José","Henry","Judas","Verstappen","Gonzalo","Barça","Leo Suárez",
              "Violencia","Zócalo","Pumas","#SaudiArabianGP","Acarreados","Alonso",
              "Barça","Barcelona","Carvajal","Checo","chivas","Clasismo","Henry","Red Bull",
              "San José","Taylor","Verstappen","Zócalo","Louis","Tomlinson","América",
              "Kessie","Rafa Puente","Xavi","Benzema","Lara","Madrid","AIFA","Bayern Munich",
              "Floricienta","Himno","John Kerry","NINE OR NONE","Ohtani","QSMP",
              "Teatro del Pueblo","Corea del Norte","ESENCIA OUT NOW","Scarlett Camberos",
              "Humbe","Jenare","#floresamarillas","Surinam","TU VALOR","The Rock","Japón",
              "SNIPER", "REINA", "AZUL","Shenhe","#21deMarzo","#FelizMartes",
              "#WorldBaseballClassic","Alicia Keys","Américas","Aries","Benito Juárez",
              "Black Adam"]
    print(bd.get_Id_tweet(bd.get_first_tweet_score_null()))   # for i,hashtag in enumerate(hashtags):
   #     
   #     guardar(hashtag,i,len(hashtags))

main()
            