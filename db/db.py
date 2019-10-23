import mysql.connector as mysql

cnx = mysql.MySQLConnection(
    host="evergreen-db-server.mysql.database.azure.com",
    port=3306,
    user="evergreenadmin@evergreen-db-server",
    password="abcd.1234",
    database="evergreen",
)
