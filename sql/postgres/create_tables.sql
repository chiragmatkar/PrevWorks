
-- Table: public.injury

-- DROP TABLE IF EXISTS public.injury;
CREATE TABLE covidSurvey (
  surveyId SERIAL PRIMARY KEY NOT NULL ,
  hadCovid bit(1) NOT NULL,
  healthcare bit(1) NOT NULL,
  fever bit(1) NOT NULL,
  loss bit(1) NOT NULL,
  pain bit(1) NOT NULL,
  cough bit(1) NOT NULL,
  breath bit(1) NOT NULL,
  conjunctivitis bit(1) NOT NULL,
  gi bit(1) NOT NULL,
  userId int NOT NULL,
  date timestamp NOT NULL
)


CREATE TABLE IF NOT EXISTS public.injury
(
    injuryId SERIAL PRIMARY KEY NOT NULL ,
    dateoccured character varying(45) COLLATE pg_catalog."default",
    injurytype character varying(45) COLLATE pg_catalog."default" NOT NULL,
    at_work boolean NOT NULL,
    reported boolean NOT NULL,
    supervisor character varying(45) COLLATE pg_catalog."default",
    supervisor_email character varying(100) COLLATE pg_catalog."default",
    supervisor_relation character varying(45) COLLATE pg_catalog."default",
    supervisor_phone character varying(45) COLLATE pg_catalog."default",
    supervisor_date character varying(45) COLLATE pg_catalog."default",
    reported_before boolean,
    reported_date character varying(45) COLLATE pg_catalog."default",
    description character varying(1500) COLLATE pg_catalog."default",
    userid integer NOT NULL,
    companyid integer,
    date timestamp without time zone DEFAULT CURRENT_TIMESTAMP
)

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