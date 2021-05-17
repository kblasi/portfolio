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

def addPhysicianProfile():
    mycursor = mydb.cursor()
    getvari = login.username
    args = [getvari,0]
    userID = getvari

    # physicianFirstName = raw_input("First Name: ")


    print("""
    Welcome! Please sellect the following
    1 - Create Physician profile
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
      physicianFirstName = raw_input("First Name: ")
      physicianLastName = raw_input("Last Name: ")
      physicianEmail = raw_input("Email: ")
      physicianPassword = raw_input("Password: ")
      physicianUserID = raw_input("User ID: ")
      physicianSpecialty = raw_input("Specialty: ")
      sql_insert_query2 = "INSERT INTO doctor (FirstName, LastName, Email, Password1, UserID, Speciality) VALUES (%s, %s, %s, %s, %s, %s);"
      values2 = (physicianFirstName, physicianLastName, physicianEmail, physicianPassword, physicianUserID, physicianSpecialty)
      mycursor.execute(sql_insert_query2, values2)
      mydb.commit()
      print ("\n" + "Profile is added into the database." + "\n")
      staffMenu.staff_menu()

    elif staffInput == 2:
        # print("Returning")
        staffMenu.staff_menu()
