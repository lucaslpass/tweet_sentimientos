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
                print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
   
    def create_db(self):
        try:
            self.get_connection() 

            mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS TweetDB (
                                IdTweet int(45)                        NOT NULL,
                                Tweet varchar(290)                     NOT NULL,
                                Username varchar(45)                   NOT NULL,
                                Hashtags varchar(120)                  NOT NULL,
                                Datetime datetime                      NOT NULL,
                                Retweets int(10)                       NOT NULL,
                                Favourites int(10)                     NOT NULL,
                                Rango varchar(45)                          NULL,
                                Score float(11)                            NULL,
                                PRIMARY KEY (idTweet)
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
 

    def insert(self,idTweet,tweet ,username , hashtags ,fecha , retweets ,favourites  ):
        try:
            self.get_connection()
            hashtags_str = ",".join(hashtags)

            cursor = self.connection.cursor()               
            mySql_insert_query = """INSERT INTO TweetDB ( 
                                    IdTweet,
                                    Tweet ,
                                    Username ,
                                    Hashtags ,
                                    Datetime , 
                                    Retweets ,
                                    Favourites 
                                     
                                    ) 
                                    VALUES (%s , %s , %s , %s , %s , %s , %s  ) """

            record = (int(idTweet),tweet ,username ,hashtags_str  , datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S'), int(retweets) ,int(favourites  ))
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
   
   
    def update(self, idTweet, rango , score ):
        try:
            self.get_connection()
            cursor = self.connection.cursor()               
            mySql_insert_query = """Update TweetDB set Rango = %s,set Score = %s where IdTweet = %s """

            record = (   rango  , score , idTweet  )
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
   

    def export_tweet(self):
        try:
            self.get_connection()
            sql_select_Query = "select * from TweetDB"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")
                return records
                 
