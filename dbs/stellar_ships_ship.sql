-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: stellar
-- ------------------------------------------------------
-- Server version	5.7.11-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ships_ship`
--

DROP TABLE IF EXISTS `ships_ship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ships_ship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creation_date` datetime(6) NOT NULL,
  `modification_date` datetime(6) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `fabrication_date` datetime(6) NOT NULL,
  `hp` varchar(10) NOT NULL,
  `power` varchar(5) NOT NULL,
  `color` varchar(10) NOT NULL,
  `detection` tinyint(1) NOT NULL,
  `boost` tinyint(1) NOT NULL,
  `passengers` int(11) NOT NULL,
  `reservation_date` datetime(6) DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `lon` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ships_ship_8424d087` (`creation_date`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ships_ship`
--

LOCK TABLES `ships_ship` WRITE;
/*!40000 ALTER TABLE `ships_ship` DISABLE KEYS */;
INSERT INTO `ships_ship` VALUES (1,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship1','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 1','2016-02-11 12:32:42.000000','3000HP','L8','Blue',0,0,3,NULL,NULL,NULL),(2,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship2','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 2','2016-02-11 12:32:42.000000','3001HP','L9','Green',0,0,4,NULL,NULL,NULL),(3,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship3','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 3','2016-02-11 12:32:42.000000','3000HP','L8','Blue',0,0,3,NULL,NULL,NULL),(4,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship4','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 4','2016-02-11 12:32:42.000000','3000HP','L8','Blue',0,0,3,NULL,NULL,NULL),(5,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship5','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 5','2016-02-11 12:32:42.000000','3000HP','L8','Blue',0,0,3,NULL,NULL,NULL),(6,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship6','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 6','2016-02-11 12:32:42.000000','3000HP','L8','Blue',0,0,3,NULL,NULL,NULL),(7,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship7','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 7','2016-02-11 12:32:42.000000','3000HP','L8','Blue',0,0,3,NULL,NULL,NULL),(8,'2016-02-11 12:33:26.047000','2016-02-11 12:33:26.047000','Ship8','http://vignette3.wikia.nocookie.net/starwars/images/c/c7/TIEfighter-Fathead.png/revision/latest?cb=20150310124222','Tie fighter 8','2016-02-11 12:32:42.000000','3000HP','L8','Blue',0,0,3,NULL,NULL,NULL);
/*!40000 ALTER TABLE `ships_ship` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-02-13 17:56:15
