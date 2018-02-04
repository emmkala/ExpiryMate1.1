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
##Insert username entry slot with caption.
entryHeader = Label(bottomFrame, text="Please Enter A Username: ", fg="green")
entryHeader.config(font=('itallic',18))
entryHeader.place(x=485, y=300)
enterName = Entry(bottomFrame)
enterName.place(x=775, y=306)
##New user button in the bottom left.
newUserB = Button(bottomFrame, text="Add New User", fg="green")
newUserB.place(x=1200, y=700)

homePage.mainloop()

