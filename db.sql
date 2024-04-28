/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - aidietconsultant2
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`aidietconsultant2` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `aidietconsultant2`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add batch',7,'add_batch'),(26,'Can change batch',7,'change_batch'),(27,'Can delete batch',7,'delete_batch'),(28,'Can view batch',7,'view_batch'),(29,'Can add login',8,'add_login'),(30,'Can change login',8,'change_login'),(31,'Can delete login',8,'delete_login'),(32,'Can view login',8,'view_login'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add trainer',10,'add_trainer'),(38,'Can change trainer',10,'change_trainer'),(39,'Can delete trainer',10,'delete_trainer'),(40,'Can view trainer',10,'view_trainer'),(41,'Can add request',11,'add_request'),(42,'Can change request',11,'change_request'),(43,'Can delete request',11,'delete_request'),(44,'Can view request',11,'view_request'),(45,'Can add feedback',12,'add_feedback'),(46,'Can change feedback',12,'change_feedback'),(47,'Can delete feedback',12,'delete_feedback'),(48,'Can view feedback',12,'view_feedback'),(49,'Can add assign',13,'add_assign'),(50,'Can change assign',13,'change_assign'),(51,'Can delete assign',13,'delete_assign'),(52,'Can view assign',13,'view_assign'),(53,'Can add workout',14,'add_workout'),(54,'Can change workout',14,'change_workout'),(55,'Can delete workout',14,'delete_workout'),(56,'Can view workout',14,'view_workout'),(57,'Can add tips',15,'add_tips'),(58,'Can change tips',15,'change_tips'),(59,'Can delete tips',15,'delete_tips'),(60,'Can view tips',15,'view_tips'),(61,'Can add health',16,'add_health'),(62,'Can change health',16,'change_health'),(63,'Can delete health',16,'delete_health'),(64,'Can view health',16,'view_health'),(65,'Can add diet',17,'add_diet'),(66,'Can change diet',17,'change_diet'),(67,'Can delete diet',17,'delete_diet'),(68,'Can view diet',17,'view_diet'),(69,'Can add chat',18,'add_chat'),(70,'Can change chat',18,'change_chat'),(71,'Can delete chat',18,'delete_chat'),(72,'Can view chat',18,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(13,'myapp','assign'),(7,'myapp','batch'),(18,'myapp','chat'),(17,'myapp','diet'),(12,'myapp','feedback'),(16,'myapp','health'),(8,'myapp','login'),(11,'myapp','request'),(15,'myapp','tips'),(10,'myapp','trainer'),(9,'myapp','user'),(14,'myapp','workout'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-11-14 15:49:03.529849'),(2,'auth','0001_initial','2023-11-14 15:49:04.806506'),(3,'admin','0001_initial','2023-11-14 15:49:05.061318'),(4,'admin','0002_logentry_remove_auto_add','2023-11-14 15:49:05.077745'),(5,'admin','0003_logentry_add_action_flag_choices','2023-11-14 15:49:05.094024'),(6,'contenttypes','0002_remove_content_type_name','2023-11-14 15:49:05.259599'),(7,'auth','0002_alter_permission_name_max_length','2023-11-14 15:49:05.334867'),(8,'auth','0003_alter_user_email_max_length','2023-11-14 15:49:05.419618'),(9,'auth','0004_alter_user_username_opts','2023-11-14 15:49:05.435197'),(10,'auth','0005_alter_user_last_login_null','2023-11-14 15:49:05.526104'),(11,'auth','0006_require_contenttypes_0002','2023-11-14 15:49:05.533091'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-14 15:49:05.548033'),(13,'auth','0008_alter_user_username_max_length','2023-11-14 15:49:05.623830'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-14 15:49:05.708309'),(15,'auth','0010_alter_group_name_max_length','2023-11-14 15:49:05.801163'),(16,'auth','0011_update_proxy_permissions','2023-11-14 15:49:05.823692'),(17,'auth','0012_alter_user_first_name_max_length','2023-11-14 15:49:05.907580'),(18,'myapp','0001_initial','2023-11-14 15:49:06.913692'),(19,'myapp','0002_auto_20230912_1453','2023-11-14 15:49:07.108726'),(20,'myapp','0003_alter_trainer_name','2023-11-14 15:49:07.191355'),(21,'myapp','0004_auto_20230918_1255','2023-11-14 15:49:08.232900'),(22,'myapp','0005_alter_tips_date','2023-11-14 15:49:08.320546'),(23,'myapp','0006_alter_workout_description','2023-11-14 15:49:08.410811'),(24,'myapp','0007_alter_workout_date','2023-11-14 15:49:08.488815'),(25,'myapp','0008_auto_20231101_1209','2023-11-14 15:49:08.878540'),(26,'myapp','0009_health_targetweight','2023-11-14 15:49:08.988642'),(27,'myapp','0010_alter_health_medical','2023-11-14 15:49:09.091990'),(28,'myapp','0011_alter_health_bmi','2023-11-14 15:49:09.177963'),(29,'myapp','0012_batch_batch_title','2023-11-14 15:49:09.276042'),(30,'myapp','0013_tips_user','2023-11-14 15:49:09.394416'),(31,'myapp','0014_auto_20231106_1549','2023-11-14 15:49:09.724290'),(32,'myapp','0015_workout_user','2023-11-14 15:49:09.844771'),(33,'sessions','0001_initial','2023-11-14 15:49:09.945290');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('5fawbhh3ps7xa9t7ckm096g00jw9ef7k','eyJsaWQiOjgsInVpZCI6IjQifQ:1rR45o:btpO3Im-AtJO8BMgiBjazWlMiJg87wc3FkPoVYcfrmM','2024-02-03 05:40:32.464772'),('7ulfquk868wm4q1vy4ej4iygyevqvt61','eyJsaWQiOjIsInVpZCI6IjEifQ:1rKukh:9eiDZvANDybp-Nhh15ABCoGNy4xx7i5-1ExsiGdLmNg','2024-01-17 06:29:19.368108'),('bt3ed14r59rty5rrrujmrh7mxr0rdqa9','eyJsaWQiOjIsInVpZCI6IjEifQ:1rCC6E:gU6BVmCQrObRRFvGBwmZxTJrHwOFEInxfvJf-q7DVuQ','2023-12-24 05:11:30.468851'),('rke465g6294zlg0t1kk2m5ho9tk9n0xd','eyJsaWQiOjIyLCJ1aWQiOiIxIn0:1rR4jg:xcK93ClenzAx-rpQmjfiqd3kxoJUBbh0Pz4UyPd6GZE','2024-02-03 06:21:44.001072'),('wjihd4zbwu8qw9jb3573kdzemxad6ib6','eyJsaWQiOjgsImJpZCI6IjEiLCJ1aWQiOiIxNiJ9:1rR5YJ:qAlEbM9Ca-GseLv93eYxunjOXpq-f6jDSuRAjTxyMmE','2024-02-03 07:14:03.889294');

/*Table structure for table `myapp_assign` */

DROP TABLE IF EXISTS `myapp_assign`;

CREATE TABLE `myapp_assign` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `time` varchar(20) NOT NULL,
  `REQUEST_id` bigint(20) NOT NULL,
  `TRAINER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_assign_REQUEST_id_37178d29_fk_myapp_request_id` (`REQUEST_id`),
  KEY `myapp_assign_TRAINER_id_9fac0067_fk_myapp_trainer_id` (`TRAINER_id`),
  CONSTRAINT `myapp_assign_REQUEST_id_37178d29_fk_myapp_request_id` FOREIGN KEY (`REQUEST_id`) REFERENCES `myapp_request` (`id`),
  CONSTRAINT `myapp_assign_TRAINER_id_9fac0067_fk_myapp_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `myapp_trainer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_assign` */

insert  into `myapp_assign`(`id`,`time`,`REQUEST_id`,`TRAINER_id`) values (1,'14/11/2023-21:55:28',1,1),(4,'14/11/2023-21:56:18',4,2),(7,'14/11/2023-21:57:33',7,2),(8,'15/11/2023-19:57:27',8,3),(9,'03/01/2024-16:22:18',9,2),(15,'06/01/2024-11:40:33',16,1),(16,'07/01/2024-11:30:33',18,1),(17,'07/01/2024-12:40:53',19,2),(18,'07/01/2024-19:17:41',20,1),(19,'20/01/2024-10:56:08',21,1),(20,'20/01/2024-10:58:51',22,1),(21,'20/01/2024-12:24:04',23,2);

/*Table structure for table `myapp_batch` */

DROP TABLE IF EXISTS `myapp_batch`;

CREATE TABLE `myapp_batch` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Batch_Capacity` varchar(20) NOT NULL,
  `Time_from` varchar(20) NOT NULL,
  `Time_to` varchar(20) NOT NULL,
  `Batch_title` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_batch` */

insert  into `myapp_batch`(`id`,`Batch_Capacity`,`Time_from`,`Time_to`,`Batch_title`) values (1,'50','09:00','12:00','Morning Batch'),(2,'30','02:00','04:00','Afternoon Batch'),(3,'40','05:00','07:00','Evening Batch'),(4,'10','13:45','16:45','Special Batch'),(5,'10','14:18','17:17','Special Batch 1'),(6,'10','10:00','20:00','Special Batch 2'),(7,'10','10:00','20:00','Special Batch 3');

/*Table structure for table `myapp_chat` */

DROP TABLE IF EXISTS `myapp_chat`;

CREATE TABLE `myapp_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `usertype` varchar(10) NOT NULL,
  `chat` varchar(100) NOT NULL,
  `TRAINER_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_TRAINER_id_eac4a259_fk_myapp_trainer_id` (`TRAINER_id`),
  KEY `myapp_chat_USER_id_df623826_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_chat_TRAINER_id_eac4a259_fk_myapp_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `myapp_trainer` (`id`),
  CONSTRAINT `myapp_chat_USER_id_df623826_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_chat` */

insert  into `myapp_chat`(`id`,`date`,`usertype`,`chat`,`TRAINER_id`,`USER_id`) values (1,'','','hi',1,1),(2,'','','hlooo',1,1),(3,'2024-01-03','trainer','ok',1,1),(4,'2024-01-03','user','kkooo',2,1),(5,'2024-01-03','user','hi',1,1),(6,'2024-01-03','trainer','ok',1,1),(7,'2024-01-03','trainer','ooooooooooooo',2,1),(8,'2024-01-03','trainer','iiiiiiii',2,1),(9,'2024-01-03','trainer','hu',2,1),(10,'2024-01-03','user','hi',1,1),(11,'2024-01-03','trainer','hi',1,1),(12,'2024-01-03','trainer','sdgew',1,1),(13,'2024-01-03','trainer','hi',1,1),(15,'2024-01-03','user','hrr',1,1),(16,'2024-01-03','user','',1,1),(17,'2024-01-03','user','',1,1),(18,'2024-01-03','user','hi',1,1),(22,'2024-01-04','user','ok',1,1),(23,'2024-01-04','user','',1,1),(24,'2024-01-04','trainer','hi',2,10),(25,'2024-01-04','trainer','hi',2,7),(26,'2024-01-05','trainer','hi',1,1),(27,'2024-01-05','trainer','yr',1,1),(28,'2024-01-05','user','hi',1,1),(30,'2024-01-05','user','ok',1,1),(31,'2024-01-07','trainer','hi',3,8),(32,'2024-01-07','trainer','hi angelo',2,4),(33,'2024-01-07','trainer','hi',1,19),(34,'2024-01-20','trainer','hi',2,4),(35,'2024-01-20','user','yes',1,1),(36,'2024-01-20','user','helloo',1,1),(37,'2024-01-20','user','hlo',1,1),(38,'2024-01-20','user','',1,1),(39,'2024-01-20','user','hello',1,1),(40,'2024-01-20','user','hello',1,1),(41,'2024-01-20','user','hiii',1,1),(42,'2024-01-20','user','hlll',1,1),(43,'2024-01-20','user','gggg',1,1),(44,'2024-01-20','user','kjh',1,1),(45,'2024-01-20','user','hello',2,4),(46,'2024-01-20','trainer','pay your fees on date',2,4),(47,'2024-01-20','user','helo',2,4),(48,'2024-01-20','trainer','hi',1,16),(49,'2024-01-20','user','heelo',1,16);

/*Table structure for table `myapp_diet` */

DROP TABLE IF EXISTS `myapp_diet`;

CREATE TABLE `myapp_diet` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `TRAINER_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  `description` varchar(500) NOT NULL,
  `title` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_diet_TRAINER_id_583c9578_fk_myapp_trainer_id` (`TRAINER_id`),
  KEY `myapp_diet_USER_id_5501b500_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_diet_TRAINER_id_583c9578_fk_myapp_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `myapp_trainer` (`id`),
  CONSTRAINT `myapp_diet_USER_id_5501b500_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_diet` */

insert  into `myapp_diet`(`id`,`date`,`TRAINER_id`,`USER_id`,`description`,`title`) values (1,'04/01/2024-22:46:02',1,1,'Chapathi 2 nos,rice\r\n','Morning'),(2,'14/11/2023-22:27:50',1,1,'Rice 250g','Afternoon'),(3,'14/11/2023-22:28:06',1,1,'chapathi 2 nos','Night'),(7,'15/11/2023-21:57:04',1,1,'ergeg','night'),(8,'28/11/2023-10:39:00',1,1,'breakfast','8am'),(9,'28/11/2023-10:39:40',1,1,'lunch','1pm'),(10,'28/11/2023-10:39:59',1,1,'dinner','8pm');

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `time` varchar(20) NOT NULL,
  `feedback` varchar(500) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`time`,`feedback`,`USER_id`) values (1,'09/12/2023-14:39:30','bad',7),(2,'09/12/2023-14:40:04','bad',7),(3,'10/12/2023-10:10:52','hi',1);

/*Table structure for table `myapp_health` */

DROP TABLE IF EXISTS `myapp_health`;

CREATE TABLE `myapp_health` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `height` varchar(3) NOT NULL,
  `weight` varchar(3) NOT NULL,
  `activelevel` varchar(20) NOT NULL,
  `medical` varchar(200) NOT NULL,
  `bmi` varchar(10) NOT NULL,
  `foodtype` varchar(10) NOT NULL,
  `target` varchar(10) NOT NULL,
  `allergies` varchar(500) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  `estimatedtime` varchar(10) NOT NULL,
  `weeklytarget` varchar(10) NOT NULL,
  `targetweight` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_health_USER_id_fc8947ef_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_health_USER_id_fc8947ef_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_health` */

insert  into `myapp_health`(`id`,`height`,`weight`,`activelevel`,`medical`,`bmi`,`foodtype`,`target`,`allergies`,`USER_id`,`estimatedtime`,`weeklytarget`,`targetweight`) values (1,'166','65','Moderately Active','None','23.59','Non-Veg','lose','none',1,'10.00 week','0.50','60'),(2,'166','62','Moderately Active','None','23.5','Non-Veg','lose','none',1,'4.00 week','0.50','60'),(5,'176','53','Lightly Active','None','17.11','Non-Veg','gain','none',4,'14.00 week','0.50','60'),(8,'176','55','Lightly Active','None','17.76','Non-Veg','gain','none',7,'6.67 weeks','0.75','60'),(9,'155','50','Lightly Active','None','20.81','Non-Veg','gain','none',8,'6.00 weeks','0.50','53'),(10,'155','50','Lightly Active','None','20.81','Non-Veg','gain','none',8,'12.00 week','0.25','53'),(11,'176','53','Lightly Active','None','17.11','Non-Veg','gain','none',4,'','Choose',''),(12,'167','70','Moderately Active','None','25.1','Non-Veg','lose','',1,'20.00 week','0.50','60'),(13,'167','67','Lightly Active','None','24.02','Non-Veg','lose','none',1,'9.33 weeks','0.75','60'),(14,'166','70','Little or NO Activit','None','25.4','Non-Veg','lose','',1,'40.00 week','0.25','60'),(16,'166','65','Lightly Active','None','23.59','Non-Veg','gain','',1,'10.00 week','0.50','70'),(17,'166','60','Lightly Active','None','21.77','Non-Veg','gain','',1,'7.00 weeks','1.00','67'),(18,'175','60','Lightly Active','None','19.59','Non-Veg','gain','',19,'20.00 week','0.50','70'),(19,'175','60','Little or NO Activit','None','19.59','Non-Veg','gain','',20,'13.33 week','0.75','70'),(20,'175','60','Little or NO Activit','None','19.59','Non-Veg','gain','',17,'20.00 week','0.50','70'),(21,'175','50','Lightly Active','None','16.33','Non-Veg','gain','',21,'40.00 week','0.50','70');

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'farheeniqbal10467@gmail.com','4127','trainer'),(3,'hrishinandan007@gmail.com','9252','trainer'),(4,'roopa@gmail.com','2269','trainer'),(5,'abhinandbhaskar89@gmail.com','abhi','user'),(8,'angelo@gmail.com','angelo','user'),(11,'dipin@gmail.com','dipin','user'),(12,'abhinaanand@gmail.com','abhina','user'),(14,'aathira@gmail.com','aathira','user'),(16,'farheeniqbal223344@gmail.com','2345','trainer'),(18,'farshid@gmail.com','farshid','user'),(19,'anik@gmail.com','anik','user'),(22,'benjuz@gmail.com','benju','user'),(23,'vishnu@gmail.com','vishnu','user'),(24,'githin@gmail.com','githin','user'),(25,'meghan@gmail.com','meghan','user'),(26,'alex@gmail.com','alex','user'),(27,'albert@gmail.com','albert','user');

/*Table structure for table `myapp_request` */

DROP TABLE IF EXISTS `myapp_request`;

CREATE TABLE `myapp_request` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `time` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  `BATCH_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_request_USER_id_8675c54c_fk_myapp_user_id` (`USER_id`),
  KEY `myapp_request_BATCH_id_09625526_fk_myapp_batch_id` (`BATCH_id`),
  CONSTRAINT `myapp_request_BATCH_id_09625526_fk_myapp_batch_id` FOREIGN KEY (`BATCH_id`) REFERENCES `myapp_batch` (`id`),
  CONSTRAINT `myapp_request_USER_id_8675c54c_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_request` */

insert  into `myapp_request`(`id`,`time`,`status`,`USER_id`,`BATCH_id`) values (1,'14/11/2023-21:36:57','approved',1,1),(4,'14/11/2023-21:50:14','Left',4,2),(7,'14/11/2023-21:57:10','approved',7,1),(8,'15/11/2023-19:56:53','approved',8,3),(9,'03/01/2024-16:21:03','approved',10,1),(16,'06/01/2024-11:39:46','approved',12,1),(17,'06/01/2024-11:46:31','rejected',13,1),(18,'07/01/2024-11:27:26','approved',16,1),(19,'07/01/2024-12:29:16','Left',17,3),(20,'07/01/2024-19:15:27','approved',19,3),(21,'20/01/2024-10:55:43','Left',20,1),(22,'20/01/2024-10:58:15','approved',17,1),(23,'20/01/2024-12:23:02','Left',21,2),(24,'20/01/2024-12:31:49','pending',4,3),(25,'20/01/2024-12:32:43','pending',21,4);

/*Table structure for table `myapp_tips` */

DROP TABLE IF EXISTS `myapp_tips`;

CREATE TABLE `myapp_tips` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `title` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  `TRAINER_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_tips_TRAINER_id_4a9deaa3_fk_myapp_trainer_id` (`TRAINER_id`),
  KEY `myapp_tips_USER_id_71b3d746_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_tips_TRAINER_id_4a9deaa3_fk_myapp_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `myapp_trainer` (`id`),
  CONSTRAINT `myapp_tips_USER_id_71b3d746_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_tips` */

insert  into `myapp_tips`(`id`,`date`,`title`,`description`,`TRAINER_id`,`USER_id`) values (1,'04/01/2024-22:32:55','Drink water','Drink 6 classes of water a day ',1,1),(3,'04/01/2024-22:46:33','tip','tip',1,1),(4,'15/11/2023-21:25:11','adminA','kmk',1,1),(5,'15/11/2023-21:26:07','jhjh','kjk',1,1),(6,'15/11/2023-21:29:58','hjj','kjk',1,1),(7,'15/11/2023-21:30:30','joj','kk',1,1),(8,'15/11/2023-21:30:59','mnk','mbm',1,1),(9,'15/11/2023-21:40:19','abhishek ','wd',1,1),(10,'15/11/2023-21:44:44','adminA','sd',1,1),(11,'15/11/2023-21:46:04','hi','kh',1,1);

/*Table structure for table `myapp_trainer` */

DROP TABLE IF EXISTS `myapp_trainer`;

CREATE TABLE `myapp_trainer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `age` varchar(20) NOT NULL,
  `sex` varchar(6) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `experience` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobilenumber` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_trainer_LOGIN_id_b7caa7db_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_trainer_LOGIN_id_b7caa7db_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_trainer` */

insert  into `myapp_trainer`(`id`,`name`,`place`,`pin`,`post`,`age`,`sex`,`qualification`,`experience`,`LOGIN_id`,`email`,`mobilenumber`) values (1,'Muhammad Farheen Iqbal','Kanhangad','671315','Kanhangad','21','Male','Bsc.Computer Science','3 Years',2,'farheeniqbal10467@gmail.com','7994110813'),(2,'Hrishinandan','Mylatty','671315','Kanhangad','20','Male','Plus Two','2 Years',3,'hrishinandan007@gmail.com','8547620138'),(3,'roopa','panathur','787878','panathur','20','Female','SSLC','1 year',4,'roopa@gmail.com','8848993973');

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `age` varchar(6) NOT NULL,
  `sex` varchar(6) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobilenumber` varchar(20) NOT NULL,
  `occupation` varchar(20) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`place`,`pin`,`post`,`age`,`sex`,`email`,`mobilenumber`,`occupation`,`LOGIN_id`) values (1,'Abhinand Bhaskar M','Nellithara','671322','Mavungal','21','Male','abhinandbhaskar89@gmail.com','8848993973','none',5),(4,'Angelo','parappa','676767','parappa','19','Male','angelo@gmail.com','8787897979','none',8),(7,'Dipin','Bedakam','676766','bedakam','20','Male','dipin@gmail.com','6876986969','none',11),(8,'Abhina Anand','manikoth','671316','manikoth','20','Female','abhinaanand@gmail.com','8648538649','none',12),(10,'Aathira','kanhangad','671311','kanhangad','25','Male','aathira@gmail.com','9898989898','Teacher',14),(12,'Farshid','Kanhangad','671311','Kanhanagd','15','Male','farshid@gmail.com','9898989898','None',18),(13,'Aniketh','chully','768699','chully','20','Male','anik@gmail.com','8768969680','footballer',19),(16,'Benjamin','Peroor','671533','peroor','20','Male','benjuz@gmail.com','5635387832','footballer',22),(17,'Vishnu','Madikai','671533','peroor','20','Male','vishnu@gmail.com','7685734567','Mason',23),(18,'Githin','Thachangad','671533','Thachangad','20','Male','githin@gmail.com','6787878787','Merchant navy',24),(19,'Meghanath','Thachangad','671533','Thachangad','20','Male','meghan@gmail.com','6787878787','doctor',25),(20,'Alex','Thachangad','671533','Thachangad','20','Male','alex@gmail.com','6787878787','doctor',26),(21,'Albert','Rajapuram','671533','Rajapuram','20','Male','albert@gmail.com','6787878787','student',27);

