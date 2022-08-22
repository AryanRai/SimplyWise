import eel
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='root')
mycursor = mydb.cursor()
eel.init('web')
state = ""

def insert_into_table(tablename, values):
    mycursor.execute(("insert into {} values({})").format(tablename))

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

@eel.expose
def create_table(tablename, dataformat):
    mycursor.execute(("create table if not exists {} ({})").format(tablename, dataformat))
    print(("table {} created").format(tablename))

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
