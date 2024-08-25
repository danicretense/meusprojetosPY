import tkinter as tk
from tkinter import simpledialog

def open_secondary_window():
    # Cria uma nova janela
    secondary_window = tk.Toplevel(root)
    secondary_window.title("Janela Secundária")
    secondary_window.geometry("300x200")

    # Desabilita a janela principal enquanto a secundária está aberta
    secondary_window.grab_set()

    # Adiciona um botão para fechar a janela secundária
    close_button = tk.Button(secondary_window, text="Fechar", command=secondary_window.destroy)
    close_button.pack(pady=50)

# Criação da janela principal
root = tk.Tk()
root.title("Janela Principal")
root.geometry("300x200")

# Botão para abrir a janela secundária
open_button = tk.Button(root, text="Abrir Janela Secundária", command=open_secondary_window)
open_button.pack(pady=50)

# Inicia o loop da aplicação
root.mainloop()
