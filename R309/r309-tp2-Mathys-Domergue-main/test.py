import tkinter as tk
my_w = tk.Tk()
width,height=910,810 # set the variables 
c_width,c_height=width-10,height-65 # canvas width height
d=str(width)+"x"+str(height)
my_w.geometry(d) 
c1 = tk.Canvas(my_w, width=c_width, height=c_height,bg='lightgreen')
c1.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

my_path = tk.PhotoImage(file = "~/Desktop/IUT-cours/R309/r309-tp2-Mathys-Domergue-main/img/client.png") # Update your image path
x1,y1=100,25 # Image position coordinate ( initial )
r1 = c1.create_image(x1,y1,  image=my_path)

def my_callback(event):
    global x1,y1
    step_x=event.x-x1 # Change in x value ( Horizontal)
    step_y=event.y-y1 # Change in y value ( vertical )
    #print(x1,y1)
    c1.move(r1,step_x,step_y) # Move image to new position 
    x1=event.x  # Set the new position as image x coordinate 
    y1=event.y  # Set the new position as image y coordinate

my_w.bind('<B1-Motion>',my_callback) # Mouse left button press and move
my_w.mainloop()