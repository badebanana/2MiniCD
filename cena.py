from tkinter import*

username = 'joao'

def Login():
    global nameEL
    global rootA

    rootA = Tk() # This now makes a new window.
    rootA.title('Chat CD - Login') # This makes the window title 'login'
    rootA.geometry('260x100')

    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah

    nameL = Label(rootA, text='Username: ') # More labels
    nameL.grid(row=1, sticky=W)

    nameEL = Entry(rootA) # The entry input
    nameEL.grid(row=1, column=1)

    print(nameEL.get())

    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)

    rootA.mainloop()

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

def CheckLogin():
    if nameEL.get() == username: # Checks to see if you entered the correct data.
        r = janelaGeral() # Opens new window
        r.mainloop()

    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()


Login()


