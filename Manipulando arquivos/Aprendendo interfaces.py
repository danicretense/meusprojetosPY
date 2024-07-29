import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

# Função para criar a interface
def create_interface():
    # Criação da janela principal
    root = tk.Tk()
    root.geometry("1994x834")  # Define o tamanho da janela (ajuste conforme necessário)
    root.title("FLOOR")
    #image = Image.open("FLOOR.png")
    #image = image.resize((350, 350), Image.Resampling.LANCZOS)  # Redimensionar a imagem (ajuste conforme necessário)
    #photo = ImageTk.PhotoImage(image)
    #image_label = tk.Label(root, image=photo)
    #image_label.place(x=500, y=-15)
    #ADICONANDO COMBO BOX
    options = ["INICIO","TÉRMINO"]
    combobox = ttk.Combobox(root, values=options, state='readonly')
    combobox.place(x=440, y=300, width=500, height=35)
    combobox.set("INICIO")
    # Adicionar o campo de entrada de texto
    entry2 = tk.Entry(root)
    entry2.place(x=440, y=350,width=500, height=35)

    # Adicionar o botão
    butao= ctk.CTkButton(root, text="REGISTRAR")
    butao.place(x=630, y=420)

    # Loop principal da interface gráfica
    root.mainloop()

# Chamar a função para criar a interface
create_interface()
