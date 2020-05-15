import mysql.connector

# connection to DB

con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="pythonDB")
# to check the connectivity
# print(con)


