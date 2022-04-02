DROP TABLE IF EXISTS Laureates, NobelPrizes, Affiliations;

CREATE TABLE Laureates(id int PRIMARY KEY, givenorgName varchar(60), familyName varchar(30), gender varchar(6), birthfoundedDate date, city varchar(40), country varchar(40));
CREATE TABLE NobelPrizes(id int, awardYear int(4), category varchar(30), sortOrder int(1), FLAGN int PRIMARY KEY);
CREATE TABLE Affiliations(id int, name varchar(60), city varchar(40), country varchar(40), FLAGN int, FLAGA int PRIMARY KEY);

LOAD DATA LOCAL INFILE 'Laureates.del' INTO TABLE Laureates FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
LOAD DATA LOCAL INFILE 'NobelPrizes.del' INTO TABLE NobelPrizes FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
LOAD DATA LOCAL INFILE 'Affiliations.del' INTO TABLE Affiliations FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
