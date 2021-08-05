-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: credito
-- ------------------------------------------------------
-- Server version	8.0.24

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

--
-- Table structure for table `cadastra`
--

DROP TABLE IF EXISTS `cadastra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cadastra` (
  `ID_Cadastra` int NOT NULL AUTO_INCREMENT,
  `FK_Pessoa` int DEFAULT NULL,
  `FK_Plano` int DEFAULT NULL,
  PRIMARY KEY (`ID_Cadastra`),
  KEY `FK_Pessoa` (`FK_Pessoa`),
  KEY `FK_Plano` (`FK_Plano`),
  CONSTRAINT `cadastra_ibfk_1` FOREIGN KEY (`FK_Pessoa`) REFERENCES `pessoa_juridica` (`FK_Pessoa`),
  CONSTRAINT `cadastra_ibfk_2` FOREIGN KEY (`FK_Plano`) REFERENCES `plano` (`ID_Plano`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadastra`
--

LOCK TABLES `cadastra` WRITE;
/*!40000 ALTER TABLE `cadastra` DISABLE KEYS */;
INSERT INTO `cadastra` VALUES (5,5,5),(6,6,6),(7,7,7),(8,8,8);
/*!40000 ALTER TABLE `cadastra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contrata`
--

DROP TABLE IF EXISTS `contrata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contrata` (
  `id` int NOT NULL AUTO_INCREMENT,
  `FK_Pessoa` int DEFAULT NULL,
  `FK_Cadastra` int DEFAULT NULL,
  `nota_avaliacao` int NOT NULL,
  `discricao_avaliacao` varchar(500) NOT NULL,
  `data_avaliacao` date NOT NULL,
  `data_contrato` date NOT NULL,
  `valor_mensal` int NOT NULL,
  `status` varchar(7) NOT NULL DEFAULT 'inativo',
  `validade` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contrata_ibfk_1` (`FK_Pessoa`),
  KEY `contrata_ibfk_2` (`FK_Cadastra`),
  CONSTRAINT `contrata_ibfk_1` FOREIGN KEY (`FK_Pessoa`) REFERENCES `pessoa_fisica` (`FK_Pessoa`),
  CONSTRAINT `contrata_ibfk_2` FOREIGN KEY (`FK_Cadastra`) REFERENCES `cadastra` (`ID_Cadastra`),
  CONSTRAINT `contrata_chk_1` CHECK (((`nota_avaliacao` >= 0) and (`nota_avaliacao` <= 5))),
  CONSTRAINT `contrata_chk_2` CHECK ((`valor_mensal` >= 0)),
  CONSTRAINT `contrata_chk_3` CHECK (((`status` = _utf8mb4'inativo') or (`status` = _utf8mb4'ativo')))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contrata`
--

LOCK TABLES `contrata` WRITE;
/*!40000 ALTER TABLE `contrata` DISABLE KEYS */;
INSERT INTO `contrata` VALUES (1,1,5,2,'Ótimo Plano','2001-05-05','2001-05-05',145,'ativo','12 meses'),(2,2,6,3,'Plano Regular','2002-06-06','2002-06-06',153,'ativo','12 meses'),(3,3,7,4,'Excelente Plano','2003-07-07','2003-07-07',162,'ativo','12 meses'),(4,4,8,5,'Melhor Plano que já tive','2004-08-08','2004-08-08',170,'ativo','12 meses');
/*!40000 ALTER TABLE `contrata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa`
--

DROP TABLE IF EXISTS `pessoa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pessoa` (
  `ID_Pessoa` int NOT NULL AUTO_INCREMENT,
  `nome_completo` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefone` int NOT NULL,
  `rua` varchar(50) NOT NULL,
  `numero` int NOT NULL,
  `cep` int NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  PRIMARY KEY (`ID_Pessoa`),
  UNIQUE KEY `ID_Pessoa` (`ID_Pessoa`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa`
--

LOCK TABLES `pessoa` WRITE;
/*!40000 ALTER TABLE `pessoa` DISABLE KEYS */;
INSERT INTO `pessoa` VALUES (1,'Victor Martins1','Victor1@gmail.com',988578569,'Rua A',23,45600000,'Itabuna','Bahia'),(2,'Victor Martins2','Victor2@gmail.com',988663514,'Rua B',24,45600000,'Itabuna','Bahia'),(3,'Victor Martins3','Victor3@gmail.com',988523697,'Rua C',25,45600000,'Itabuna','Bahia'),(4,'Victor Martins4','Victor4@gmail.com',988745236,'Rua D',26,45600000,'Itabuna','Bahia'),(5,'Victor Martins5','Victor5@gmail.com',988745632,'Rua E',27,45600000,'Itabuna','Bahia'),(6,'Victor Martins6','Victor6@gmail.com',988456321,'Rua F',28,45600000,'Itabuna','Bahia'),(7,'Victor Martins7','Victor7@gmail.com',988745632,'Rua H',29,45600000,'Itabuna','Bahia'),(8,'Victor Martins8','Victor8@gmail.com',991253617,'Rua I',30,45600000,'Itabuna','Bahia');
/*!40000 ALTER TABLE `pessoa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa_fisica`
--

DROP TABLE IF EXISTS `pessoa_fisica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pessoa_fisica` (
  `FK_Pessoa` int NOT NULL,
  `cpf` varchar(50) DEFAULT NULL,
  UNIQUE KEY `FK_Pessoa` (`FK_Pessoa`),
  UNIQUE KEY `cpf` (`cpf`),
  CONSTRAINT `pessoa_fisica_ibfk_1` FOREIGN KEY (`FK_Pessoa`) REFERENCES `pessoa` (`ID_Pessoa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa_fisica`
--

LOCK TABLES `pessoa_fisica` WRITE;
/*!40000 ALTER TABLE `pessoa_fisica` DISABLE KEYS */;
INSERT INTO `pessoa_fisica` VALUES (1,'08545678936'),(3,'15935784632'),(2,'85236974141'),(4,'98732124989');
/*!40000 ALTER TABLE `pessoa_fisica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa_juridica`
--

DROP TABLE IF EXISTS `pessoa_juridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pessoa_juridica` (
  `FK_Pessoa` int DEFAULT NULL,
  `cnpj` varchar(50) DEFAULT NULL,
  `nomefantasia` varchar(50) NOT NULL,
  UNIQUE KEY `FK_Pessoa` (`FK_Pessoa`),
  KEY `cnpj` (`cnpj`),
  CONSTRAINT `pessoa_juridica_ibfk_1` FOREIGN KEY (`FK_Pessoa`) REFERENCES `pessoa` (`ID_Pessoa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa_juridica`
--

LOCK TABLES `pessoa_juridica` WRITE;
/*!40000 ALTER TABLE `pessoa_juridica` DISABLE KEYS */;
INSERT INTO `pessoa_juridica` VALUES (5,'56487923145678','TurboNet'),(6,'31456785648792','TorpedoNet'),(7,'14567856487392','NetCoon'),(8,'41568734567892','Oi Velox');
/*!40000 ALTER TABLE `pessoa_juridica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plano`
--

DROP TABLE IF EXISTS `plano`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plano` (
  `ID_Plano` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `velocidade` int DEFAULT NULL,
  `preco` int NOT NULL,
  `abrangencia` varchar(500) NOT NULL,
  `status` varchar(7) DEFAULT 'inativo',
  `discricao` varchar(50) NOT NULL,
  PRIMARY KEY (`ID_Plano`),
  CONSTRAINT `plano_chk_1` CHECK ((`preco` > 0)),
  CONSTRAINT `plano_chk_2` CHECK (((`status` = _utf8mb4'ativo') or (`status` = _utf8mb4'inativo')))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plano`
--

LOCK TABLES `plano` WRITE;
/*!40000 ALTER TABLE `plano` DISABLE KEYS */;
INSERT INTO `plano` VALUES (5,'Turbonet 150mb',180,170,'Itabuna-Ílheus','ativo','Turbonet 150 megas'),(6,'TorpedoNet',192,180,'Itabuna-Ílheus	','ativo','TorpedoNet 160 megas'),(7,'NetCoon',204,190,'Itabuna-Ílheus	','ativo','Netcoon 170 megas'),(8,'Oi velox 180 megas',216,200,'Itabuna-Ílheus	','ativo','Oi velox180 megas');
/*!40000 ALTER TABLE `plano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vw_contratosefetivos`
--

DROP TABLE IF EXISTS `vw_contratosefetivos`;
/*!50001 DROP VIEW IF EXISTS `vw_contratosefetivos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_contratosefetivos` AS SELECT 
 1 AS `nome_completo`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vw_contratosefetivos`
--

/*!50001 DROP VIEW IF EXISTS `vw_contratosefetivos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_contratosefetivos` AS select `pessoa`.`nome_completo` AS `nome_completo` from (`contrata` join `pessoa`) where (`pessoa`.`ID_Pessoa` = `contrata`.`FK_Pessoa`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 21:21:33
