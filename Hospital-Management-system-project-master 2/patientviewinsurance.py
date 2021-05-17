import mysql.connector
import login
import patientmenu
import patientmodifyinsurance

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def patientViewInsurance():
    mycursor = mydb.cursor()
    getvari = login.username
    args = [getvari,0]

    result_args2= mycursor.callproc("patientviewinsurancename", args)
    result_args3= mycursor.callproc("patientviewinsuranceExpiration", args)

    print("\n")

    print_insurance =("""Insurance provider: {0} \nExpirantion Date: {1} """)

    print (print_insurance.format(result_args2[1], result_args3[1]))
    print("\n")

    back_result = raw_input("Would you like modify your insurance information? (Y/N): ")

    if back_result == ("Y") or back_result == ("y") or back_result == ("N") or back_result == ("n"):
        if back_result ==("Y") or back_result ==("y"):
            patientmodifyinsurance.patientmodifyinsurance()
        elif back_result == ("N") or back_result == ("n"):
            patientmenu.patient_menu()
            
