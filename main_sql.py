import eel
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='root')
mycursor = mydb.cursor()
eel.init('web')
state = ""

@eel.expose
def getdashboard():
    mycursor.execute("SELECT SUM(Price) AS 'Total Sales' FROM transactions where status = 'completed'")
    returnlist = []
    for row in mycursor:
        print(row)
        returnlist.append(row)
    print(returnlist)
    eel.sqlreturndashboard(returnlist)

@eel.expose
def update_password(tablename, value, condition):
    print(("update {} set password = {} where {}").format(tablename, value, condition))
    mycursor.execute(("update {} set password = {} where {}").format(tablename, value, condition))
    mydb.commit()

@eel.expose
def update_accesslevel(tablename, value, condition):
    print(("update {} set accesslevel = {} where {}").format(tablename, value, condition))
    mycursor.execute(("update {} set accesslevel = {} where {}").format(tablename, value, condition))
    mydb.commit()

@eel.expose
def update_cost(tablename, value, condition):
    print(("update {} set cost = {} where {}").format(tablename, value, condition))
    mycursor.execute(("update {} set cost = {} where {}").format(tablename, value, condition))
    mydb.commit()
    
@eel.expose
def update_quantity(tablename, value, condition):
    print(("update {} set quantity = {} where {}").format(tablename, value, condition))
    mycursor.execute(("update {} set quantity = {} where {}").format(tablename, value, condition))
    mydb.commit()

@eel.expose
def update_specific(tablename, value, condition):
    print(("update {} set value = {} where {}").format(tablename, value, condition))
    mycursor.execute(("update {} set value = {} where {}").format(tablename, value, condition))
    mydb.commit()

@eel.expose
def update_status_todo(tablename, value, condition):
    print(("update {} set Status = {} where {}").format(tablename, value, condition))
    mycursor.execute(("update {} set Status = {} where {}").format(tablename, value, condition))
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
        create_table("users", "username varchar(50) PRIMARY KEY NOT NULL, Imageurl varchar(512), Date varchar(20) NOT NULL, password varchar(40) NOT NULL, accesslevel int(4) NOT NULL")
        
    if (stateparam == "loginpage"):
        create_database("CsProj")
        create_table("users", "username varchar(50) PRIMARY KEY NOT NULL, Imageurl varchar(512), Date varchar(20) NOT NULL, password varchar(40) NOT NULL, accesslevel int(4) NOT NULL")
 
    

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
        mycursor.execute('select password from users where username = "{}"'.format(username))
        returnlist = []
        for row in mycursor:
            print(row)
            returnlist.append(row)
            print(returnlist[0][0])
        if (str(returnlist[0][0]) == str(password)):
            eel.switchpage("mainpage")
            print("success")
            #admin
        else:
            #not admin
            eel.switchpage("loginfailed")


eel.start('login.html', port=8080)
