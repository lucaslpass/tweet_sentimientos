CREATE DATABASE `tweet_mx` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE tweet_mx;
  
CREATE TABLE `TweetDB` (
  `IdTweet` int(45) NOT NULL ,
  `TTopic` varchar(45) NOT NULL,
  `Datetime` datetime NOT NULL,
  `Username` varchar(45)  NOT NULL,
  `Tweet` varchar(290) NOT NULL,
  `Rango` varchar(45)  NULL,
  `score` Float(11)  NULL,	

  PRIMARY KEY (`idTweet`),
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb3;







