
import tkinter as tk
from tkinter import ttk
def plus():  
    x=int(label['text']) 
    x=x+1        
    label.configure(text=str(x)) 
def moins():
    x=int(label['text'])
    x=x-1
    label.configure(text=str(x))  
gui = tk.Tk()
gui.geometry('300x100')  
label = tk.Label(gui, text="0")
label.pack(pady=20)
buttonplus = tk.Button(gui, text="+", command=plus)
buttonmoins = tk.Button(gui, text="-", command=moins)
buttonplus.pack()
buttonmoins.pack()
gui.mainloop()

#https://github.com/IUT-Beziers/r309-tp1-Adrien-BOURLANGES-GABARRE


