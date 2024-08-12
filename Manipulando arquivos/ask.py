import tkinter as tk

def on_click():
    print("Texto clicado!")

root = tk.Tk()

label = tk.Label(root, text="Clique aqui", fg="blue", cursor="hand2")
label.pack()

# Associar uma função ao evento de clique
label.bind("<Button-1>", lambda e: on_click())

root.mainloop()
