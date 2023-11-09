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
    global x1,y1
    step_x=event.x-x1 # Change in x value ( Horizontal)
    step_y=event.y-y1 # Change in y value ( vertical )
    #print(x1,y1)
    c1.move(r1,step_x,step_y) # Move image to new position 
    x1=event.x  # Set the new position as image x coordinate 
    y1=event.y  # Set the new position as image y coordinate


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
