CREATE DATABASE `HealthyFarm` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

CREATE TABLE `Animal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `arrived` date NOT NULL,
  `left` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Building` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `zone` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_animal` int(11) NOT NULL,
  `temperature` int(11) NOT NULL,
  `heart_rate` int(11) NOT NULL,
  `lat` int(11) NOT NULL,
  `long` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `Data_FK` FOREIGN KEY (`id`) REFERENCES `Animal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `isadmin` tinyint(1) NOT NULL,
  `role` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_UN` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
