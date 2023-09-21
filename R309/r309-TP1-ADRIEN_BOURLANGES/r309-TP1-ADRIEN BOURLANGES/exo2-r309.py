from tkinter import *
from tkinter import ttk
gui = Tk()
gui.geometry('300x300')
l = Label( gui, text = "Veuillez entrer votre Email :" )
l.pack( side = TOP )
e = Entry( gui, bd = 10 )
e.pack( side = LEFT )
s = e.get()
def valider():
    s = e.get()
    print(s)
buttonmoins = Button(gui, text="valider", command=valider)
buttonmoins.pack(side=LEFT)
gui.mainloop()