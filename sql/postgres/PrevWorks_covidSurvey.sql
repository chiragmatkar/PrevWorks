-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE SEQUENCE covidSurvey_seq;

CREATE TABLE covidSurvey (
  surveyId int NOT NULL DEFAULT NEXTVAL ('covidSurvey_seq'),
  hadCovid boolean NOT NULL,
  healthcare boolean NOT NULL,
  fever boolean NOT NULL,
  loss boolean NOT NULL,
  pain boolean NOT NULL,
  cough boolean NOT NULL,
  breath boolean NOT NULL,
  conjunctivitis boolean NOT NULL,
  gi boolean NOT NULL,
  userId int NOT NULL,
  date timestamp(0) NOT NULL,
  PRIMARY KEY (surveyId)
)