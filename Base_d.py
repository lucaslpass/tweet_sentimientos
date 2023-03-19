from datetime import datetime
import mysql.connector
from mysql.connector import Error


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
        return self.passwoord
    


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
   
    def create_db(self):
        try:
            self.get_connection() 

            mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS TweetDB (
                                Id      int(90)                        AUTO_INCREMENT,
                                IdTweet varchar(90)                    NOT NULL,
                                Tweet varchar(290)                     NOT NULL,
                                Username varchar(45)                   NOT NULL,
                                Hashtags varchar(120)                  NOT NULL,
                                Datetime datetime                      NOT NULL,
                                Rango varchar(45)                          NULL,
                                Score float(11)                            NULL,
                                PRIMARY KEY (Id)
                                );
                                """
            cursor = self.connection.cursor()
            result = cursor.execute(mySql_Create_Table_Query)
            print("TweetDB Table created successfully ")

        except mysql.connector.Error as error:
            print("TweetDB to create table in MySQL: {}".format(error))
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")

    def drop_bd(self):

        try:
            self.get_connection() 
          
            sql_select_Query = "DROP TABLE IF EXISTS TweetDB;"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            print("TweetDB Table delete successfully ")            

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
 

    def insert(self,idTweet,tweet ,username , hashtags ,fecha  ):
        try:
            self.get_connection()

            cursor = self.connection.cursor()               
            mySql_insert_query = """INSERT INTO TweetDB ( 
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
            print("Record inserted successfully into TweetDB table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")
   
   
    def update(self, id , rango , score ):
        try:
            self.get_connection()
            cursor = self.connection.cursor()               
            mySql_insert_query = """Update TweetDB set Rango = %s, Score = %s where Id = %s"""

            record = (  rango  , float(score) ,int(id))
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

    def get_hashtags(self):
        try:
            self.get_connection()
            sql_Query = "SELECT DISTINCT Hashtags FROM TweetDB"
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

    def get_tweet(self, id ,hastag):
        try:
            self.get_connection()
            sql_Query ="SELECT Id, Tweet, Username FROM TweetDB WHERE Hashtags = %s AND Id = %s LIMIT 1"
            cursor = self.connection.cursor()
            cursor.execute(sql_Query, (hastag,id))
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

    def count_tweets(self, hastag):
        try:
            self.get_connection()
            count_Query = "SELECT COUNT(*) FROM TweetDB WHERE Hashtags = %s"
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
    
    
    def get_first_tweet_id(self, hastag):
        try:
            self.get_connection()
            tweet_Query = "SELECT Id FROM TweetDB WHERE Hashtags = %s LIMIT 1"
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

