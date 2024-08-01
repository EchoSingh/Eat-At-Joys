import mysql.connector
mydb=mysql.connector.connect (host="localhost",user="root",passwd="P@$$W0rd" )
mycursor=mydb.cursor ()
mycursor.execute("create database food")

