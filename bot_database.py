import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000")
mycursor = mydb.cursor()
mycursor.execute("use botbuck")


def register(usr):
    mycursor.execute("insert into data values('" + usr + "',100);")
    mydb.commit()


def wallet(usr):
    mycursor.execute("select primo from data where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()
    return a[0]


def update_wallet(usr, primo):
    mycursor.execute("update data set primo =" + primo + " where userid = '" + usr + "'")
    mycursor.execute("select primo from data where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()
    return a[0]
