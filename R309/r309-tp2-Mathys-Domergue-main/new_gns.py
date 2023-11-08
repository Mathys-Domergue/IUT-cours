from tkinter import *
from PIL import Image

gui = Tk()
gui.title("Votre plan réseau")
gui.geometry("600x540")

img_cliq = ""
def choix(val):
	global img_cliq
	if val == 1:
		img_cliq = img1
	elif val == 2:
		img_cliq = img2
	elif val == 3:
		img_cliq = img3
	
def keydown(e):
	if e.char == "c":
		print("Ordinateur")
		can.create_image(e.x-10,e.y-20,image=img1)
	elif e.char == "s":
		print("Switch")
		can.create_image(e.x-10,e.y-20,image=img2)
	elif e.char == "r":
		print("Routeur")
		can.create_image(e.x-10,e.y-20,image=img3)
		
	
  
def delete(event):
    x=event.x
    y=event.y
    t=can.find_closest(x, y)
    if t:
        can.delete(t[0])
    



		
old=[None, None]

def clic(event):
    old[0]=event.x
    old[1]=event.y

def glisser(event):
    can.move(img1, event.x-old[0], event.y-old[1])
    old[0]=event.x
    old[1]=event.y


lg, ht = 600,540
can=Canvas(gui,bg="ivory",width=lg,height=ht)
can.pack(side='bottom', padx=20, pady=40)

img1 = PhotoImage(file = '~/Desktop/IUT-cours/R309/r309-tp2-Mathys-Domergue-main/img/client.png')
img2 = PhotoImage(file = '~/Desktop/IUT-cours/R309/r309-tp2-Mathys-Domergue-main/img/switch.png')
img3 = PhotoImage(file = '~/Desktop/IUT-cours/R309/r309-tp2-Mathys-Domergue-main/img/routeur.png')

gui.resizable(False,False)
gui.bind("<KeyPress>", keydown)
gui.bind("<Key-BackSpace>", delete)
gui.bind("<B1-Motion>",glisser)
gui.bind("<Button-1>",clic)

gui.mainloop()
