from tkinter import *
from tkinter import ttk

gui = Tk()
gui.title("Identification")
gui.geometry("300x150")

arobase = False
point = False
espace = False
def envoyer():
	print(mail.get())

def touche(key):
	if "@" in mail.get():
		arobase = True
	else:
		arobase = False
	if "." in mail.get():
		point = True
	else:
		point = False
	if " " not in mail.get():
		espace = False
	else:
		espace = True
		
	if arobase==True and point==True and espace==False:
		but1.configure(state=NORMAL)
	else: 
		but1.configure(state=DISABLED)
		
label = ttk.Label(gui,text="Veuillez entre votre Email :")
label.pack(pady=5)

mail=ttk.Entry(gui)
mail.pack()

but1=ttk.Button(gui, width = 20, text="Valider:",state=DISABLED, command=envoyer)
but1.pack()

gui.bind("<Key>",touche)

gui.mainloop()