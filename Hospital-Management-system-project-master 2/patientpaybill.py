import mysql.connector
import patientmenu
import login


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def paybill():
    mycursor = mydb.cursor()
    getvari = login.username
    args = [getvari,0]
    userID = getvari

    result_args1= mycursor.callproc("getpatientbill", args)
    balance = result_args1[1]

    print("\nCurrent balance: " + balance)
    print("1 - Pay balance")
    print("2 - Patient menu\n")

    choice = int(raw_input("Option number: "))

    if choice == 1:
        paid = raw_input("Enter the amount you would like to pay today: ")
        subtract = (int(balance))- (int(paid)) 
        sql_update_query2 = "UPDATE patient SET Bill = %s WHERE UserID = %s"
        values2 = (subtract, userID)
        mycursor.execute(sql_update_query2, values2)
        mydb.commit()
        print("Your balance is now: " + (str(subtract)))
        patientmenu.patient_menu()

        

    elif choice == 2:
        patientmenu.patient_menu()
    
    else:
        print("Not an option. Quitting application!")
        quit
