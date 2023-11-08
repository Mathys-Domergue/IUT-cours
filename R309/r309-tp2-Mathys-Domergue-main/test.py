from tkinter import *
from PIL import Image

gui = Tk()
gui.title("Votre plan réseau")
gui.geometry("720x360")
cnv = Canvas(gui, width=720, height=360)
cnv.pack()

img_cliq = ""
def choix(val):
	global img_cliq
	if val == 1:
		img_cliq = img1

	
def keydown(e):
	if e.char == "c":
		print("Ordinateur")
		cnv.create_image(e.x-10,e.y-20,image=img1)

old=[None, None]

def clic(event):
    old[0]=event.x
    old[1]=event.y

def glisser(event):
    cnv.move(img_cliq, event.x-old[0], event.y-old[1])
    old[0]=event.x
    old[1]=event.y

img1 = PhotoImage(file = '~/Desktop/IUT-cours/R309/r309-tp2-Mathys-Domergue-main/img/client.png')

gui.bind("<KeyPress>", keydown)
cnv.bind("<B1-Motion>",glisser)
cnv.bind("<Button-1>",clic)

gui.mainloop()