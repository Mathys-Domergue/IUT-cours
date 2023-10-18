import tkinter as tk
from tkinter import ttk
def plus():  
    x= label.cget("text")
    x=x+1        
    label.configure(text=x) 
def moins():
    x= label.cget("text")
    x=x-1
    label.configure(text=x)  
root = tk.Tk()
root.geometry('300x300')  


label = tk.Label(root, text=0)
label.pack(pady=20)
buttonplus = tk.Button(root, text="+", command=plus)
buttonmoins = tk.Button(root, text="-", command=moins)
buttonplus.pack()
buttonmoins.pack()
root.mainloop()
