import mysql.connector
mydb=mysql.connector.connect (host="localhost",user="root",passwd="P@$$W0rd" ,database="food")
mycursor=mydb.cursor ()
mycursor.execute("drop table if exists fooditems")
mycursor.execute("create table fooditems(foodname varchar(20) primary key,price int(5))")
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('cake',500)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('pastry',100)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('icecream',200)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('pies',100)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('custard',250)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('puddings',200)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('cupcake',100)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('rasmalai',50)
mycursor.execute(sql,val)
sql="insert into fooditems(foodname,price)values(%s,%s)"
val=('gulabjamun',200)
mycursor.execute(sql,val)
mydb.commit()
print("################# WELCOME TO JOY'S EAT ###################")
mycursor.execute("select * from fooditems")
myresult=mycursor.fetchall()
print("           Items            Price") 
for x in myresult:
    print ("        ~ ",x[0],"  -->  ",x[1])
name=input("Enter the name of item : ")
qty =int(input("Enter quantity : "))
sql2="select * from fooditems where foodname = %s"
foodname=(name,)
mycursor.execute(sql2,foodname)
myresult1=mycursor.fetchall()
print("Your receipt:")
for y in myresult1:
	print("Please pay Rs.", qty*y[1]," for ",y[0])
print("Visit Again!!! ")
    
