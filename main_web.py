import eel
eel.init('web')
state = ""

@eel.expose
def sendstate(stateparam):
    print("change in state"+ " state is " + stateparam)
    global state
    state = stateparam
    eel.switchpage(stateparam)

eel.start('main.html')
