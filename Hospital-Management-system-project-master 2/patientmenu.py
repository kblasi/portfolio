import mysql.connector
from patientProfile import getPatientProfile
from patientviewinsurance import patientViewInsurance
from patientScheduleApp import schedApp
from patientpaybill import paybill

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def patient_menu():
    print("""
    Welcome Patient! \n
    Selection menu: \n
    1 - My profile
    2 - Schedule appointment
    3 - My insurance information
    4 - Pay bill

    5 - Sign out
     """)
    choice = int(input("Menu option: "))

    if choice == 1:
        getPatientProfile()
    elif choice == 2:
        schedApp()
    elif choice == 3:
        patientViewInsurance()
    elif choice == 4:
        paybill()
    elif choice == 5:
        print('Signing out...')
        quit
    else:
        print("Not an option. Quitting application!")
        quit