/*Table structure for table `myapp_workout` */

DROP TABLE IF EXISTS `myapp_workout`;

CREATE TABLE `myapp_workout` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `title` varchar(20) NOT NULL,
  `description` varchar(200) NOT NULL,
  `video` varchar(500) NOT NULL,
  `TRAINER_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_workout_TRAINER_id_deffb721_fk_myapp_trainer_id` (`TRAINER_id`),
  KEY `myapp_workout_USER_id_cf660a3a_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_workout_TRAINER_id_deffb721_fk_myapp_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `myapp_trainer` (`id`),
  CONSTRAINT `myapp_workout_USER_id_cf660a3a_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_workout` */

insert  into `myapp_workout`(`id`,`date`,`title`,`description`,`video`,`TRAINER_id`,`USER_id`) values (1,'14/11/2023-22:32:39','pushup','a excise to build muscles','/static/videos/14112023-223239.mp4',1,1),(3,'15/11/2023-21:07:00','work','out','/static/videos/15112023-210700.mp4',1,1),(4,'15/11/2023-21:08:06','work','outsdf','/static/videos/15112023-210806.mp4',1,1),(5,'15/11/2023-21:10:26','work','outsdfs','/static/videos/15112023-211026.mp4',1,1),(6,'15/11/2023-21:10:58','sd','sd','/static/videos/15112023-211058.mp4',1,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
