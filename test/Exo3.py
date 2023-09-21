from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ma page nulle")
root.geometry("360x360")

lg, ht = 320, 320
dessin=Canvas(root,bg="ivory",width=lg,height=ht)
dessin.pack(side='left', padx=20, pady=20)

j= 0
while j < 8:
	if j%2 == 0:
		i= 1
	else:
		i = 0
	while i < 9:
		dessin.create_rectangle(40*i,40*j,40*i+40,40*j+40,fill="black")
		i += 2
	j+=1

root.mainloop()
