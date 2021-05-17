CREATE DEFINER=`root`@`localhost` PROCEDURE `logincheckusernameDoctor`(
	IN Doctor_UserId VARCHAR(45), 
    OUT outDoctorUserID VARCHAR(45))
BEGIN
	SELECT Password1 INTO outDoctorUserID FROM doctor WHERE UserID = Doctor_UserID;
END



CREATE DEFINER=`root`@`localhost` PROCEDURE `logincheckusernamePatient`(
	IN Patient_UserId VARCHAR(45), 
    OUT outPatientUserID VARCHAR(45)
)
BEGIN
	SELECT Password1 INTO outPatientUserID FROM Patient WHERE UserID = Patient_UserID;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `logincheckusernameStaff`(
	IN Staff_UserId VARCHAR (45),
    OUT outStaffUserID VARCHAR (45)
    )
BEGIN
	SELECT Password1 INTO outStaffUserID FROM Staff WHERE UserID = Staff_UserID;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `PatientModifyProfile2`(IN intendedUserID VARCHAR(45),OUT output VARCHAR(255))
BEGIN
	SELECT * INTO output FROM Patient WHERE UserID = intendedUserID ;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `patientProfileAddress`(
	IN patient_address VARCHAR (45),
    OUT out_patient_address VARCHAR (45)
    )
BEGIN
	SELECT Address INTO out_patient_address FROM Patient WHERE UserID = patient_address;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `patientProfileDOB`(
	IN patient_DOB VARCHAR (45),
    OUT out_patient_DOB VARCHAR (45)
    )
BEGIN
	SELECT DOB INTO out_patient_DOB FROM Patient WHERE UserID = patient_DOB;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `patientProfileEmail`(
	IN patient_Email VARCHAR (45),
    OUT out_patient_Email VARCHAR (45)
)
BEGIN
	SELECT Email INTO out_patient_Email FROM Patient WHERE UserID = patient_Email;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `patientProfileFirstname`(
	IN patient_firstname VARCHAR (45),
	OUT out_patient_firstname VARCHAR (45)
    )
BEGIN
	SELECT FirstName INTO out_patient_firstname FROM Patient WHERE UserID = patient_firstname;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `patientProfileLastname`(
	IN patient_lastname VARCHAR (45),
    OUT out_patient_lastname VARCHAR (45)
    )
BEGIN
	SELECT LastName INTO out_patient_lastname FROM Patient WHERE UserID = patient_lastname;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `patientProfileUserID`(
	IN patient_UserID VARCHAR (45),
    OUT out_patient_UserID VARCHAR (45))
BEGIN
	SELECT UserID INTO out_patient_UserID FROM Patient WHERE UserID = patient_UserID;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `patientUpdateAddress`(
	IN Patient_updateAddress VARCHAR(45), 
    OUT outPatientUpdateAddress VARCHAR(45))
BEGIN
	UPDATE Patient SET Address = outPatientUpdateAddress WHERE UserID = Patient_updateAddress;
END

CREATE DEFINER=`root`@`localhost` PROCEDURE `patientviewinsuranceExpiration`(
IN patient_insuranceExpir VARCHAR (45),
	OUT out_patient_insurancExpir VARCHAR (45)
    )
BEGIN
	SELECT expirationDate INTO out_patient_insurancExpir FROM insurance WHERE patientuserID = patient_insuranceExpir;
END

CREATE DEFINER=`root`@`localhost` PROCEDURE `patientviewinsurancename`(
IN patient_insurancename VARCHAR (45),
	OUT out_patient_insurancename VARCHAR (45)
    )
BEGIN
	SELECT insuranceName INTO out_patient_insurancename FROM insurance WHERE patientuserID = patient_insurancename;
END

CREATE DEFINER=`root`@`localhost` PROCEDURE `getpatientbill`(
	IN Patient_bill VARCHAR(45), 
    OUT outPatientbill VARCHAR(45)
)
BEGIN
	SELECT Bill INTO outPatientbill FROM Patient WHERE UserID = Patient_bill;
END
