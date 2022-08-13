import eel
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='root')
mycursor = mydb.cursor()
eel.init('web')
state = ""

def create_database(dbname):
    mycursor.execute(("create database if not exists {}").format(dbname))
    mycursor.execute(("use {}").format(dbname))
    print("db createed and now in use")

def create_table(tablename, dataformat):
    mycursor.execute(("create table if not exists {} ({})").format(tablename, dataformat))
    print("db createed and now in use")

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
        #create_table("users", "userid INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), accesslevel int(1)")
        


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
