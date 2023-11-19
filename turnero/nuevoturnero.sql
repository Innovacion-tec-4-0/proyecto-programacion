CREATE DATABASE  IF NOT EXISTS `nuevoturnero` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nuevoturnero`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: nuevoturnero
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `historial_tramites`
--

DROP TABLE IF EXISTS `historial_tramites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_tramites` (
  `idHistorial` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int NOT NULL,
  `idTramite` int NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  PRIMARY KEY (`idHistorial`),
  UNIQUE KEY `idHistorial_UNIQUE` (`idHistorial`),
  KEY `idUsuario` (`idUsuario`),
  KEY `idTramite` (`idTramite`),
  CONSTRAINT `historial_tramites_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`),
  CONSTRAINT `historial_tramites_ibfk_2` FOREIGN KEY (`idTramite`) REFERENCES `tramite` (`idTramite`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_tramites`
--

LOCK TABLES `historial_tramites` WRITE;
/*!40000 ALTER TABLE `historial_tramites` DISABLE KEYS */;
INSERT INTO `historial_tramites` VALUES (1,3,1,'Gracias por elegirnos su turno es: 17','2023-11-19','16:31:37');
/*!40000 ALTER TABLE `historial_tramites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tramite`
--

DROP TABLE IF EXISTS `tramite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tramite` (
  `idTramite` int NOT NULL AUTO_INCREMENT,
  `tipode_tramite` varchar(100) NOT NULL,
  PRIMARY KEY (`idTramite`),
  UNIQUE KEY `idTramite_UNIQUE` (`idTramite`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tramite`
--

LOCK TABLES `tramite` WRITE;
/*!40000 ALTER TABLE `tramite` DISABLE KEYS */;
INSERT INTO `tramite` VALUES (1,'Caja'),(2,'Catastro'),(3,'Licencia de conducir'),(4,'Agua'),(5,'Otros'),(6,'Propiedades'),(7,'Comercio'),(8,'Tasas del automotor'),(9,'Servicio Preferencial'),(10,'Cementerio');
/*!40000 ALTER TABLE `tramite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `dni` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `nacimiento` varchar(40) NOT NULL,
  `fallecimiento` varchar(40) DEFAULT NULL,
  `domicilio` varchar(100) NOT NULL,
  `telefono` int NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `estadocivil` varchar(20) DEFAULT NULL,
  `sexo` varchar(10) DEFAULT NULL,
  `observacion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `idUsuario_UNIQUE` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'336','Gaston','Trejo','1988-06-03',NULL,'catamarca',33333333,'gaston@gmail.com','casado','masc','nada'),(2,'33','Juan','Perez','1999-01-01',NULL,'cc',22,'JP@gmail.com','soltero','masc','escorpio'),(3,'303','Caro','Duarte','1982-05-20',NULL,'cordoba',444433,'caro@gmail.com','soltera','fem','tauro'),(4,'285','Victoria','Urcola','1981-05-22',NULL,'la falda',555,'victo@gmail.com','casada','fem','geminis'),(5,'347','Cesar','Martins','1987-03-30',NULL,'la calera',8877,'luqui@gmail.com','casado','masc','milico'),(6,'438','Santi','Ferreyra','2002-05-22',NULL,'arroyito',888,'santi@gmail.com','soltero','masc','redes'),(7,'123','Kevin','Kessler','1995-08-23',NULL,'san francisco',321546789,'kevin@gmail.com','casado','masc','Profe');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-19 16:52:56
