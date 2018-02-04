from tkinter import *

##Create home page for the UI.
homePage = Tk()
topFrame = Frame(homePage, width=1500, height=900)
topFrame.pack()
bottomFrame = Frame(homePage, width=1500, height=900)
bottomFrame.pack(side=BOTTOM)
##Create the title or header of our home page introducing them to the app.
header = Label(topFrame, text="Welcome to ExpiryMate!", fg="green")
header.config(font=('bold',36))
header.pack()

<<<<<<< HEAD
test_1 = Label(homePage, text="Test")
test_1.pack()
=======


##New user button in the bottom left.
newUserB = Button(bottomFrame, text="Add New User", fg="green")
newUserB.pack(side=BOTTOM)
>>>>>>> 04a6ea52fc856820ffae5c3ad41056445982f792

homePage.mainloop()

