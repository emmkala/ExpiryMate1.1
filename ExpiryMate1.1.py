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



##New user button in the bottom left.
newUserB = Button(bottomFrame, text="Add New User", fg="green")
newUserB.pack(side=BOTTOM)

homePage.mainloop()

