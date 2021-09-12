from tkinter import *
from tkinter import ttk
from time import sleep

root = Tk()

b_tk = Button(text = 'Hello tk')
b_ttk = ttk.Button(text = 'Hello ttk')

b_tk.pack()
b_ttk.pack()


b_tk.config(background = '#b00', foreground = '#fff')


style = ttk.Style()
style.configure('TButton', background = '#0b0', foreground = '#fff')


root.mainloop()