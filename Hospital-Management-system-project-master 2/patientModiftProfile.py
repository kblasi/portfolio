import mysql.connector
import login
import patientmenu


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="rincon413",
  database="Project"
)

def modifyPatientProfile():
    mycursor = mydb.cursor()
    getvari = login.username
    args = [getvari,0]
    userID = getvari

    print("""
    What would you like to modify?
    1 - Address
    2 - Password

    3 - Back to previous menu
    """)
    patientInput = int(input("Option number: "))

    if patientInput == 1:

      patientUpdateAddress = str(raw_input("Enter new address: "))
      sql_update_query = "UPDATE patient SET Address = %s WHERE UserID = %s"
      values = (patientUpdateAddress, userID)
      mycursor.execute(sql_update_query, values)
      mydb.commit()
      print ("\n Address updated to " + patientUpdateAddress + "\n")
      patientmenu.patient_menu()


    elif patientInput == 2:
      patientUpdatePassword = raw_input("Enter new password: ")
      sql_update_query2 = "UPDATE patient SET Password1 = %s WHERE UserID = %s"
      values2 = (patientUpdatePassword, userID)
      mycursor.execute(sql_update_query2, values2)
      mydb.commit()
      print ("\n Password updated to " + patientUpdatePassword + "\n")
      patientmenu.patient_menu()

    elif patientInput == 3:
      patientmenu.patient_menu()
