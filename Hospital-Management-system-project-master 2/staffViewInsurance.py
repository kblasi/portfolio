import mysql.connector
import login
import staffMenu

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def staffViewInsurance():
    mycursor = mydb.cursor()
    getvari = raw_input("Enter patient user ID: ")
    args = [getvari,0]

    result_args2= mycursor.callproc("patientviewinsurancename", args)
    result_args3= mycursor.callproc("patientviewinsuranceExpiration", args)

    print("\n")

    print_insurance =("""Insurance provider: {0} \nExpirantion Date: {1} """)

    print (print_insurance.format(result_args2[1], result_args3[1]))

    print("""
    1 - Quit
    2 - Back to previous menu
    """)
    staffInput = int(input("Option number: "))

    if staffInput == 1:
        quit()
    elif staffInput == 2:
        staffMenu.staff_menu()
