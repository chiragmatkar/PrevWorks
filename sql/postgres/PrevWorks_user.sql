DROP TABLE IF EXISTS users;
/* SQLINES DEMO *** cs_client     = @@character_set_client */;
/* SQLINES DEMO *** er_set_client = utf8mb4 */;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE SEQUENCE user_seq;

CREATE TABLE users (
  userId int NOT NULL DEFAULT NEXTVAL ('user_seq'),
  email varchar(100) NOT NULL,
  fname varchar(45) NOT NULL,
  lname varchar(45) NOT NULL,
  password varchar(102) NOT NULL,
  age int DEFAULT NULL,
  occupationId int DEFAULT NULL,
  PRIMARY KEY (userId)
);

ALTER SEQUENCE user_seq RESTART WITH 12651;
/* SQLINES DEMO *** er_set_client = @saved_cs_client */;

CREATE INDEX occupationId_idx ON users (occupationId);

INSERT INTO users VALUES
(1,'rjsteele@usc.edu','Robert','Steele','pbkdf2:sha256:260000$fOuhmx3wWMwMFv7x$8439668687e87e84c2209e46b274fed316d3fb426d9c3bbc3aa7c5acf23018bb',0,0),
(2,'email@email.com','Robert','Steele','pbkdf2:sha256:260000$X4WM14OLG7dSUd9f$f5aa4f62b647422d68a12dae2b06049be959d1db57bc800ff23182a2a3cc09cf',0,0),
(3,'test@gmail.com','test','test','pbkdf2:sha256:260000$y6YudjNT8tZyjUkY$3b30aa96c4932a717ac89e4d5d20c0422d2b05e3af7fee71828f7de60eaa4aee',0,0),
(4,'test2@gmail.com','test','test','pbkdf2:sha256:260000$PCqmoZQeUOsCSTMD$7e1b21820aaba73cc3fa724121dba8ef2ef7dca9271f6001cf312bf0e542f7ee',0,0),
(5,'test@yaho.com','test','test','pbkdf2:sha256:260000$KxZdPyqPuryP3CMA$f4ca1f3f0c4b6779ad1125cea9c8efce6e4aff7cd66e4a25698a379be2055592',0,0),
(6,'test@g.com','test','test','pbkdf2:sha256:260000$XWPvrN0kf33qMt4A$2cee55f4f386cb1d293b0f60e97499dc1770a0a1884f7b4ccdf82820ff025efc',0,0)
