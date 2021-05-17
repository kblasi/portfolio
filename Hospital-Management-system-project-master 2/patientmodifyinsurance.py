import mysql.connector
import login
import patientmenu

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def patientmodifyinsurance():
    mycursor = mydb.cursor()
    getvari = login.username
    args = [getvari,0]
    userID = getvari

    print("""
    What would you like to modify?
    1 - Insurance provider
    2 - Expiration date

    3 - Back to patient menu
    """)

    patientInput = int(input("Option number: "))

    if patientInput == 1:

      patientUpdateProvider = str(raw_input("Enter new insurance provider: "))
      sql_update_query = "UPDATE insurance SET insuranceName = %s WHERE patientuserID = %s"
      values = (patientUpdateProvider, userID)
      mycursor.execute(sql_update_query, values)
      mydb.commit()
      print ("\n Provider updated to " + patientUpdateProvider + "\n")
      patientmenu.patient_menu()

    elif patientInput == 2:
      patientUpdateExpir = raw_input("Enter new expiration date (YYYY-MM-DD): ")
      sql_update_query2 = "UPDATE insurance SET expirationDate = %s WHERE patientuserID = %s"
      values2 = (patientUpdateExpir, userID)
      mycursor.execute(sql_update_query2, values2)
      mydb.commit()
      print ("\n Expiration date updated to " + patientUpdateExpir + "\n")
      patientmenu.patient_menu()

    elif patientInput == 3:
      patientmenu.patient_menu()
