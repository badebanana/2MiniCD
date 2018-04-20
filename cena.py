from tkinter import*

def menu(janelaGeral):
    def quitApp():
        janelaGeral.quit()

    menuBar = Menu(janelaGeral)
    optionsMenu = Menu(menuBar, tearoff=0)
    optionsMenu.add_command(label="Nova sala")
    optionsMenu.add_command(label="Entrar noutra sala")
    optionsMenu.add_separator()
    optionsMenu.add_command(label="Exit", command=quitApp)
    menuBar.add_cascade(label="Sala", menu=optionsMenu)
    janelaGeral.config(menu=menuBar)

def janelaGeral():
    janelaGeral = Tk()
    janelaGeral.title("#MerdaGeral")
    janelaGeral.geometry('450x450')
    menu(janelaGeral)

    def click():
        messageBox.insert('0.0',textEntry.get()+"\n")
        textEntry.delete(0, 'end')

    messageBox = Text(janelaGeral, wrap='word', width=50, height=25, background="white")
    messageBox.place(x=5, y=0)
    #Fazer scrollBar na messageBox
    label = Label(janelaGeral, text="Message")
    label.place(x=5, y=410)
    textEntry = Entry(janelaGeral, width=50)
    textEntry.place(x=60, y=410)
    btn = Button(janelaGeral, text="Send", command=click)
    btn.place(x=370, y=405)
    janelaGeral.mainloop()

#janelaGeral()

def entrar():
    janelaGeral()

class Interface:
    def __init__(self, janelaUser):
        self.janelaUser = janelaUser
        janelaUser.title("Chat de CD")
        janelaUser.geometry('400x200')

        self.label = Label(janelaUser, text="CHAT CD")
        self.label.config(font=("verdana",20,"bold"))
        self.label.place(x=135,y=10)
        self.labelUser = Label(janelaUser, text="Nome de Utilizador:")
        self.labelUser.place(x=45, y=85)
        self.textEntry = Entry(janelaUser, width=30)
        self.textEntry.place(x=160, y=85)
        self.btn = Button(janelaUser, text="Entrar", command=entrar)
        self.btn.place(x=175, y=120)

    def guardarNome(self):
        print(self.textEntry.get())

