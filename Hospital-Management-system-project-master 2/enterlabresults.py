import mysql.connector
import login
import physicianmenu




mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="Project")

def enter_lab_results():
    mycursor = mydb.cursor()

    print("""
    What would you like to do?
    1 - Enter in lab results

    2 - Back to previous menu
    """)
    physicianInput = int(input("Option number: "))

    if physicianInput ==1:
        UserID = (raw_input("Enter patient UserID: "))
        labdate = (raw_input("Enter date of lab: "))
        labtest = (raw_input("Enter test completed: "))
        labresults = raw_input("Enter results of lab: ")
        furtheractions = raw_input("Further actions to be taken: ")
        sql_insert_query = "INSERT INTO lab (UserID,dateoflab, labtest, labresults, furtheractions) VALUES(%s,%s,%s,%s,%s);"
        values = (UserID, labdate, labtest, labresults, furtheractions)
        mycursor.execute(sql_insert_query, values)
        mydb.commit()
        
        print("\n " + " Lab results have been added to the database. " + "\n")
        physicianmenu.physician_menu()

        
    if physicianInput == 2:
      physicianmenu.physician_menu()