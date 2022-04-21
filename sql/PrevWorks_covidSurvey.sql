-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: db-mysql-sfo2-95612-do-user-9925891-0.b.db.ondigitalocean.com    Database: PrevWorks
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '8a37705a-2187-11ec-9527-82f4811bc759:1-6255,
cb4f808b-3fcf-11ec-938e-12a7b1409b34:1-53194';

--
-- Table structure for table `covidSurvey`
--

DROP TABLE IF EXISTS `covidSurvey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `covidSurvey` (
  `surveyId` int NOT NULL AUTO_INCREMENT,
  `hadCovid` bit(1) NOT NULL,
  `healthcare` bit(1) NOT NULL,
  `fever` bit(1) NOT NULL,
  `loss` bit(1) NOT NULL,
  `pain` bit(1) NOT NULL,
  `cough` bit(1) NOT NULL,
  `breath` bit(1) NOT NULL,
  `conjunctivitis` bit(1) NOT NULL,
  `gi` bit(1) NOT NULL,
  `userId` int NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`surveyId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `covidSurvey`
--

LOCK TABLES `covidSurvey` WRITE;
/*!40000 ALTER TABLE `covidSurvey` DISABLE KEYS */;
/*!40000 ALTER TABLE `covidSurvey` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-06 17:30:21
