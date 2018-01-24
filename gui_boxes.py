import easygui

flavor = easygui.integerbox("enter a number ")
#flavor = easygui.enterbox("What is your favorite ice cream flavor?", default = 'Vanilla')
#flavor = easygui.textbox("pick an ice cream flavour")
#flavor = easygui.choicebox("choose a flavour", choices = ["chocolate", "vanilla", "strawberry"])

easygui.msgbox("you picked " + flavor)

