from guizero import App, Combo, Text, TextBox, PushButton, yesno, Picture
import translate

#Check language type and convert to abbr for API
def checkLang(lang):
    dic = {"Chinese": "zh", "English": "en", "Japanese": "jp", "Korean": "kor", "Vietnamese": "vie" ,"French": "fra", "Spanish": "spa", "Thai": "th", "Arabic": "ara", "Russian": "ru", "German": "de", "Italian": "it", "Greek": "el", "Auto": "auto"}
    return dic[lang]

#Function passing three paremeters for API; Current language type, Content, and result language type and get result
def show():
    finalresult.value = translate.translate(checkLang(choice.value), check.value, checkLang(buttons.value))

def do_this_onClose():
    if yesno("Close", "Do you want to close the app?"):
        app.destroy()

#GUI zero 
app = App(title = "JWS translate", width = 450, height = 350,layout = "grid")
choice = Combo(app, options = ["Auto", "English", "Korean", "Chinese", "Spanish", "Japanese", "Vietnamese", "French",  "Thai", "Arabic", "Russian", "German", "Italian", "Greek"], grid = [1,0], align = "left")
description = Text(app,text = "Select the Language: ", grid = [0,0])
check = TextBox(app,text = "", grid = [1,1], width = 35, height = 6, scrollbar = True, multiline = True)
descripChek = Text(app, text = "Content: ", grid = [0,1], align = "left")
buttons = Combo(app, options = ["English", "Korean", "Chinese", "Spanish", "Japanese", "Vietnamese", "French",  "Thai", "Arabic", "Russian", "German", "Italian", "Greek"], grid = [1,3], align = "left")
descripbuG = Text(app, text = "Translate to ", grid = [0,3], align = "left")
done = PushButton(app, command = show, text = "Translate", grid = [1,4])
finalresultText = Text(app, text = "Result: ",grid = [0,5], align = "left")
finalresult = TextBox(app, text = "", grid=[1,5], align = "left", multiline = True, width = 35, height = 6, scrollbar = True)

check.focus()
app.on_close(do_this_onClose)
app.display()