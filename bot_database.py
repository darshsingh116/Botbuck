import time

import mysql.connector


# mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000" , auth_plugin='mysql_native_password')
# mycursor = mydb.cursor()
# mycursor.execute("use botbuck")


def register(usr):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("insert into data values('" + usr + "',100 ,0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);")
    mydb.commit()

    mycursor.close()


def wallet(usr):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select primo from data where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()
    return a[0]


def update_wallet(usr, primo):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
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
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select wish_time from data where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()
    return a[0]


def wish_timestamp_update(usr, time):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("update data set wish_time = " + str(time) + " where userid = '" + usr + "'")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()


def starter(usr, character):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute(("update data set " + character + " = 1 where userid = '" + usr + "';"))
    mydb.commit()

    mycursor.close()


def wish_character(usr, character):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute(("update data set " + character + " = " + character + "+ 1 where userid = '" + usr + "';"))
    mydb.commit()

    mycursor.close()

def token():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select * from token ")
    a = mycursor.fetchone()
    mydb.commit()

    mycursor.close()
    return a[0]

def inv_name(usr):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")
    mycursor.execute("select amber,kaeya,lisa,barbara,diluc,jean,razor,klee,bennett,noelle,fischl,sucrose,mona,diona,albedo, rosaria,eula,venti from data where userid='"+usr+"'")

    x = mycursor.description

    return x

def inv_value(usr):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")
    mycursor.execute("select amber,kaeya,lisa,barbara,diluc,jean,razor,klee,bennett,noelle,fischl,sucrose,mona,diona,albedo, rosaria,eula,venti from data where userid='"+usr+"'")

    x = mycursor.fetchone()

    return x



def enemy_stat(enemy):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select element,hp,atk from enemies where name='" + enemy + "'")

    x = mycursor.fetchone()
    mycursor.close()
    return x


def char_stat(character):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select element,hp,atk from stats where character_name='" + character + "'")


    x = mycursor.fetchone()
    mycursor.close()
    return x

def check_char(user,character):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="0000",
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use botbuck")

    mycursor.execute("select " + character + " from data where userid='"+user+"'")

    x = mycursor.fetchone()
    mycursor.close()
    return x