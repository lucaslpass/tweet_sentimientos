
import re
import unicodedata

def clean_accents(text):
    # Eliminar signos de puntuación
    text = re.sub(r'[^\w\s]+', ' ', text)
    # Eliminar emojis
    text = text.encode('ascii', 'ignore').decode('utf-8')
    # Eliminar acentos
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    # Convertir todo el texto a minúsculas
    text = text.lower()
    return text

def clave_valor_maximo(diccionario):
    clave_maxima = max(diccionario, key=diccionario.get)
    valor_maximo = diccionario[clave_maxima]
    return clave_maxima, valor_maximo

def count_words(text):
    exclude_words = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'al', 'del', 'lo', 'le', 'y', 'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les', 'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy', 'voy', 'porque', 'he', 'son', 'solo', 'tengo', 'muy','ja','JAJA','JAja']
    top_words = {}
    words = text.lower().split()
    for word in words:
        if word not in exclude_words:
            top_words[word] = top_words.get(word, 0) + 1
    return top_words

def clean_sig(text):
    # Eliminar signos de puntuación
    text = re.sub('[^\w\s]|_', ' ', text)


    # Separar emojis de palabras
    text = re.sub('([^\w\s])', r' \1 ', text)
    
    # Convertir todo a minúsculas
    text = text.lower()
    
    # Eliminar espacios en blanco adicionales
    text = re.sub('\s+', ' ', text).strip()
    
    return text

def date_clean(date):
    date_clean = date.split("+")[0]
    return date_clean
def score_clean(date):
    date_clean = date.split(" ")[0]
    return date_clean

def tweet_clean_links(tweet):

    patron = r'https?://[^\s]+'

    tweet_sin_links = re.sub(patron, '',tweet)
    return tweet_sin_links

def tweet_clean_caracters(tweet):
    tweet_clean_caracters= re.sub(r'[@#](\w+)', r'\1', tweet)
    return tweet_clean_caracters
    



