import tkinter as tk
from tkinter import font as tkfont

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
        newUser = tk.Button(self, text="New User", bg="#89bf85",
                            command=lambda: controller.show_frame("CreateUser"))
        newUser['font'] = controller.text_font
        functionalScreen = tk.Button(self, text="Existing User", bg="#78a974",
                                     command=lambda: controller.show_frame("FunctionalPage"))
        functionalScreen['font'] = controller.text_font
        quitButton = tk.Button(self, text="Quit", bg="#60875d",
                               command=lambda: exit())
        quitButton['font'] = controller.text_font
        newUser.pack(pady=25)
        functionalScreen.pack(pady=25)
        quitButton.pack(pady=75)

class CreateUser(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Please Sign Up to Continue!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        enterName = tk.Entry(self)
        enterName.pack()
        toFunctions = tk.Button(self, text="Go to Main Menu.", bg="green",
                                command=lambda: controller.show_frame("FunctionalPage"))
        toFunctions.pack()
        

class FunctionalPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Functions Page!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        returnMenu = tk.Button(self, text="Return to the home page.", bg="green",
                               command=lambda: controller.show_frame("TitlePage"))
        returnMenu.pack()

if __name__ == "__main__":
    app = ExpiryMate()
    app.mainloop()
