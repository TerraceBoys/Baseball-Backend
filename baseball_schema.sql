-- MySQL dump 10.13  Distrib 5.5.52, for Linux (x86_64)
--
-- Host: localhost    Database: baseball
-- ------------------------------------------------------
-- Server version	5.5.52

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
-- Table structure for table `game_state`
--

DROP TABLE IF EXISTS `game_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_state` (
  `gs_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `gs_score_1` int(11) NOT NULL DEFAULT '0',
  `gs_score_2` int(11) NOT NULL DEFAULT '0',
  `gs_inning` int(11) NOT NULL DEFAULT '1',
  `gs_batting` int(11) NOT NULL DEFAULT '0',
  `gs_base_1` int(11) NOT NULL DEFAULT '0',
  `gs_base_2` int(11) NOT NULL DEFAULT '0',
  `gs_base_3` int(11) NOT NULL DEFAULT '0',
  `gs_strikes` int(11) NOT NULL DEFAULT '0',
  `gs_balls` int(11) NOT NULL DEFAULT '0',
  `gs_outs` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`gs_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_state`
--

LOCK TABLES `game_state` WRITE;
/*!40000 ALTER TABLE `game_state` DISABLE KEYS */;
INSERT INTO `game_state` VALUES (1,0,0,1,0,0,0,0,0,0,0),(2,0,0,1,0,0,0,0,0,0,0),(9,0,0,1,0,0,0,0,0,0,0),(12,0,0,1,0,0,0,0,0,0,0),(13,0,0,1,0,0,0,0,0,0,0),(14,0,0,1,0,0,0,0,0,0,0),(15,0,0,1,0,0,0,0,0,0,0),(16,0,0,1,0,0,0,0,0,0,0),(17,0,0,1,0,0,0,0,0,0,0),(18,0,0,1,0,0,0,0,0,0,0),(19,0,0,1,0,0,0,0,0,0,0),(20,0,0,1,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `game_state` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-19 19:25:27
