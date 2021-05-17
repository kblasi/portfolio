import mysql.connector
from login import login

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="YOURPASSWORD",
  database="Project"
)


def main():
    login()


main()
