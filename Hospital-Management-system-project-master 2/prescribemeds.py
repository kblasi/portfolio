import mysql.connector
import login
import physicianmenu




mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="Project")

def prescribe_meds():
    mycursor = mydb.cursor()

    print("""
    What would you like to do?
    1 - Prescribe medication

    2 - Back to previous menu
    """)
    physicianInput = int(input("Option number: "))

    if physicianInput ==1:
        UserID = (raw_input("Enter patient UserID: "))
        MedicationName = (raw_input("Enter name of medication: "))
        PhysicianID = (raw_input("Enter your physician ID: "))
        Dosage = raw_input("Enter dosage: ")
        PrescriptionLength = raw_input("Enter length of prescription: ")
        sql_insert_query2 = "INSERT INTO medication (UserID, MedicationName, PhysicianID, Dosage, PrescriptionLength) VALUES(%s,%s,%s,%s,%s);"
        values2 = (UserID, MedicationName, PhysicianID, Dosage, PrescriptionLength)
        mycursor.execute(sql_insert_query2, values2)
        mydb.commit()
        
        print("\n " + " Medications have been added to the database. " + "\n")
        physicianmenu.physician_menu()

        
    if physicianInput == 2:
      physicianmenu.physician_menu()