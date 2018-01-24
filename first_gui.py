import easygui

respose = easygui.buttonbox("pick favorite flavour of ice cream", choices = ["Vanilla", "chocolate", "blackberry"])

easygui.msgbox( "you picked " + respose)

 