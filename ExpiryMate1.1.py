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
        
        self.title_font = tkfont.Font(family='Georgia', size=28, weight="bold", slant="italic")
        self.subtitle_font = tkfont.Font(family='Georgia', size=16, weight='bold', slant="italic")
        self.text_font = tkfont.Font(family='Georgia', size=10, weight='bold', slant="italic")
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
        labelHidden1 = tk.Label(self, text="000", fg="#aff2a9", bg="#aff2a9")
        labelHidden1.pack(side="left", fill="y", padx=16)
        labelHidden2 = tk.Label(self, text="000", fg="#aff2a9", bg="#aff2a9")
        labelHidden2.pack(side="right", fill="y", padx=16)
        labelLogo = tk.Label(self, text="ExpiryMate", font=controller.title_font, bg="#60875d", fg="#aff2a9")
        labelSub = tk.Label(self, text="Sign In or Sign Up", font=controller.subtitle_font, bg="#78a974", fg="#a1dd9c")
        labelLogo.pack( fill="x", pady=10)
        labelSub.pack( fill="x", pady=15)
        newUser = tk.Button(self, text="Add a new user", fg="white", bg="#89bf85",
                            command=lambda: controller.show_frame("CreateUser"))
        newUser['font'] = controller.text_font
        functionalScreen = tk.Button(self, text="Sign In", fg="white", bg="#78a974",
                                     command=lambda: controller.show_frame("FunctionalPage"))
        functionalScreen['font'] = controller.text_font
        quitButton = tk.Button(self, text="Click to Quit", fg="white", bg="#60875d",
                               command=lambda: exit())
        quitButton['font'] = controller.text_font
        newUser.pack(fill="x", pady=25)
        functionalScreen.pack(fill="x", pady=25)
        quitButton.pack(fill="x", pady=75)

class CreateUser(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        labelHidden1 = tk.Label(self, text="000", fg="#aff2a9", bg="#aff2a9")
        labelHidden1.pack(side="left", fill="y", padx=16)
        labelHidden2 = tk.Label(self, text="000", fg="#aff2a9", bg="#aff2a9")
        labelHidden2.pack(side="right", fill="y", padx=16)
        labelLogo = tk.Label(self, text="ExpiryMate", font=controller.title_font, bg="#60875d", fg="#aff2a9")
        labelLogo.pack( fill="x", pady=10)
        label1 = tk.Label(self, text="Sign Up to Continue!", font=controller.subtitle_font, bg="#78a974", fg="#a1dd9c")
        label1.pack(fill="x", pady=15)
        enterName = tk.Entry(self)
        enterName.pack(fill="x")
        setUser = tk.Button(self, text="Sign Up", fg="white", bg="#89bf85",
                                command=lambda: createUser(enterName.get()))
        setUser['font'] = controller.text_font
        toFunctions = tk.Button(self, text="Proceed to Your Pantry", fg="white", bg="#78a974",
                                command=lambda: controller.show_frame("FunctionalPage"))
        toFunctions['font'] = controller.text_font
        setUser.pack(fill="x", pady=25)
        toFunctions.pack(fill="x", pady=25)

        

class FunctionalPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Functions Page!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        t = SimpleTable(self)
        t.pack(side="right", fill="y")

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

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    app = ExpiryMate()
    app.mainloop()
