DROP TABLE IF EXISTS bodyParts;

CREATE TABLE bodyParts (
  bodyId SERIAl PRIMARY KEY,
  name varchar(45) NOT NULL
)

DROP TABLE IF EXISTS feature;
CREATE TABLE feature (
  featureId SERIAl PRIMARY KEY,
  name varchar(100) NOT NULL
)
INSERT INTO feature VALUES (2,'age'),(3,'salary');

CREATE TABLE user2company (
  userId int NOT NULL,
  companyId int NOT NULL,
  position varchar(100) DEFAULT NULL,
  user2companyId  SERIAL PRIMARY KEY
)
CREATE TABLE occupations (
  occupationId SERIAl PRIMARY KEY,
  occupationName varchar(200) NOT NULL
)
CREATE TABLE occupationDaysProbabilities (
  probId SERIAl PRIMARY KEY,
  probability float NOT NULL,
  avgDays int NOT NULL,
  occupationId int NOT NULL
)

CREATE TABLE occupationBodyProbability (
  probId  SERIAl PRIMARY KEY,
  occupationId int NOT NULL,
  probability float NOT NULL,
  bodyId int NOT NULL
)


CREATE TABLE occupationAgeProbabilities (
  probabilityId SERIAl PRIMARY KEY,
  ageLower int NOT NULL,
  ageUpper int NOT NULL,
  probability float NOT NULL,
  occupationId int NOT NULL
)


CREATE TABLE feature2user (
  userId int NOT NULL,
  featureId int NOT NULL,
  value varchar(100)  NOT NULL,
  mappingId SERIAl PRIMARY KEY
)


CREATE TABLE companyToIndustry (
  companyName varchar(100) NOT NULL PRIMARY KEY,
  industry varchar(400) NOT NULL,
  classification varchar(580) NOT NULL
)