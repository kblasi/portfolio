import mysql.connector
import getpass
from patientmenu import patient_menu

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def login():

    print("""
    Select your role:
    1 - Patient
    2 - Physician
    3 - Staff
     """)
    choice = int(input("Role number: "))
    if choice == (1) or choice == (2) or choice == (3):
        global login_user
        username = int(input("Enter UserID: "))
        global username
        if choice == 1:
            passwordCounter = 0
            mycursor = mydb.cursor()
            args = [username,0]
            result_args1= mycursor.callproc("logincheckusernamePatient", args)
            
            while passwordCounter <= 2:
                EnterPassword = getpass.getpass("Enter Password: ")
                
                if EnterPassword != result_args1[1]:
                    passwordCounter= passwordCounter+1
                    print("Wrong password! Try again.")

                if EnterPassword == result_args1[1]:
                    print("Logging in...")
                    patient_menu()
                    break
            else:
                print("Three wrong attmpts! Quitting application.\n")
                

        elif choice == 2:
            passwordCounter = 0
            mycursor = mydb.cursor()
            args = [username,0]
            result_args1= mycursor.callproc("logincheckusernameDoctor", args)
            
            while passwordCounter <= 2:
                EnterPassword = getpass.getpass("Enter Password: ")
                
                if EnterPassword != result_args1[1]:
                    passwordCounter= passwordCounter+1
                    print("Wrong password! Try again.")

                if EnterPassword == result_args1[1]:
                    print("Logging in...")
                    physician_menu()
            else:
                print("Three wrong attmpts! Quitting application.\n")
                


        elif choice == 3:
            passwordCounter = 0
            mycursor = mydb.cursor()
            args = [username,0]
            result_args1= mycursor.callproc("logincheckusernameStaff", args)
            
            while passwordCounter <= 2:
                EnterPassword = getpass.getpass("Enter Password: ")
                
                if EnterPassword != result_args1[1]:
                    passwordCounter= passwordCounter+1
                    print("Wrong password! Try again.")

                if EnterPassword == result_args1[1]:
                    print("Logging in...")
                    staff_menu()
            else:
                print("Three wrong attmpts! Quitting application.\n")
                
            
    else:
        print("Not an option. Quitting application")
        quit


        
        
