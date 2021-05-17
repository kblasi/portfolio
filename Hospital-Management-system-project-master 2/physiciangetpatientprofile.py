import mysql.connector
import login
import physicianmenu
# from physicianmenu import physician_menu



mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="Project"
)

def physicianGetPatientProfile():
    mycursor = mydb.cursor()
    getvari = physicianmenu.username1
    args = [getvari,0]

    result_args2= mycursor.callproc("patientProfileFirstname", args)
    result_args3= mycursor.callproc("patientProfileLastname", args)
    result_args4= mycursor.callproc("patientProfileAddress", args)
    result_args5= mycursor.callproc("patientProfileEmail", args)
    result_args6= mycursor.callproc("patientProfileUserID", args)
    result_args7= mycursor.callproc("patientProfileDOB", args)

    print_profile =("""First Name: {0}\nLast Name: {1}\nAddress: {2}\nEmail: {3}\nUserID: {4}\nDOB: {5}""")
    
    print("\n| Your patient's profile |")
    print('---------------')
    print (print_profile.format(result_args2[1], result_args3[1], result_args4[1], result_args5[1], result_args6[1], result_args7[1]))
    print('---------------')

    back_result = raw_input("Would you like to return to Physician menu? (Y/N): ")

    if back_result == ("Y") or back_result == ("N"):
        if back_result ==("Y"):
            print("Okay")
            physicianmenu.physician_menu()
        elif back_result == ("N"):
            print("Okay, logging out...")
            quit

    else:
        print("Not an option. Quitting application")
        quit  



