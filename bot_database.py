import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000")
mycursor = mydb.cursor()
mycursor.execute("use botbuck")

def register(usr):
    mycursor.execute("insert into data values('" + usr + "',100);")
    mydb.commit()
