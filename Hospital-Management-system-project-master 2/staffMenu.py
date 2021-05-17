import mysql.connector
from staffGetPatientProfile import getPatientProfile
from modifyPhysicianProfile import modifyPhysicianProfile
from addPhysicianProfile import addPhysicianProfile
from staffViewInsurance import staffViewInsurance
from staffAddBill import addBill

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def staff_menu():
    print("""
    Welcome Staff! \n
    Selection menu: \n
    1 - Add Physician Profile
    2 - Modify Physician Profile
    3 - Bill
    4 - View Patient Insurance
    5 - View Patient Profile
    6 - Log out
     """)
    choice = int(input("Menu option: "))

    if choice == 1:
        addPhysicianProfile()
    elif choice == 2:
        modifyPhysicianProfile()
    elif choice == 3:
        addBill()
    elif choice == 4:
        staffViewInsurance()
    elif choice == 5:
        getPatientProfile()
    elif choice == 6:
        quit()
    else:
        print("Not an option. Quitting application!")
        quit()
