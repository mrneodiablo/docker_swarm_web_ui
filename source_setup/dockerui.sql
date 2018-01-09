-- MySQL dump 10.13  Distrib 5.5.50, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: dockerui
-- ------------------------------------------------------
-- Server version	5.5.50

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add driver networks',1,'add_drivernetworks'),(2,'Can change driver networks',1,'change_drivernetworks'),(3,'Can delete driver networks',1,'delete_drivernetworks'),(4,'Can add driver volumes',2,'add_drivervolumes'),(5,'Can change driver volumes',2,'change_drivervolumes'),(6,'Can delete driver volumes',2,'delete_drivervolumes'),(7,'Can add logs login logout',3,'add_logsloginlogout'),(8,'Can change logs login logout',3,'change_logsloginlogout'),(9,'Can delete logs login logout',3,'delete_logsloginlogout'),(10,'Can add logs user',4,'add_logsuser'),(11,'Can change logs user',4,'change_logsuser'),(12,'Can delete logs user',4,'delete_logsuser'),(13,'Can add user permissions',5,'add_userpermissions'),(14,'Can change user permissions',5,'change_userpermissions'),(15,'Can delete user permissions',5,'delete_userpermissions'),(16,'Can add permissions',6,'add_permissions'),(17,'Can change permissions',6,'change_permissions'),(18,'Can delete permissions',6,'delete_permissions'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add permission',8,'add_permission'),(23,'Can change permission',8,'change_permission'),(24,'Can delete permission',8,'delete_permission'),(25,'Can add user',9,'add_user'),(26,'Can change user',9,'change_user'),(27,'Can delete user',9,'delete_user'),(28,'Can add group',10,'add_group'),(29,'Can change group',10,'change_group'),(30,'Can delete group',10,'delete_group'),(31,'Can add content type',11,'add_contenttype'),(32,'Can change content type',11,'change_contenttype'),(33,'Can delete content type',11,'delete_contenttype'),(34,'Can add session',12,'add_session'),(35,'Can change session',12,'change_session'),(36,'Can delete session',12,'delete_session'),(37,'Can add product',13,'add_product'),(38,'Can change product',13,'change_product'),(39,'Can delete product',13,'delete_product'),(40,'Can add registry',14,'add_registry'),(41,'Can change registry',14,'change_registry'),(42,'Can delete registry',14,'delete_registry');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$JnzjNRKm0n79$ldTzNWgYL9z+ZllknrrAxrezphn611xDbj7zhtuXHr0=','2016-11-14 03:03:11',1,'dongvt','','','',1,1,'2016-11-01 21:46:27'),(5,'pbkdf2_sha256$36000$M0rOqRaEKw2a$MNCVjQYhpJ5ZIaFR/awW5T2OAqwME/MERus7oyjeItk=',NULL,0,'admin','Admin','Super','',0,1,'2016-11-14 09:17:07');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-11-02 03:09:05','1','admin',1,'[{\"added\": {}}]',6,1),(2,'2016-11-02 03:09:20','2','container_admin',1,'[{\"added\": {}}]',6,1),(3,'2016-11-02 03:09:29','3','container_read_only',1,'[{\"added\": {}}]',6,1),(4,'2016-11-02 03:09:47','1','dongvt',1,'[{\"added\": {}}]',5,1),(5,'2016-11-02 03:13:49','4','node_admin',1,'[{\"added\": {}}]',6,1),(6,'2016-11-02 03:14:20','5','node_read_only',1,'[{\"added\": {}}]',6,1),(7,'2016-11-02 03:15:00','6','image_admin',1,'[{\"added\": {}}]',6,1),(8,'2016-11-02 03:21:03','1','dongvt',3,'',5,1),(9,'2016-11-02 03:21:13','2','dongvt',1,'[{\"added\": {}}]',5,1),(10,'2016-11-02 03:21:19','3','dongvt',1,'[{\"added\": {}}]',5,1),(11,'2016-11-02 03:21:24','4','dongvt',1,'[{\"added\": {}}]',5,1),(12,'2016-11-02 04:01:01','1','htcpg1',1,'[{\"added\": {}}]',13,1),(13,'2016-11-02 04:01:34','2','dmhmp2',1,'[{\"added\": {}}]',13,1),(14,'2016-11-02 11:33:56','4','dongvt',3,'',5,1),(15,'2016-11-02 11:33:56','3','dongvt',3,'',5,1),(16,'2016-11-02 11:34:07','2','dongvt',3,'',5,1),(17,'2016-11-02 11:34:25','5','dongvt',1,'[{\"added\": {}}]',5,1),(18,'2016-11-02 11:36:00','6','dongvt',1,'[{\"added\": {}}]',5,1),(19,'2016-11-02 14:23:06','1','local',1,'[{\"added\": {}}]',2,1),(20,'2016-11-02 14:25:04','1','bridge',1,'[{\"added\": {}}]',1,1),(21,'2016-11-02 14:25:15','2','macvlan',1,'[{\"added\": {}}]',1,1),(22,'2016-11-02 14:25:31','3','host',1,'[{\"added\": {}}]',1,1),(23,'2016-11-02 14:25:37','4','null',1,'[{\"added\": {}}]',1,1),(24,'2016-11-04 06:49:42','1','dmhmp1',1,'[{\"added\": {}}]',13,1),(25,'2016-11-04 06:50:26','2','dmhmp1',1,'[{\"added\": {}}]',13,1),(26,'2016-11-04 06:51:44','1','dmhmp1',2,'[{\"changed\": {\"fields\": [\"scope\"]}}]',13,1),(27,'2016-11-04 06:59:40','2','dmhmp1',2,'[{\"changed\": {\"fields\": [\"scope\"]}}]',13,1),(28,'2016-11-04 06:59:47','1','dmhmp1',2,'[{\"changed\": {\"fields\": [\"scope\"]}}]',13,1),(29,'2016-11-04 06:59:51','2','dmhmp1',2,'[{\"changed\": {\"fields\": [\"scope\"]}}]',13,1),(30,'2016-11-04 07:14:14','3','htcpg1',1,'[{\"added\": {}}]',13,1),(31,'2016-11-04 07:15:02','4','htcpg1',1,'[{\"added\": {}}]',13,1),(32,'2016-11-05 02:41:42','1','gs2_registry',1,'[{\"added\": {}}]',14,1),(33,'2016-11-05 02:41:51','1','gs2_registry',2,'[]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'admin','logentry'),(10,'auth','group'),(8,'auth','permission'),(9,'auth','user'),(11,'contenttypes','contenttype'),(12,'sessions','session'),(1,'swarm_ui','drivernetworks'),(2,'swarm_ui','drivervolumes'),(3,'swarm_ui','logsloginlogout'),(4,'swarm_ui','logsuser'),(6,'swarm_ui','permissions'),(13,'swarm_ui','product'),(14,'swarm_ui','registry'),(5,'swarm_ui','userpermissions');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-11-01 21:46:04'),(2,'auth','0001_initial','2016-11-01 21:46:04'),(3,'admin','0001_initial','2016-11-01 21:46:04'),(4,'admin','0002_logentry_remove_auto_add','2016-11-01 21:46:04'),(5,'contenttypes','0002_remove_content_type_name','2016-11-01 21:46:04'),(6,'auth','0002_alter_permission_name_max_length','2016-11-01 21:46:04'),(7,'auth','0003_alter_user_email_max_length','2016-11-01 21:46:04'),(8,'auth','0004_alter_user_username_opts','2016-11-01 21:46:04'),(9,'auth','0005_alter_user_last_login_null','2016-11-01 21:46:04'),(10,'auth','0006_require_contenttypes_0002','2016-11-01 21:46:04'),(11,'auth','0007_alter_validators_add_error_messages','2016-11-01 21:46:04'),(12,'auth','0008_alter_user_username_max_length','2016-11-01 21:46:04'),(13,'sessions','0001_initial','2016-11-01 21:46:04'),(14,'swarm_ui','0001_initial','2016-11-01 21:46:04'),(15,'swarm_ui','0002_product','2016-11-02 03:59:27'),(16,'swarm_ui','0003_auto_20161104_1337','2016-11-04 06:38:00'),(17,'swarm_ui','0004_auto_20161104_1343','2016-11-04 06:43:42'),(18,'swarm_ui','0005_auto_20161104_1348','2016-11-04 06:48:55'),(19,'swarm_ui','0006_auto_20161104_1403','2016-11-04 07:04:08'),(20,'swarm_ui','0007_registry','2016-11-05 02:39:49');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7jhte8goi0uhspcbllibrm97ed8bxarv','Y2RkMWZkYzkzMjY1YzI0YzU1OTYyN2Q2NGQwOTA5MmFhMGY0NGI0Yjp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwiX2F1dGhfdXNlcl9oYXNoIjoiMjM1OTFhNmYxZGEzYWNmZGQxOTlhZjBhMTc4YTlkMTE5OTZmYjQxNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJwZXJtaXNzaW9uIjpbXX0=','2016-11-15 22:37:28'),('bxe3jab82t751kj1b77y3yknz014pns9','MjI0NWVhZjk2YzczYWM5ZTliMTRlZDY5YTc3MTM3MzkzMDYzNGYyMTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6WyI4IiwiMSJdfQ==','2016-11-18 03:58:45'),('dsrqat3j5hx1e1w6mnhqt63oajtd6loz','MjI0NWVhZjk2YzczYWM5ZTliMTRlZDY5YTc3MTM3MzkzMDYzNGYyMTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6WyI4IiwiMSJdfQ==','2016-11-24 09:20:00'),('if0h9aifge80uywta5msc0m684akjc88','NjIzNGIzNjc4MzliZDM0MDkzYTUzYzZhNmViNzFlNTgxMDAyOTcyNTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6W119','2016-11-15 22:35:22'),('mi7t5wvfm7aa7gr23smx5vplg47dgmmh','MjI0NWVhZjk2YzczYWM5ZTliMTRlZDY5YTc3MTM3MzkzMDYzNGYyMTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6WyI4IiwiMSJdfQ==','2016-11-24 07:39:54'),('mxzf2yv7w44hod5j1pzdxy4ldqvuvb60','MjI0NWVhZjk2YzczYWM5ZTliMTRlZDY5YTc3MTM3MzkzMDYzNGYyMTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6WyI4IiwiMSJdfQ==','2016-11-24 17:46:15'),('pji8n6u9fj47dmjis568uqdb1txw4846','MjI0NWVhZjk2YzczYWM5ZTliMTRlZDY5YTc3MTM3MzkzMDYzNGYyMTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6WyI4IiwiMSJdfQ==','2016-11-28 09:16:35'),('x0x053xbd6bw6j0hbn65om67vp0bsxg6','MjI0NWVhZjk2YzczYWM5ZTliMTRlZDY5YTc3MTM3MzkzMDYzNGYyMTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6WyI4IiwiMSJdfQ==','2016-11-27 16:46:19'),('xgg9rldpncfs9cuwwq83p3mx2lctog4j','MjI0NWVhZjk2YzczYWM5ZTliMTRlZDY5YTc3MTM3MzkzMDYzNGYyMTp7InVzZXJuYW1lIjoiZG9uZ3Z0IiwicGVybWlzc2lvbiI6WyI4IiwiMSJdfQ==','2016-11-23 08:51:04');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_drivernetworks`
--

