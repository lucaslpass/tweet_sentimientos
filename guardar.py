import csv 
from Base_d import Bd
import os
import time
import pandas as pd



bd=Bd()
bd.set_user("lVC$4")
bd.set_host("localhost")
bd.set_datebase("tweet_mx")
bd.set_passwoord("anes%ar&t$noc")   

total_tweets1 = bd.count_tweets_score_null()

# Crear un archivo CSV y escribir la fila de encabezados
hashtags1=["AIFA","Bayern Munich","Floricienta","Himno","John Kerry","NINE OR NONE","Ohtani","QSMP","Teatro del Pueblo","Corea del Norte","ESENCIA OUT NOW","Scarlett Camberos","Humbe","Jenare","#floresamarillas","Surinam","TU VALOR","The Rock","Japón","SNIPER", "REINA", "AZUL","Shenhe","#21deMarzo","#FelizMartes","#WorldBaseballClassic","Alicia Keys","Américas","Aries","Benito Juárez","Black Adam",]
hashtags2=["Checo","Akron","América","Chivas","Cisneros","Lara","Pocho","Rayados","Romo","Mozo","Cabecita","Vega","Tigres","Andrada","Chima","Pizarro","#ClasicoNacional","Rafa", "Puente","Pumas","Norma Piña","San José","Henry","Judas","Verstappen","Gonzalo","Barça","Leo Suárez","Violencia","Zócalo"]
hashtags3=[ "Pumas","#SaudiArabianGP","Acarreados","Alonso","Barça","Barcelona","Carvajal","Checo","chivas","Clasismo","Henry","Red Bull","San José","Taylor","Verstappen","Zócalo","Louis","Tomlinson","América","Kessie","Rafa Puente","Xavi","Benzema","Lara","Madrid"]
for hashtag in hashtags1: 
    t=bd.get_tweets_by_hashtag(hashtag)
    print(hashtag)
    df = pd.DataFrame(t, columns=["Id", "Tweet"])
    df.to_csv("/home/lucsa/Documentos/Nao_py_data_analyst/captura/backups/backup"+hashtag+".csv")
for hashtag in hashtags2: 
    t=bd.get_tweets_by_hashtag(hashtag)
    print(hashtag)
    df = pd.DataFrame(t, columns=["Id", "Tweet"])
    df.to_csv("/home/lucsa/Documentos/Nao_py_data_analyst/captura/backups/backup"+hashtag+".csv")
for hashtag in hashtags3: 
    t=bd.get_tweets_by_hashtag(hashtag)
    print(hashtag)
    df = pd.DataFrame(t, columns=["Id", "Tweet"])
    df.to_csv("/home/lucsa/Documentos/Nao_py_data_analyst/captura/backups/backup"+hashtag+".csv")
