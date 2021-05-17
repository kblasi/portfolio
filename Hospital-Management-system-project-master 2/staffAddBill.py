import mysql.connector
import staffMenu
import login


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)

def addBill():
    mycursor = mydb.cursor()
    getvari = raw_input("Enter patient user ID: ")
    args = [getvari,0]
    userID = getvari

    result_args1= mycursor.callproc("getpatientbill", args)
    balance = result_args1[1]

    print("\nCurrent balance: " + str(balance))
    print("1 - Add balance")
    print("2 - Staff menu\n")

    choice = int(raw_input("Option number: "))

    if choice == 1:
        bill = raw_input("Enter the amount you would like to add to bill: ")
        addition = (int(balance))+ (int(bill)) 
        sql_update_query2 = "UPDATE patient SET Bill = %s WHERE UserID = %s"
        values2 = (addition, userID)
        mycursor.execute(sql_update_query2, values2)
        mydb.commit()
        print("Patient balance is now: " + (str(addition)))

        print("""
        1 - Quit
        2 - Back to previous menu
        """)
        staffInput = int(input("Option number: "))

        if staffInput == 1:
            quit()
        elif staffInput == 2:
            staffMenu.staff_menu()


    elif choice == 2:
        staffMenu.staff_menu()
    
    else:
        print("Not an option. Quitting application!")
        quit
