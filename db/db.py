import mysql.connector as mysql

# cnx = mysql.MySQLConnection(
#     host="evergreen-db-server.mysql.database.azure.com",
#     port=3306,
#     user="evergreenadmin@evergreen-db-server",
#     password="abcd.1234",
#     database="evergreen",
# )
cnx = mysql.connector.connect(
    user="evergreenadmin@evergreen-db-server", 
    password="abcd.1234", 
    host="evergreen-db-server.mysql.database.azure.com", 
    port=3306, 
    database="evergreen", 
    ssl_verify_cert=false
)