DROP TABLE IF EXISTS `swarm_ui_drivernetworks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_drivernetworks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `driver` varchar(32) NOT NULL,
  `scope` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_drivernetworks`
--

LOCK TABLES `swarm_ui_drivernetworks` WRITE;
/*!40000 ALTER TABLE `swarm_ui_drivernetworks` DISABLE KEYS */;
INSERT INTO `swarm_ui_drivernetworks` VALUES (1,'bridge','local'),(2,'macvlan','local'),(3,'host','local'),(4,'null','local');
/*!40000 ALTER TABLE `swarm_ui_drivernetworks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_drivervolumes`
--

DROP TABLE IF EXISTS `swarm_ui_drivervolumes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_drivervolumes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `driver` varchar(32) NOT NULL,
  `scope` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_drivervolumes`
--

LOCK TABLES `swarm_ui_drivervolumes` WRITE;
/*!40000 ALTER TABLE `swarm_ui_drivervolumes` DISABLE KEYS */;
INSERT INTO `swarm_ui_drivervolumes` VALUES (1,'local','local');
/*!40000 ALTER TABLE `swarm_ui_drivervolumes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_logsloginlogout`
--

DROP TABLE IF EXISTS `swarm_ui_logsloginlogout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_logsloginlogout` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `action` varchar(32) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_logsloginlogout`
--

LOCK TABLES `swarm_ui_logsloginlogout` WRITE;
/*!40000 ALTER TABLE `swarm_ui_logsloginlogout` DISABLE KEYS */;
INSERT INTO `swarm_ui_logsloginlogout` VALUES (1,'dongvt','login','2016-11-01 22:00:50'),(2,'dongvt','login','2016-11-01 22:35:22'),(3,'dongvt','login','2016-11-02 03:05:02'),(4,'dongvt','logout','2016-11-02 03:22:06'),(5,'dongvt','login','2016-11-02 03:22:20'),(6,'dongvt','logout','2016-11-02 11:35:14'),(7,'dongvt','login','2016-11-02 11:35:21'),(8,'dongvt','logout','2016-11-02 11:36:21'),(9,'dongvt','login','2016-11-02 11:36:30'),(10,'dongvt','logout','2016-11-02 16:14:05'),(11,'mrneodiablo','login','2016-11-02 16:14:11'),(12,'mrneodiablo','logout','2016-11-02 16:19:48'),(13,'dongvt','login','2016-11-02 16:19:55'),(14,'dongvt','logout','2016-11-02 16:20:04'),(15,'mrneodiablo','login','2016-11-02 16:20:13'),(16,'mrneodiablo','logout','2016-11-02 16:20:47'),(17,'dongvt','login','2016-11-02 16:20:53'),(18,'dongvt','logout','2016-11-04 03:55:03'),(19,'mrneodiablo','login','2016-11-04 03:57:19'),(20,'mrneodiablo','logout','2016-11-04 03:57:27'),(21,'dongvt','login','2016-11-04 03:58:45'),(22,'dongvt','login','2016-11-04 07:11:23'),(23,'dongvt','logout','2016-11-04 07:51:02'),(24,'dongvt','login','2016-11-04 07:51:12'),(25,'dongvt','logout','2016-11-04 08:51:09'),(26,'dongvt','login','2016-11-04 08:52:06'),(27,'dongvt','logout','2016-11-04 17:40:59'),(28,'nanght','login','2016-11-04 17:41:05'),(29,'nanght','logout','2016-11-04 17:43:12'),(30,'dongvt','login','2016-11-04 17:43:20'),(31,'dongvt','logout','2016-11-04 17:43:29'),(32,'nanght','login','2016-11-04 17:43:34'),(33,'nanght','logout','2016-11-04 17:44:43'),(34,'dongvt','login','2016-11-04 17:44:54'),(35,'dongvt','logout','2016-11-04 18:22:45'),(36,'dongvt','login','2016-11-04 18:23:19'),(37,'dongvt','logout','2016-11-05 03:41:22'),(38,'dongvt','login','2016-11-05 03:44:54'),(39,'dongvt','logout','2016-11-07 00:01:56'),(40,'nanght','login','2016-11-07 00:02:01'),(41,'nanght','logout','2016-11-07 07:39:36'),(42,'dongvt','login','2016-11-07 07:39:42'),(43,'dongvt','logout','2016-11-08 06:35:54'),(44,'dongvt','login','2016-11-08 06:36:05'),(45,'dongvt','logout','2016-11-08 10:38:50'),(46,'dongvt','login','2016-11-08 10:38:56'),(47,'dongvt','logout','2016-11-08 12:07:27'),(48,'dongvt','login','2016-11-08 12:07:35'),(49,'dongvt','logout','2016-11-08 15:54:14'),(50,'nanght','login','2016-11-08 15:54:22'),(51,'nanght','logout','2016-11-09 01:30:20'),(52,'dongvt','login','2016-11-09 01:30:30'),(53,'dongvt','logout','2016-11-09 01:44:19'),(54,'dongvt','login','2016-11-09 03:11:26'),(55,'dongvt','logout','2016-11-09 08:50:55'),(56,'dongvt','login','2016-11-09 08:51:04'),(57,'dongvt','login','2016-11-10 07:39:54'),(58,'dongvt','login','2016-11-10 09:20:00'),(59,'dongvt','login','2016-11-10 17:46:15'),(60,'dongvt','login','2016-11-13 16:46:19'),(61,'dongvt','login','2016-11-13 19:07:12'),(62,'dongvt','login','2016-11-14 03:00:40'),(63,'dongvt','login','2016-11-14 03:02:18'),(64,'dongvt','login','2016-11-14 03:11:51'),(65,'dongvt','logout','2016-11-14 03:49:05'),(66,'mrneodiablo','login','2016-11-14 03:49:11'),(67,'mrneodiablo','logout','2016-11-14 03:51:26'),(68,'dongvt','login','2016-11-14 03:51:33'),(69,'dongvt','logout','2016-11-14 09:16:21'),(70,'dongvt','login','2016-11-14 09:16:35');
/*!40000 ALTER TABLE `swarm_ui_logsloginlogout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_logsuser`
--

DROP TABLE IF EXISTS `swarm_ui_logsuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_logsuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `action` varchar(32) NOT NULL,
  `feature` varchar(32) NOT NULL,
  `message` varchar(256) NOT NULL,
  `container` varchar(32) NOT NULL,
  `node` varchar(32) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=172 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_logsuser`
--

LOCK TABLES `swarm_ui_logsuser` WRITE;
/*!40000 ALTER TABLE `swarm_ui_logsuser` DISABLE KEYS */;
INSERT INTO `swarm_ui_logsuser` VALUES (1,'dongvt','stop','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 08:05:07'),(2,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 08:05:12'),(3,'dongvt','rename','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\', \'container_data\': {\'name\': u\'GS2-test15-hihi\'}}','','','2016-11-02 08:05:23'),(4,'dongvt','pause','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 08:05:40'),(5,'dongvt','unpause','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 08:05:43'),(6,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:39:23'),(7,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:39:26'),(8,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:39:45'),(9,'dongvt','stop','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:40:40'),(10,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:40:55'),(11,'dongvt','pause','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:40:57'),(12,'dongvt','unpause','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:41:05'),(13,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:41:10'),(14,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:41:13'),(15,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:41:17'),(16,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:41:25'),(17,'dongvt','pause','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:41:26'),(18,'dongvt','unpause','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:41:28'),(19,'dongvt','monitor','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:42:59'),(20,'dongvt','monitor','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:04'),(21,'dongvt','monitor','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:09'),(22,'dongvt','monitor','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:14'),(23,'dongvt','monitor','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:19'),(24,'dongvt','monitor','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:24'),(25,'dongvt','restart','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:35'),(26,'dongvt','kill','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:44'),(27,'dongvt','start','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:43:49'),(28,'dongvt','rename','container','{\'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\', \'container_data\': {\'name\': u\'GS2-ahihi\'}}','','','2016-11-02 09:44:09'),(29,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'440cfdaaf74f1169b5e33cf56f1b244369fac3c5411e0a64ef3b50e19838cb17\'}','','','2016-11-02 09:44:22'),(30,'dongvt','remove','node','{\'node_ip\': u\'10.40.89.103:2375\'}','','','2016-11-02 11:27:51'),(31,'dongvt','create','user','{\'lastname\': \'\', \'user\': u\'mrneodiablo\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'1\', \'7\', \'9\', \'8\']}','','','2016-11-02 16:13:44'),(32,'mrneodiablo','monitor','container','{\'container_id\': u\'cc6e527156605d0f984d12a56871ea5ce04dc6f3bdaf1158ff7c9f1e62a97a78\'}','','','2016-11-02 16:18:16'),(33,'mrneodiablo','monitor','container','{\'container_id\': u\'cc6e527156605d0f984d12a56871ea5ce04dc6f3bdaf1158ff7c9f1e62a97a78\'}','','','2016-11-02 16:18:21'),(34,'mrneodiablo','monitor','container','{\'container_id\': u\'cc6e527156605d0f984d12a56871ea5ce04dc6f3bdaf1158ff7c9f1e62a97a78\'}','','','2016-11-02 16:18:26'),(35,'mrneodiablo','monitor','container','{\'container_id\': u\'cc6e527156605d0f984d12a56871ea5ce04dc6f3bdaf1158ff7c9f1e62a97a78\'}','','','2016-11-02 16:18:31'),(36,'mrneodiablo','monitor','container','{\'container_id\': u\'cc6e527156605d0f984d12a56871ea5ce04dc6f3bdaf1158ff7c9f1e62a97a78\'}','','','2016-11-02 16:18:36'),(37,'dongvt','update','user','{\'lastname\': \'\', \'user\': u\'mrneodiablo\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'7\', \'9\', \'8\']}','','','2016-11-02 16:20:03'),(38,'dongvt','disconnect','network','{\'network_id\': u\'653c28ec2cc79fb4d40aa22cb5a3eaf51ba41bee7dee890f0e6b93204667142e\', \'container_id\': u\'84728073a88bba28a85855bafdbb040bdff74c5b8c4c3171856caa083e77157d\', \'force\': u\'1\'}','','','2016-11-03 08:05:15'),(39,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': u\'1\'}','','','2016-11-03 09:58:06'),(40,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.33\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-03 09:59:17'),(41,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.33\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\'}','','','2016-11-03 10:05:35'),(42,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\'}','','','2016-11-03 10:05:50'),(43,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': u\'1\'}','','','2016-11-04 04:49:12'),(44,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.33\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 04:49:23'),(45,'dongvt','disconnect','network','{\'network_id\': u\'39bc4c853917aa2646c628b7ba4875d9fe0fe8567125434bf3a358131dfab19f\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 17:26:26'),(46,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 17:29:22'),(47,'dongvt','disconnect','network','{\'network_id\': u\'39bc4c853917aa2646c628b7ba4875d9fe0fe8567125434bf3a358131dfab19f\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 17:29:49'),(48,'dongvt','disconnect','network','{\'network_id\': u\'d0c4b9b4ce7e8063b798af905366055389997512b05ab1f17cef3a4e7e9dcc95\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\', \'force\': 1}','','','2016-11-04 17:31:17'),(49,'dongvt','connect','network','{\'network_id\': u\'d0c4b9b4ce7e8063b798af905366055389997512b05ab1f17cef3a4e7e9dcc95\', \'ip\': u\'10.40.2.33\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\'}','','','2016-11-04 17:34:57'),(50,'dongvt','connect','network','{\'network_id\': u\'d438c57c50601063f1cacb4c64949d8bafc1324bae9375ee73e2e764b6eec682\', \'ip\': u\'49.213.109.23\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\'}','','','2016-11-04 17:35:47'),(51,'dongvt','create','user','{\'lastname\': \'\', \'user\': u\'nanght\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'7\', \'9\', \'8\']}','','','2016-11-04 17:40:19'),(52,'dongvt','update','user','{\'lastname\': \'\', \'user\': u\'nanght\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'14\', \'7\', \'9\', \'8\']}','','','2016-11-04 17:40:30'),(53,'dongvt','update','user','{\'lastname\': \'\', \'user\': u\'nanght\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'14\', \'7\', \'9\', \'8\']}','','','2016-11-04 17:40:52'),(54,'dongvt','update','user','{\'lastname\': \'\', \'user\': u\'nanght\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'14\', \'1\', \'7\', \'9\', \'8\']}','','','2016-11-04 17:43:27'),(55,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:37:25'),(56,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:37:32'),(57,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:37:47'),(58,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:38:02'),(59,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 22:41:04'),(60,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:42:17'),(61,'dongvt','connect','network','{\'network_id\': u\'309b89df7dc07d230541bd9929edef1724df47b5f5d2ef3ff62f3471db76fbaa\', \'ip\': u\'10.40.23.26\', \'container_id\': u\'84728073a88bba28a85855bafdbb040bdff74c5b8c4c3171856caa083e77157d\'}','','','2016-11-04 22:46:35'),(62,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 22:48:19'),(63,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:48:47'),(64,'dongvt','disconnect','network','{\'network_id\': u\'309b89df7dc07d230541bd9929edef1724df47b5f5d2ef3ff62f3471db76fbaa\', \'container_id\': u\'84728073a88bba28a85855bafdbb040bdff74c5b8c4c3171856caa083e77157d\', \'force\': 1}','','','2016-11-04 22:51:55'),(65,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 22:51:59'),(66,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 22:52:03'),(67,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:52:27'),(68,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 22:54:33'),(69,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:55:02'),(70,'dongvt','disconnect','network','{\'network_id\': u\'d0c4b9b4ce7e8063b798af905366055389997512b05ab1f17cef3a4e7e9dcc95\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\', \'force\': 1}','','','2016-11-04 22:55:51'),(71,'dongvt','connect','network','{\'network_id\': u\'d0c4b9b4ce7e8063b798af905366055389997512b05ab1f17cef3a4e7e9dcc95\', \'ip\': u\'10.40.2.33\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\'}','','','2016-11-04 22:56:17'),(72,'dongvt','disconnect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\', \'force\': 1}','','','2016-11-04 22:57:07'),(73,'dongvt','connect','network','{\'network_id\': u\'5ce17b75c073b527f81fec06f87b69e1bd17ed9d827270e009aafaeb90ff7c97\', \'ip\': u\'10.40.2.32\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-04 22:58:49'),(74,'dongvt','disconnect','network','{\'network_id\': u\'d438c57c50601063f1cacb4c64949d8bafc1324bae9375ee73e2e764b6eec682\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\', \'force\': 1}','','','2016-11-05 02:21:28'),(75,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'1a84d282b184cd252ab60901ec6a5e33e4e443e2d0269d672b62e51c43db0559\'}','','','2016-11-06 17:47:44'),(76,'dongvt','connect','network','{\'network_id\': u\'a3fecbde0d64e54cc5134b3147412f728a8959eecd643664ab1b0198b518ba5f\', \'ip\': u\'49.213.119.202\', \'container_id\': u\'7280c52d88ef3054b3215f93d958af4fea919eb03d5d9621262b9d4228769372\'}','','','2016-11-06 18:28:27'),(77,'dongvt','connect','network','{\'network_id\': u\'a3fecbde0d64e54cc5134b3147412f728a8959eecd643664ab1b0198b518ba5f\', \'ip\': u\'49.213.119.203\', \'container_id\': u\'da88dec9c4598c5fff5236009bebf450d226b268b080174d94dd54b4c94cc103\'}','','','2016-11-06 18:29:31'),(78,'dongvt','connect','network','{\'network_id\': u\'a3fecbde0d64e54cc5134b3147412f728a8959eecd643664ab1b0198b518ba5f\', \'ip\': u\'49.213.119.204\', \'container_id\': u\'8f6c78b85b05f5249f072021e15136645bcd0e4d20cef70c21bcbc372333930d\'}','','','2016-11-06 18:29:39'),(79,'dongvt','remove_image','registry','{\'name_registry\': u\'caas-c6-base\', \'tag_registry\': u\'v1\'}','','','2016-11-06 23:18:43'),(80,'dongvt','remove_image','registry','{\'name_registry\': u\'caas-c6-base\', \'tag_registry\': u\'v1\'}','','','2016-11-06 23:18:45'),(81,'dongvt','create','container','{\'container_data\': {\'Cmd\': [], \'Volumes\': {}, \'Hostname\': \'\', \'StdinOnce\': True, \'AttachStdin\': True, \'Env\': [], \'OpenStdin\': True, \'Tty\': True, \'Domainname\': \'\', \'Image\': \'\', \'Labels\': {}, \'HostConfig\': {\'NetworkMode\': u\'MTO_DOCKER_HTCPG1_Server113/host\',','','','2016-11-10 09:57:38'),(82,'dongvt','create','container','{\'container_data\': {\'Cmd\': [], \'Volumes\': {}, \'Hostname\': \'\', \'StdinOnce\': True, \'AttachStdin\': True, \'Env\': [], \'OpenStdin\': True, \'Tty\': True, \'Domainname\': \'\', \'Image\': \'\', \'Labels\': {}, \'HostConfig\': {\'NetworkMode\': u\'MTO_DOCKER_HTCPG1_Server113/vlan89','','','2016-11-10 18:34:51'),(83,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'12802c812485b966d7ae31b0efc9ab52e587012fda995d586e54ae6d710ba763\'}','','','2016-11-10 19:47:15'),(84,'dongvt','stop','container','{\'container_id\': u\'5edec28989dbb6598d73ef1be885ea6cc6f4a0659d5ada773f3f8e35e68d862a\'}','','','2016-11-10 19:47:54'),(85,'dongvt','start','container','{\'container_id\': u\'5edec28989dbb6598d73ef1be885ea6cc6f4a0659d5ada773f3f8e35e68d862a\'}','','','2016-11-10 19:48:03'),(86,'dongvt','pause','container','{\'container_id\': u\'5edec28989dbb6598d73ef1be885ea6cc6f4a0659d5ada773f3f8e35e68d862a\'}','','','2016-11-10 19:48:11'),(87,'dongvt','unpause','container','{\'container_id\': u\'5edec28989dbb6598d73ef1be885ea6cc6f4a0659d5ada773f3f8e35e68d862a\'}','','','2016-11-10 19:48:14'),(88,'dongvt','add','product','{\'vlan_gateway\': u\'10.40.89.1\', \'vlan_subnet\': u\'10.40.89.0/24\', \'vlan_name\': u\'vlan489\', \'product_status\': u\'1\', \'vlan_scope\': u\'1\', \'product_name\': u\'dockergs2\'}','','','2016-11-11 03:14:08'),(89,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'12342\', \'StdinOnce\':','','','2016-11-11 08:27:21'),(90,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'123456\', \'StdinOnce\'','','','2016-11-11 08:28:28'),(91,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'1111\', \'StdinOnce\': ','','','2016-11-11 08:30:46'),(92,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'yyyyyyyyyyy\', \'Stdin','','','2016-11-11 08:34:57'),(93,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'wwwwwwwwww\', \'StdinO','','','2016-11-11 08:48:24'),(94,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'ssssssssss\', \'StdinO','','','2016-11-11 08:52:24'),(95,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'qqqqqq\', \'StdinOnce\'','','','2016-11-11 09:01:37'),(96,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'222222222\', \'StdinOn','','','2016-11-11 09:21:04'),(97,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'4444444\', \'StdinOnce','','','2016-11-11 09:24:17'),(98,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'3333333\', \'StdinOnce','','','2016-11-11 09:30:26'),(99,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'eeeeeeee\', \'StdinOnc','','','2016-11-11 09:32:30'),(100,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'wwwwww\', \'StdinOnce\'','','','2016-11-11 09:35:32'),(101,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'4333333333333\', \'Std','','','2016-11-11 09:44:41'),(102,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'wwwwwwwwwwww\', \'Stdi','','','2016-11-11 09:48:58'),(103,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/caas-c6-base:latest\', \'Hostname\': u\'3333333333\', \'StdinO','','','2016-11-11 09:50:58'),(104,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/caas-c6-base:latest\', \'Hostname\': u\'3333333322\', \'StdinO','','','2016-11-11 09:51:42'),(105,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'eeeeeee\', \'StdinOnce','','','2016-11-11 09:52:55'),(106,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'32323233\', \'StdinOnc','','','2016-11-11 10:04:56'),(107,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'undefined:undefined/dongvt/centos:6.8.1\', \'Hostname\': u\'wwwwww\', \'StdinOnce\'','','','2016-11-11 10:07:26'),(108,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'dddddddd\', \'StdinOnce\'','','','2016-11-11 10:11:43'),(109,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'33333333\', \'StdinOnce\'','','','2016-11-11 10:12:50'),(110,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'444444\', \'StdinOnce\': ','','','2016-11-11 10:13:28'),(111,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'323223123\', \'StdinOnce','','','2016-11-11 10:19:21'),(112,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'weeeeeeeee\', \'StdinOnc','','','2016-11-11 10:20:35'),(113,'dongvt','stop','container','{\'container_id\': u\'5edec28989dbb6598d73ef1be885ea6cc6f4a0659d5ada773f3f8e35e68d862a\'}','','','2016-11-11 10:23:01'),(114,'dongvt','start','container','{\'container_id\': u\'5edec28989dbb6598d73ef1be885ea6cc6f4a0659d5ada773f3f8e35e68d862a\'}','','','2016-11-11 10:25:24'),(115,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'mds-ddssdfd\', \'StdinOn','','','2016-11-11 10:26:02'),(116,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'dddddddd\', \'StdinOnce\'','','','2016-11-11 10:29:26'),(117,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'1212212\', \'StdinOnce\':','','','2016-11-11 10:59:15'),(118,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'wwwwwwww\', \'StdinOnce\'','','','2016-11-11 11:04:40'),(119,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'dddddddddd\', \'StdinOnc','','','2016-11-11 11:06:58'),(120,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'wwwwwwww\', \'StdinOnce\'','','','2016-11-11 11:08:47'),(121,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'wqeqwewqe\', \'StdinOnce','','','2016-11-11 11:11:13'),(122,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'333333333333\', \'StdinO','','','2016-11-11 11:16:47'),(123,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'44444\', \'StdinOnce\': T','','','2016-11-11 11:28:11'),(124,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'333333\', \'StdinOnce\': ','','','2016-11-11 11:37:10'),(125,'dongvt','start','container','{\'container_id\': u\'a04ac9a56a800f45389a229a28c0b7637fdf454186af4572b029fa5e00c81d63\'}','','','2016-11-11 11:44:09'),(126,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'5555555555\', \'StdinOnc','','','2016-11-11 11:47:23'),(127,'dongvt','start','container','{\'container_id\': u\'3e29113355d7b11c791e9fcbbf873e3203c06a9aa2c1b20dbbd526a96f28b246\'}','','','2016-11-11 11:47:40'),(128,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'22222\', \'StdinOnce\': T','','','2016-11-11 11:50:03'),(129,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'111111\', \'StdinOnce\': ','','','2016-11-11 11:51:01'),(130,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'ddddd\', \'StdinOnce\': T','','','2016-11-11 11:52:29'),(131,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'www222\', \'StdinOnce\': ','','','2016-11-13 16:51:08'),(132,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'5ff90348dec801490d49de4e424d9f673a997d65406b433bf069b65c9f9fb475\'}','','','2016-11-13 17:11:09'),(133,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'709708b43fed126b0ae5c1d2cea30a252bd490e9fec2261a74215bf9ed3a4f34\'}','','','2016-11-13 17:11:55'),(134,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'a8f35fa445bb632b8de8c6374e33d829539511a99ba6b55d26bfefc27be1587a\'}','','','2016-11-13 17:12:30'),(135,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'ed4d97a30bdecc2fe05ededf773fdd717b5f5eb1f8c8b3529cff99900aede77b\'}','','','2016-11-13 17:12:40'),(136,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'4444444\', \'StdinOnce\':','','','2016-11-13 17:15:09'),(137,'dongvt','rename','container','{\'container_id\': u\'d035ce6c990ff821cc22a911a389ed106dc2c2a8f59a0f1df5a17b34379b6324\', \'container_data\': {\'name\': u\'test1\'}}','','','2016-11-13 17:27:20'),(138,'dongvt','pause','container','{\'container_id\': u\'d035ce6c990ff821cc22a911a389ed106dc2c2a8f59a0f1df5a17b34379b6324\'}','','','2016-11-13 17:27:26'),(139,'dongvt','restart','container','{\'container_id\': u\'d035ce6c990ff821cc22a911a389ed106dc2c2a8f59a0f1df5a17b34379b6324\'}','','','2016-11-13 17:27:29'),(140,'dongvt','unpause','container','{\'container_id\': u\'d035ce6c990ff821cc22a911a389ed106dc2c2a8f59a0f1df5a17b34379b6324\'}','','','2016-11-13 17:27:31'),(141,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'d035ce6c990ff821cc22a911a389ed106dc2c2a8f59a0f1df5a17b34379b6324\'}','','','2016-11-13 17:27:57'),(142,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'e2eb8ccf67d8ae19d11602ba5d956544a173c33a3a47f82cd8694f93e5c00716\'}','','','2016-11-13 17:28:04'),(143,'dongvt','restart','container','{\'container_id\': u\'27444cde08dc6532c6e92c9d1484db0554c670af892e806bb4b7dbaa4091806c\'}','','','2016-11-13 17:28:20'),(144,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'27444cde08dc6532c6e92c9d1484db0554c670af892e806bb4b7dbaa4091806c\'}','','','2016-11-13 17:28:31'),(145,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'c8e7d4809a502b1a0f59c70d7aac726c777d280ec746334012a97f1da7e3d80b\'}','','','2016-11-13 17:30:18'),(146,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'3e29113355d7b11c791e9fcbbf873e3203c06a9aa2c1b20dbbd526a96f28b246\'}','','','2016-11-13 17:30:38'),(147,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'87f7c542002daa4f1ac3c949f05ae30a93c17d1198a08372d51b98aaf0c9cb62\'}','','','2016-11-13 17:30:45'),(148,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'84728073a88bba28a85855bafdbb040bdff74c5b8c4c3171856caa083e77157d\'}','','','2016-11-13 17:31:39'),(149,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'0203cfcd740bde41eb101dc3ae5297462fd2a914e965db4b8edabdb46c2d7966\'}','','','2016-11-13 17:31:46'),(150,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'2e7da2fec51261144956b7dd27a4a47844823970b09a7d6296f68213d58a5162\'}','','','2016-11-13 17:31:53'),(151,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'5edec28989dbb6598d73ef1be885ea6cc6f4a0659d5ada773f3f8e35e68d862a\'}','','','2016-11-13 17:32:02'),(152,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'a04ac9a56a800f45389a229a28c0b7637fdf454186af4572b029fa5e00c81d63\'}','','','2016-11-13 17:32:10'),(153,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'wwwwwwww\', \'StdinOnce\'','','','2016-11-13 17:34:18'),(154,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'123213123\', \'StdinOnce','','','2016-11-13 17:35:27'),(155,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'vothanhdong_1003\', \'St','','','2016-11-13 17:37:26'),(156,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'vothanhdong-1993\', \'St','','','2016-11-13 17:39:04'),(157,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'vothanhdong_1003\', \'St','','','2016-11-13 18:45:21'),(158,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'abcd\', \'StdinOnce\': Fa','','','2016-11-13 18:45:55'),(159,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'222222\', \'StdinOnce\': ','','','2016-11-13 18:51:43'),(160,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'6652fa183b8df4273ec73054c330b237e2b49f34c9733e6631e70f7e88abd357\'}','','','2016-11-13 18:54:01'),(161,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'fe791dc0f78b2b7bb7742a0f7558a52bdb8a6dc172aeba3339a4962c76e5e238\'}','','','2016-11-13 18:54:08'),(162,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'a9a6274b7d9fd352fae3e3501aae693b7ffa559fee49680de4ac82fa43a47418\'}','','','2016-11-13 18:54:14'),(163,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'22222222222\', \'StdinOn','','','2016-11-14 02:18:36'),(164,'dongvt','remove','container','{\'remove_volume\': u\'1\', \'remove_force\': u\'1\', \'container_id\': u\'de92bb38788cfc32b26edf41e18dec713f2b5c66ae99fb1296099dcfd4b76f3b\'}','','','2016-11-14 02:18:53'),(165,'dongvt','update','user','{\'lastname\': \'\', \'user\': u\'mrneodiablo\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'12\', \'7\', \'9\', \'8\']}','','','2016-11-14 03:39:52'),(166,'dongvt','remove','user','{\'user\': u\'nanght\'}','','','2016-11-14 03:41:20'),(167,'dongvt','create','user','{\'lastname\': \'\', \'user\': u\'222\', \'firstname\': \'\', \'permission\': [\'11\', \'10\', \'13\', \'1\', \'7\', \'9\', \'8\']}','','','2016-11-14 03:42:48'),(168,'dongvt','create','container','{\'container_data\': {\'Tty\': True, \'Labels\': {\'mto.product.name\': u\'dockergs2\', \'com.docker.swarm.constraints\': u\'[\"ip==10.40.89.113\"]\'}, \'Volumes\': {}, \'Domainname\': \'\', \'Image\': u\'10.60.93.253:5002/dongvt/centos:6.8.1\', \'Hostname\': u\'dongvt-test\', \'StdinOn','','','2016-11-14 07:39:09'),(169,'dongvt','remove','user','{\'user\': u\'mrneodiablo\'}','','','2016-11-14 09:16:43'),(170,'dongvt','remove','user','{\'user\': u\'222\'}','','','2016-11-14 09:16:45'),(171,'dongvt','create','user','{\'lastname\': u\'Super\', \'user\': u\'admin\', \'firstname\': u\'Admin\', \'permission\': [\'11\', \'10\', \'13\', \'12\', \'1\', \'3\', \'2\', \'5\', \'4\', \'7\', \'6\', \'9\', \'8\']}','','','2016-11-14 09:17:07');
/*!40000 ALTER TABLE `swarm_ui_logsuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_permissions`
--

DROP TABLE IF EXISTS `swarm_ui_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_permissions` (
  `name` varchar(32) NOT NULL,
  `code` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_permissions`
--

LOCK TABLES `swarm_ui_permissions` WRITE;
/*!40000 ALTER TABLE `swarm_ui_permissions` DISABLE KEYS */;
INSERT INTO `swarm_ui_permissions` VALUES ('admin',1),('container_admin',2),('node_admin',3),('volume_admin',4),('network_admin',5),('image_admin',6),('container_read_only',7),('node_read_only',8),('volume_read_only',9),('network_read_only',10),('image_read_only',11),('user_admin',12),('user_read_only',13),('registry_read_only',14),('registry_admin',15),('product_read_only',16),('product_admin',17);
/*!40000 ALTER TABLE `swarm_ui_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_product`
--

DROP TABLE IF EXISTS `swarm_ui_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `container` int(11) NOT NULL,
  `gateway` varchar(32) NOT NULL,
  `subnet` varchar(32) NOT NULL,
  `vlan` varchar(32) NOT NULL,
  `scope` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_product`
--

LOCK TABLES `swarm_ui_product` WRITE;
/*!40000 ALTER TABLE `swarm_ui_product` DISABLE KEYS */;
INSERT INTO `swarm_ui_product` VALUES (1,'dmhmp1',1,0,'10.40.2.1','10.40.2.0/24','vlan402','1'),(2,'dmhmp1',1,0,'49.213.108.1','49.213.108.0/26','vlan220','2'),(3,'htcpg1',1,0,'10.40.23.1','10.40.23.0/24','vlan423','1'),(4,'htcpg1',1,0,'49.213.119.193','49.213.119.192/27','vlan226','2'),(8,'dockergs2',1,0,'10.40.89.1','10.40.89.0/24','vlan489','1');
/*!40000 ALTER TABLE `swarm_ui_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_registry`
--

DROP TABLE IF EXISTS `swarm_ui_registry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_registry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `ip` varchar(32) NOT NULL,
  `port` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_registry`
--

LOCK TABLES `swarm_ui_registry` WRITE;
/*!40000 ALTER TABLE `swarm_ui_registry` DISABLE KEYS */;
INSERT INTO `swarm_ui_registry` VALUES (4,'Gs2_registry','10.60.93.253',5002);
/*!40000 ALTER TABLE `swarm_ui_registry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swarm_ui_userpermissions`
--

DROP TABLE IF EXISTS `swarm_ui_userpermissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swarm_ui_userpermissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_code_id` int(11) NOT NULL,
  `username_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `swarm_ui_userpermiss_permission_code_id_b7a6c43a_fk_swarm_ui_` (`permission_code_id`),
  KEY `swarm_ui_userpermissions_username_id_a08c4344_fk_auth_user_id` (`username_id`),
  CONSTRAINT `swarm_ui_userpermissions_username_id_a08c4344_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `swarm_ui_userpermiss_permission_code_id_b7a6c43a_fk_swarm_ui_` FOREIGN KEY (`permission_code_id`) REFERENCES `swarm_ui_permissions` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swarm_ui_userpermissions`
--

LOCK TABLES `swarm_ui_userpermissions` WRITE;
/*!40000 ALTER TABLE `swarm_ui_userpermissions` DISABLE KEYS */;
INSERT INTO `swarm_ui_userpermissions` VALUES (5,8,1),(6,1,1),(62,11,5),(63,10,5),(64,13,5),(65,12,5),(66,1,5),(67,3,5),(68,2,5),(69,5,5),(70,4,5),(71,7,5),(72,6,5),(73,9,5),(74,8,5);
/*!40000 ALTER TABLE `swarm_ui_userpermissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'dockerui'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-14 16:21:29
