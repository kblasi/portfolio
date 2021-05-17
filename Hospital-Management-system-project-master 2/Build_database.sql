CREATE TABLE `doctor` (
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password1` varchar(45) NOT NULL,
  `UserID` int(15) NOT NULL,
  `Speciality` varchar(45) NOT NULL,
  PRIMARY KEY (`UserID`)
);

INSERT INTO doctor (FirstName, LastName, Email, Password1, UserID, Speciality)
VALUES ('Meredith','Grey','MeredithGrey@gmail.com','apple888','2001','General Surgeon');

INSERT INTO doctor (FirstName, LastName, Email, Password1, UserID, Speciality)
VALUES ('Mark','Sloan','MarkSloan@gmail.com','fish000!','2005','Plastic Surgery');

INSERT INTO doctor (FirstName, LastName, Email, Password1, UserID, Speciality)
VALUES ('Derek','Shepherd','DerekShepherd@gmail.com','brain11!','2004','Neurology');

INSERT INTO doctor (FirstName, LastName, Email, Password1, UserID, Speciality)
VALUES ('Christina','Yang','ChristinaYang@gmail.com','chicken111!','2002','Cardiology');

INSERT INTO doctor (FirstName, LastName, Email, Password1, UserID, Speciality)
VALUES ('Alex','Karev','AlexKarev@gmail.com','book999$','2003','Pediatrics');


CREATE TABLE `patient` (
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password1` varchar(45) NOT NULL,
  `UserID` int(15) NOT NULL,
  `DOB` date NOT NULL,
  PRIMARY KEY (`UserID`)
);

INSERT INTO patient (FirstName, LastName, Address, Email, Password1, UserID, DOB)
VALUES ('John','Smith','123 Main St','JohnSmith@yahoo.com','password1!','1001','1990-12-09');

INSERT INTO patient (FirstName, LastName, Address, Email, Password1, UserID, DOB)
VALUES ('Alec','Bobby','321 S Clinton St','AlecBobby@gmail.com','dog123!','1002','1999-05-10');

INSERT INTO patient (FirstName, LastName, Address, Email, Password1, UserID, DOB)
VALUES ('Kyle','Bobby','333 N Forest St','KyleBobby@gmail.com','cookie321!','1003','1970-02-01');

INSERT INTO patient (FirstName, LastName, Address, Email, Password1, UserID, DOB)
VALUES ('Jenifer','Fox','454 E Burlington St','JeniferFox@aol.com','dolphin432#','1004','1993-12-12');

INSERT INTO patient (FirstName, LastName, Address, Email, Password1, UserID, DOB)
VALUES ('Elvis','Johns','847 W Austin Ave','ElvisJohns@yahoo.com','dog847!','1005','2000-10-01');


CREATE TABLE `staff` (
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password1` varchar(45) NOT NULL,
  `UserID` varchar(45) NOT NULL,
  PRIMARY KEY (`UserID`)
);

INSERT INTO staff (FirstName, LastName, Email, Password1, UserID)
VALUES ('Erin','Grant','ErinGrant@gmail.com','dolphin22!','3001');

INSERT INTO staff (FirstName, LastName, Email, Password1, UserID)
VALUES ('Casey','Duffy','CaseyDuffy@gmail.com','boat221#','3002');

INSERT INTO staff (FirstName, LastName, Email, Password1, UserID)
VALUES ('Frank','Ocean','FrankOcean@gmail.com','turtles11!','3003'):

ALTER TABLE patient
ADD COLUMN Bill int(8) AFTER DOB;

UPDATE patient SET Bill = '0' WHERE UserID = '1001';
UPDATE patient SET Bill = '0' WHERE UserID = '1002';
UPDATE patient SET Bill = '0' WHERE UserID = '1003';
UPDATE patient SET Bill = '0' WHERE UserID = '1004';
UPDATE patient SET Bill = '0' WHERE UserID = '1005';

CREATE TABLE `insurance` (
  `patientuserID` int(11) NOT NULL,
  `insuranceName` varchar(45) NOT NULL,
  `expirationDate` varchar(45) NOT NULL,
  PRIMARY KEY (`patientuserID`)
);

INSERT INTO insurance VALUES('1001', 'Blue Cross Blue Shield' , '2020-1-1' );

INSERT INTO insurance VALUES('1002', 'United Health Care', '2021-12-30' );

INSERT INTO insurance VALUES('1003', 'Cigna', '2020-6-1' );

INSERT INTO insurance VALUES('1004', 'Blue Cross Blue Shield', '2019-21-30' );

INSERT INTO insurance VALUES('1005', 'Blue Cross Blue Shield', '2024-1-1');
