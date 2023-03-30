from transformers import pipeline
import csv

classifier = pipeline('sentiment-analysis', 
                      model="nlptown/bert-base-multilingual-uncased-sentiment")

hashtags1=["AIFA","Bayern Munich","Floricienta","Himno","John Kerry","NINE OR NONE","Ohtani","QSMP","Teatro del Pueblo","Corea del Norte","ESENCIA OUT NOW","Scarlett Camberos","Humbe","Jenare","#floresamarillas","Surinam","TU VALOR","The Rock","Japón","SNIPER", "REINA", "AZUL","Shenhe","#21deMarzo","#FelizMartes","#WorldBaseballClassic","Alicia Keys","Américas","Aries","Benito Juárez","Black Adam",]
hashtags2=["Checo","Akron","América","Chivas","Cisneros","Lara","Pocho","Rayados","Romo","Mozo","Cabecita","Vega","Tigres","Andrada","Chima","Pizarro","#ClasicoNacional","Rafa", "Puente","Pumas","Norma Piña","San José","Henry","Judas","Verstappen","Gonzalo","Barça","Leo Suárez","Violencia","Zócalo"]
hashtags3=[ "Pumas","#SaudiArabianGP","Acarreados","Alonso","Barça","Barcelona","Carvajal","Checo","chivas","Clasismo","Henry","Red Bull","San José","Taylor","Verstappen","Zócalo","Louis","Tomlinson","América","Kessie","Rafa Puente","Xavi","Benzema","Lara","Madrid"]
for hashtag in hashtags1:
    archivo = f"/home/lucsa/Documentos/Nao_py_data_analyst/captura/backups/backup"+hashtag+".csv"
    f=open(archivo, newline='') 
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        
        results = classifier(row[1])
        for result in results:
            print(row[0])
            print(f"polaridad: {result['label']}, score: {round(result['score'], 4)}")