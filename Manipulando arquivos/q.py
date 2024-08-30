import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
win=tk.Tk()
win.geometry('190x90')
win.title("FLOOR")
label_termino=ttk.Label(win,text="TÉRMINO REGISTRADO",font=('Arial',10,'bold'))
label_termino.place(x=20,y=20)
ver_registro=ttk.Button(win,text="VER REGISTRO").place(x=45,y=40)
win.mainloop()