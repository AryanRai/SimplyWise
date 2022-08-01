import eel
eel.init('web')
state = ""

@eel.expose
def sendstate(stateparam):
    print("change in state"+ " state is " + stateparam)
    global state
    state = stateparam
    eel.switchpage(stateparam)

@eel.expose
def checklogin(usernameparam, passwordparam):
    print("login creds are username: " + usernameparam + " password: " + passwordparam)
    global username
    global password
    username = usernameparam
    password = passwordparam
    eel.switchpage("mainpage")



eel.start('login.html')
