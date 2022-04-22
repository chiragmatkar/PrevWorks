DROP TABLE IF EXISTS injury;
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE SEQUENCE injury_seq;

CREATE TABLE injury (
  injuryId int NOT NULL DEFAULT NEXTVAL ('injury_seq'),
  dateOccured timestamp(0) NOT NULL,
  injuryType varchar(45) NOT NULL,
  at_work boolean NOT NULL,
  reported boolean NOT NULL,
  supervisor varchar(45) NOT NULL,
  supervisor_email varchar(100) NOT NULL,
  supervisor_relation varchar(45) NOT NULL,
  supervisor_phone varchar(45) NOT NULL,
  supervisor_date timestamp(0) NOT NULL,
  reported_before boolean NOT NULL,
  reported_date timestamp(0) NOT NULL,
  description varchar(1500)  NOT NULL,
  userId int NOT NULL,
  companyId int DEFAULT NULL,
  PRIMARY KEY (injuryId)
)