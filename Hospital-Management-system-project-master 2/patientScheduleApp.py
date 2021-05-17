import mysql.connector
import patientmenu
import login


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def schedApp():
    mycursor = mydb.cursor()
    getvari = login.username
    args = [getvari,0]
    userID = getvari


    inputDate = raw_input("Please enter the desired date of the appointment (YYYY-MM-DD): ")
    inputTime = raw_input("Please enter the desired time between 8AM and 4PM (hh:mm): ")
    inputPhysician = raw_input("Please enter the UserID of the desired physician: ")
    inputReason = raw_input("Please enter the reason for the appointment: ")

    sql_update_query2 = "INSERT INTO appointment(userID, Date, Time, physicanID, reason) VALUES(%s,%s,%s,%s,%s);"
    values = (getvari,inputDate,inputTime,inputPhysician,inputReason)
    mycursor.execute(sql_update_query2, values)
    mydb.commit()

    print ("\n Appointment created!")
    patientmenu.patient_menu()
