import time

import mysql.connector


# mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000" , auth_plugin='mysql_native_password')
# mycursor = mydb.cursor()
# mycursor.execute("use botbuck")


def register(usr):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("insert into data values('" + usr + "',100 ,0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);")
    mydb.commit()

    mycursor.close()


def wallet(usr):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select primo from data where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()
    return a[0]


def update_wallet(usr, primo):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("update data set primo =" + primo + " where userid = '" + usr + "'")
    mycursor.execute("select primo from data where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()
    return a[0]


def wish_timestamp_get(usr):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select wish_time from data where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()
    return a[0]


def wish_timestamp_update(usr, time):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("update data set wish_time = " + str(time) + " where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()


def starter(usr, character):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute(("update data set " + character + " = 1 where userid = '" + usr + "';"))
    mydb.commit()

    mycursor.close()


def wish_character(usr, character):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute(("update data set " + character + " = " + character + "+ 1 where userid = '" + usr + "';"))
    mydb.commit()

    mycursor.close()

def token():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="BotBuck123!",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select * from token ")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()
    return a[0]
