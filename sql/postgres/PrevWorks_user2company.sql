

DROP TABLE IF EXISTS `user2company`;
CREATE TABLE `user2company` (
  `userId` int NOT NULL,
  `companyId` int NOT NULL,
  `position` varchar(100) DEFAULT NULL,
  `user2companyId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`user2companyId`)
)




