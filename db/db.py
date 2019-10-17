import mysql.connector as mysql
# from dotenv import load_dotenv
# import os

# load_dotenv()

# _user = os.getenv("EVERGREEN_USER")
# _password = os.getenv("EVERGREEN_PASSWORD")

# user=_user,
# password=_password,

cnx = mysql.MySQLConnection(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="evergreen",
)

'''
import mysql.connector as mysql

cnx = mysql.MySQLConnection(
    host="127.0.0.1",
    port=3306,
    user=_user,
    password=_password,
    database="evergreen",
)
'''