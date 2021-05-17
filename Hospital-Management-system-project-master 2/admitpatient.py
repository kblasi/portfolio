import mysql.connector
import login
import physicianmenu




mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="Project")

def admit_patient():
    mycursor = mydb.cursor()

    username2 = int(raw_input("Enter Patient UserID: "))
    getvari = username2
    args = [getvari,0]


    print("""
    What would you like to enter?
    1 - Date of admission (MM/DD/YY)
    2 - Time of admission
    3 - Admission status

    4 - Back to previous menu
    """)
    physicianInput = int(input("Option number: "))

    if physicianInput ==1:
        dateofadmit = (raw_input("Date of admission (MM/DD/YY): "))
        sql_update_query = "UPDATE admission SET dateofadmit = %s WHERE UserID = %s"
        values = (dateofadmit, username2)
        mycursor.execute(sql_update_query, values)
        mydb.commit()

        print ("\n Date of admission updated to " + dateofadmit + "\n")
        physicianmenu.physician_menu()

    elif physicianInput ==2:
        timeofadmit = (raw_input("Enter time of admission: "))
        sql_update_query = "UPDATE admission SET timeofadmit = %s WHERE UserID = %s"
        values1 = (timeofadmit, username2)
        mycursor.execute(sql_update_query, values1)
        mydb.commit()

        print("\n Time of admission updated to " + timeofadmit +"\n")
        physicianmenu.physician_menu()

    elif physicianInput ==3:
        status = raw_input("Admit? Y/N: ")
        sql_update_query = "UPDATE admission SET status = %s WHERE UserID = %s"
        values2 = (status, username2)
        mycursor.execute(sql_update_query, values2)
        mydb.commit()
        
        print("Patient is admitted")
        physicianmenu.physician_menu()

    elif physicianInput == 4:
      physicianmenu.physician_menu()
    