import mysql.connector
import login
import staffMenu
# from staffMenu import staff_menu


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def modifyPhysicianProfile():
    mycursor = mydb.cursor()
    getvari = login.username
    args = [getvari,0]
    userID = getvari

    physicianID = raw_input("Enter Physician ID: ")

    print("""
    What would you like to modify?
    1 - Password
    2 - Back to previous menu
    """)
    staffInput = int(input("Option number: "))

    # if staffInput == 1:

    #   physicianUpdateAddress = str(raw_input("Enter new address: "))
    #   sql_update_query = "UPDATE doctor SET Address = %s WHERE UserID = %s"
    #   values = (physicianUpdateAddress, userID)
    #   mycursor.execute(sql_update_query, values)
    #   mydb.commit()
    #   print ("\n Address updated to " + physicianUpdateAddress + "\n")
    # #   staffMenu.patient_menu()


    if staffInput == 1:
      physicianUpdatePassword = raw_input("Enter new password: ")
      sql_update_query2 = "UPDATE doctor SET Password1 = %s WHERE UserID = %s"
      values2 = (physicianUpdatePassword, physicianID)
      mycursor.execute(sql_update_query2, values2)
      mydb.commit()
      print ("\n Password updated to " + physicianUpdatePassword + "\n")
      staffMenu.staff_menu()

    elif staffInput == 2:
        # print("Returning")
        staffMenu.staff_menu()
