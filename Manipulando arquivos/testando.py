import tkinter as tk

def minha_funcao(arg):
    print(f"Argumento recebido: {arg}")

root = tk.Tk()

botao = tk.Button(root, text="Clique aqui", command=lambda: minha_funcao("Olá, mundo!"))
botao.pack()

root.mainloop()
