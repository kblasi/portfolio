import mysql.connector
from patientProfile import getPatientProfile
import login
from physiciangetpatientprofile import physicianGetPatientProfile
from admitpatient import admit_patient
from prescribemeds import prescribe_meds
from enterlabresults import enter_lab_results

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="Project"
)

def physician_menu():
    print("""
    Welcome Physician! \n
    Selection menu: \n
    1 - View patient profile
    2 - Admit patient
    3 - Prescribe Medication
    4 - Enter test results
     """)
    choice = int(input("Menu option: "))

    if choice == 1:
        print("---Get patient profile---")
        username1 = int(input("Enter Patient UserID: "))
        global username1
        physicianGetPatientProfile()
    elif choice == 2:
        print("---Admit patient---")
        admit_patient()
    elif choice == 3:
        print("---Prescribe Medication---")
        prescribe_meds()
    elif choice == 4:
        print("---Enter test results---") 
        enter_lab_results()
    
    else:
        print("Not an option. Quitting application!")
        quit
