import eel
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='root')
mycursor = mydb.cursor()
eel.init('web')
state = ""

@eel.expose
def update_specific(tablename, value, condition):
    print(("update {} set value = {} where {}").format(tablename, value, condition))
    mycursor.execute(("update {} set value = {} where {}").format(tablename, value, condition))
    mydb.commit()

@eel.expose
def droptable(tablename):
    print(("drop table {}").format(tablename))
    mycursor.execute(("drop table {}").format(tablename))
    mydb.commit()

@eel.expose
def delete_specific(tablename, condition):
    print(("delete from {} where {}").format(tablename, condition))
    mycursor.execute(("delete from {} where {}").format(tablename, condition))
    mydb.commit()

@eel.expose
def insert_into_table(tablename, values):
    print(("insert into {} values({})").format(tablename, values))
    mycursor.execute(("insert into {} values({})").format(tablename, values))
    mydb.commit()

@eel.expose
def insert_into_table_autoinc(tablename, fields ,values):
    print(("insert into {} ({}) values({})").format(tablename, fields, values))
    mycursor.execute(("insert into {} ({}) values({})").format(tablename, fields, values))
    mydb.commit()

@eel.expose
def getall(tablename):
    mycursor.execute(("select * from {}").format(tablename))
    returnlist = []
    for row in mycursor:
        print(row)
        returnlist.append(row)
    eel.sqlreturn(returnlist)
    

@eel.expose
def getspecific(tablename, condition):
    mycursor.execute(("select * from {} where {}").format(tablename, condition))

@eel.expose
def create_database(dbname):
    mycursor.execute(("create database if not exists {}").format(dbname))
    mycursor.execute(("use {}").format(dbname))
    print(("db created {} and now in use").format(dbname))
    mydb.commit()

@eel.expose
def create_table(tablename, dataformat):
    print(("create table if not exists {} ({})").format(tablename, dataformat))
    mycursor.execute(("create table if not exists {} ({})").format(tablename, dataformat))
    print(("table {} created").format(tablename))
    mydb.commit()

@eel.expose
def sendstate(stateparam):
    print("change in state"+ " state is " + stateparam)
    global state
    state = stateparam
    statechangereact(stateparam)
    eel.switchpage(stateparam)

def statechangereact(stateparam):
    if (stateparam == "loginpage"):
        create_database("CsProj")
        create_table("users", "username VARCHAR(50) PRIMARY KEY NOT NULL, password VARCHAR(50) NOT NULL, accesslevel INT(1), fname VARCHAR(50), lname VARCHAR(50), DOB date, phonenumber INT(10), email VARCHAR(100)")
        
    if (stateparam == "loginpage"):
        create_database("CsProj")
        create_table("users", "username VARCHAR(50) PRIMARY KEY NOT NULL, password VARCHAR(50) NOT NULL, accesslevel INT(1), fname VARCHAR(50), lname VARCHAR(50), DOB date, phonenumber INT(10), email VARCHAR(100)")
 
    

@eel.expose
def checklogin(usernameparam, passwordparam):
    print("login creds are username: " + usernameparam + " password: " + passwordparam)
    global username
    global password
    username = usernameparam
    password = passwordparam
    if (username == "admin" and password == "root"):
        #admin
        eel.switchpage("mainpage")

    else:
        #not admin
        eel.switchpage("loginfailed")


eel.start('login.html', port=8080)
