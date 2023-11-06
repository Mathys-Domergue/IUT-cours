import tkinter as tk
from tkinter import *
def plus():  
    x= label.cget("text")
    x=x+1        
    label.configure(text=x) 
def moins():
    x= label.cget("text")
    x=x-1
    label.configure(text=x)  
root = tk.Tk()
root.geometry('150x150')  

root.resizable(False,False)
label = tk.Label(root, text=0)
label.pack(pady=20)
buttonplus = tk.Button(root, text="+", command=plus)
buttonmoins = tk.Button(root, text="-", command=moins)
buttonplus.pack(side= LEFT)
buttonmoins.pack(side=RIGHT)
root.mainloop()
