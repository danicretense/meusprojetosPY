import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
def testando():
 pass
# Função para criar a interface
def create_interface():
    # Criação da janela principal
    root = tk.Tk()
    root.geometry("1994x834")  # Define o tamanho da janela (ajuste conforme necessário)
    root.title("FLOOR")
    image = Image.open("LOGO.png")
    image = image.resize((300, 300), Image.Resampling.LANCZOS)  # Redimensionar a imagem (ajuste conforme necessário)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.place(x=550, y=-20)
    #ADICONANDO COMBO BOX
    options = ["INICIO","TÉRMINO"]
    combobox = ttk.Combobox(root, values=options, state='readonly')
    combobox.place(x=440, y=300, width=500, height=35)
    combobox.set("INICIO")
    # Adicionar o campo de entrada de texto
    entry2 = tk.Entry(root)
    entry2.place(x=440, y=350,width=500, height=35)
    def primeiro_comando():
      t=combobox.get()
      if t=="INICIO": 
       label=tk.Label(root,text="REGISTRADO!")
       label.place(x=630,y=460)  
    
    # Adicionar o botão
    butao= ctk.CTkButton(root, text="REGISTRAR",command=primeiro_comando)
    butao.place(x=630, y=420)
    #--------------
    #Adicionando outro botão
    
    #butao._command=testando
    # Loop principal da interface gráfica
    root.mainloop()

# Chamar a função para criar a interface
create_interface()
