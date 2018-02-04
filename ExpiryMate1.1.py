from CSVeditor import CSVeditor
import tkinter as tk
from tkinter import font as tkfont
from userClass import User

currentUser = User("")

def createUser(name):
        currentUser = User(name)
        
class ExpiryMate(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title_font = tkfont.Font(family='Helvecita', size=28, weight="bold", slant="italic",)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (TitlePage, CreateUser, FunctionalPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("TitlePage")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class TitlePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This Is The Title Page", font=controller.title_font)
        label.pack( fill="x", pady=10)
        newUser = tk.Button(self, text="Add a new user", bg="green",
                            command=lambda: controller.show_frame("CreateUser"))
        functionalScreen = tk.Button(self, text="Click Here if you are an existing user", bg="green",
                                     command=lambda: controller.show_frame("FunctionalPage"))
        quitButton = tk.Button(self, text="Click to Quit", bg="green",
                               command=lambda: exit())
        newUser.pack()
        functionalScreen.pack()
        quitButton.pack()

class CreateUser(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Please create a new user to continue!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        enterName = tk.Entry(self)
        enterName.pack()
        setUser = tk.Button(self, text="Set New User.", bg="green",
                                command=lambda: createUser(enterName.get()))
        toFunctions = tk.Button(self, text="Proceed to Functional Page", bg="green",
                                command=lambda: controller.show_frame("FunctionalPage"))
        setUser.pack()
        toFunctions.pack()

        

class FunctionalPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Functions Page!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        enterFood = tk.Entry(self)
        enterFood.pack()
        enterDay = tk.Entry(self)
        enterDay.pack()
        addFood = tk.Button(self, text="Click here to add a new food item!", bg="green",
                            command=lambda: currentUser.addItem(enterFood.get(),int(enterDay.get())))
        addFood.pack()

        deleteFood = tk.Entry(self)
        deleteFood.pack()
        removeFood = tk.Button(self, text="Click here to remove the entered food item.", bg="green",
                               command=lambda: currentUser.deleteItem(deleteFood.get()))
        removeFood.pack()
        
        returnMenu = tk.Button(self, text="Return to the home page.", bg="green",
                               command=lambda: controller.show_frame("TitlePage"))
        returnMenu.pack()

if __name__ == "__main__":
    app = ExpiryMate()
    app.mainloop()
