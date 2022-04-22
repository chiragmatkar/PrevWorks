
DROP TABLE IF EXISTS company;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8mb4 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE SEQUENCE company_seq;

CREATE TABLE company (
  companyId int NOT NULL DEFAULT NEXTVAL ('company_seq'),
  companyName varchar(100) NOT NULL,
  streetAddr varchar(45) DEFAULT NULL,
  city varchar(45) DEFAULT NULL,
  country varchar(45) DEFAULT NULL,
  zip varchar(45) DEFAULT NULL,
  phone varchar(45) DEFAULT NULL,
  password varchar(102) NOT NULL,
  loginName varchar(100) NOT NULL,
  PRIMARY KEY (companyId)
)   ;

ALTER SEQUENCE company_seq RESTART WITH 5;
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;

--
-- SQLINES DEMO *** table `company`
--

/* SQLINES DEMO ***  `company` DISABLE KEYS */;
INSERT INTO company VALUES
(1,'asdf',NULL,NULL,NULL,NULL,NULL,'pbkdf2:sha256:260000$aY2r1bObFvowr3YV$0acc276c583868fc549d9a93663cdbf2fe61f317f1a980340198e5bb24bed15b','user@gmail.com')