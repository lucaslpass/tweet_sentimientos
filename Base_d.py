from datetime import datetime
import mysql.connector  
from mysql.connector import Error
import os

class Bd :
    def __init__(self ,host= "" ,database= "", user= "", passwoord ="" ) :
        self.host =host
        self.datebase =database
        self.user = user
        self.passwoord= passwoord
        self.connection= self.get_connection()
    
    def set_host(self,host):
        self.host = host
    def set_datebase(self,datebase):
        self.datebase = datebase
    def set_user(self,user):
        self.user = user
    def set_passwoord(self, passwoord):
        self.passwoord = passwoord    
    def get_host(self):
        return self.host 
    def get_datebase(self):
        return self.datebase
    def get_user(self):
        return self.user
    def get_host(self):
        return self.host
    


    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                 database=self.datebase,
                                                 user= self.user,
                                                 password=self.passwoord)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                #print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                #print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
            os.system('clear')
   
    def create_dbs(self):
        try:
            self.get_connection() 

            # Crear tabla TweetDB1
            tweet_table_query = """CREATE TABLE IF NOT EXISTS TweetDB1 (
                                Id      int(90)                        AUTO_INCREMENT,
                                IdTweet varchar(90)                    NOT NULL,
                                Tweet varchar(290)                     NOT NULL,
                                Username varchar(45)                   NOT NULL,
                                Hashtags varchar(120)                  NOT NULL,
                                Datetime datetime                      NOT NULL,
                                Score int(11)                            NULL,
                                PRIMARY KEY (Id)
                                );
                                """
            cursor = self.connection.cursor()
            cursor.execute(tweet_table_query)
            print("TweetDB Table created successfully ")

            # Crear tabla HashtagCount
            hashtag_table_query = """CREATE TABLE IF NOT EXISTS HashtagCount (
                                Id      int(90)                        AUTO_INCREMENT,
                                Hashtag varchar(90)                    NOT NULL,
                                Word varchar(90)                       NOT NULL,
                                Count_W int(90)                        NOT NULL,
                                PRIMARY KEY (Id)
                                );
                                """
            cursor.execute(hashtag_table_query)
            print("HashtagCount Table created successfully ")

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (self.connection.is_connected()):
                cursor.close()
                self.connection.close()
                #print("MySQL connection is closed")

    
    def drop_db(self):
        try:
            self.get_connection() 
        
            sql_select_Query = "DROP TABLE IF EXISTS TweetDB1;"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            print("TweetDB1 Table deleted successfully ")            

            #sql_select_Query = "DROP TABLE IF EXISTS HashtagDB1;"
            #cursor = self.connection.cursor()
            #cursor.execute(sql_select_Query)
            #print("HashtagDB1 Table deleted successfully ")            
    
        except mysql.connector.Error as e:
            print("Error deleting table from MySQL", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
    

    def insert_into_tweetdb1(self,idTweet,tweet ,username , hashtags ,fecha):
        try:
            self.get_connection()

            cursor = self.connection.cursor()               
            mySql_insert_query = """INSERT INTO TweetDB1 ( 
                                    IdTweet,
                                    Tweet ,
                                    Username ,
                                    Hashtags ,
                                    Datetime 
                                  
                                    ) 
                                    VALUES (%s , %s , %s , %s , %s  ) """

            record = (int(idTweet),tweet ,username ,hashtags  , datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S'))
            cursor.execute(mySql_insert_query, record)
            self.connection.commit()
            #print("Record inserted successfully into TweetDB1 table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                #print("MySQL connection is closed")
   
    def insert_into_hashtagdb(self,hashtag, word, count_w):
        try:
            self.get_connection()

            mySql_insert_query = """INSERT INTO HashtagCount (Hashtag, Word, Count_W) 
                                VALUES (%s , %s , %s  );"""
            record = ( hashtag , word , int(count_w) )
            cursor =self.connection.cursor()
            cursor.execute(mySql_insert_query,record)
            self.connection.commit()
            #print("Record inserted successfully into HashtagDB1 table")


        except mysql.connector.Error as e:
            print("Error inserting data into HashtagDB1 table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()

    def delete_w_from_hashtagdb(self, word):
        try:
            self.get_connection()
            mySql_delete_query = """DELETE  FROM HashtagCount WHERE Word = %s;"""
            record =  [word]
            cursor = self.connection.cursor()
            cursor.execute(mySql_delete_query, record)
            self.connection.commit()
            print("Record deleted successfully from HashtagCount table")

        except mysql.connector.Error as e:
            print("Error deleting data from HashtagCount table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()

    def get_top_100_words_by_count_w(self):
        try:
            self.get_connection()
            cursor = self.connection.cursor()

            sql_query = """SELECT hc.Word, MAX(hc.Count_W) AS Max_Count
                                FROM HashtagCount hc
                                WHERE hc.Word NOT IN (
                                  SELECT t.Hashtags
                                  FROM  TweetDB1 as t
                                  WHERE t.Hashtags IS NOT NULL
                                )
                              
                                GROUP BY hc.Word
                                ORDER BY Max_Count DESC
                                LIMIT 100;"""
            cursor.execute(sql_query)

            top_10_words = cursor.fetchall()

            return top_10_words

        except mysql.connector.Error as e:
            print("Error reading data from HashtagCount table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")

    def update_into_tweetdb1(self, id  , score ):
        try:
            self.get_connection()
            cursor = self.connection.cursor()               
            mySql_insert_query = """Update TweetDB1 set  Score = %s where Id = %s"""

            record = ( score ,id)
            cursor.execute(mySql_insert_query, record)
            self.connection.commit()
            #print("Record inserted successfully into TweetDB table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                #print("MySQL connection is closed")

   
    def get_hashtags_into_tweetdb1(self):
        try:
            self.get_connection()
            sql_Query = "SELECT DISTINCT Hashtags FROM TweetDB1"
            cursor = self.connection.cursor()
            cursor.execute(sql_Query)
            # get all records
            records = cursor.fetchall()

            hashtags = []
            for record in records:
                hashtags.extend(record[0].split())

            return hashtags

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")            

    def get_tweets(self):
        try:
            self.get_connection()
            sql_Query ="SELECT Id, Tweet, Hashtags ,Username  FROM TweetDB1 WHERE Score IS NOT NULL "
            cursor = self.connection.cursor()
            cursor.execute(sql_Query)
            # get the first record
            record = cursor.fetchall()

            return record

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")
    
    def get_tweets_h_s_d(self):
        try:
            self.get_connection()
            sql_Query ="SELECT  Hashtags ,Score , Datetime  FROM TweetDB1 WHERE Score IS NOT NULL "
            cursor = self.connection.cursor()
            cursor.execute(sql_Query)
            # get the first record
            record = cursor.fetchall()

            return record

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")


    def get_tweets_by_hashtag(self, hashtag):
        try:
            self.get_connection()
            sql_Query = "SELECT Id, Tweet,Score FROM TweetDB1 WHERE Hashtags LIKE '%" + hashtag + "%'"
            cursor = self.connection.cursor()
            cursor.execute(sql_Query)
            # get all records
            records = cursor.fetchall()

            tweets = []
            for record in records:
                tweets.append((record[0], record[1]))

            return tweets

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")

    def get_hashtag_w_counts(self, hashtag):
        try:
            self.get_connection()

            mySql_Select_Query = "SELECT Word, Count_W FROM HashtagCount WHERE Hashtag = %s"
            cursor = self.connection.cursor()
            cursor.execute(mySql_Select_Query, (hashtag,))

            records = cursor.fetchall()
            hashtag_counts = {}

            for row in records:
                word = row[0]
                count = row[1]
                hashtag_counts[word] = count

            return hashtag_counts

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()


    def get_Id_tweet(self, id ):
        try:
            self.get_connection()
            sql_Query ="SELECT Id, Tweet, Hashtags ,Username, Score FROM TweetDB1 WHERE Id = %s LIMIT 1"
            cursor = self.connection.cursor()
            cursor.execute(sql_Query, (id,))
                #print("MySQL connection is closed")
            # get the first record
            record = cursor.fetchone()

            return record

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")
    
    def get_score_tweet(self ):
        try:
            self.get_connection()
            sql_Query ="SELECT  Hashtags , Score FROM TweetDB1 "
            cursor = self.connection.cursor()
            cursor.execute(sql_Query)
            #print("MySQL connection is closed")
            # get the first record
            record = cursor.fetchall()
            return record
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")


    def count_tweets(self, hastag):
        try:
            self.get_connection()
            count_Query = "SELECT COUNT(*) FROM TweetDB1 WHERE Hashtags = %s"
            cursor = self.connection.cursor()
            cursor.execute(count_Query, (hastag,))
            count_result = cursor.fetchone()[0]

            return count_result

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")
    
    def count_tweets_score_null(self):
        try:
            self.get_connection()
            count_Query = "SELECT COUNT(*) FROM TweetDB1 WHERE Score IS Null "
            cursor = self.connection.cursor()
            cursor.execute(count_Query)
            count_result = cursor.fetchone()[0]

            return count_result

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")
    
    
    
    def get_first_tweet_hastag(self, hastag):
        try:
            self.get_connection()
            tweet_Query = "SELECT Id FROM TweetDB1 WHERE Hashtags = %s LIMIT 1"
            cursor = self.connection.cursor()
            cursor.execute(tweet_Query, (hastag,))
            tweet_result = cursor.fetchone()[0]

            return tweet_result

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")

    def get_first_tweet_score_null(self):
        try:
            self.get_connection()
            tweet_query = "SELECT Id FROM TweetDB1 WHERE Score IS NULL LIMIT 1"
            cursor = self.connection.cursor()
            cursor.execute(tweet_query)
            tweet_result = cursor.fetchone()

            return tweet_result[0] if tweet_result else None

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                #print("MySQL connection is closed")
