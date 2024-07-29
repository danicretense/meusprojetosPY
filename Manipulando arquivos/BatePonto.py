import os
import csv
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
def main():
 def covertendo(saida, entrada):
    c1 = datetime.strptime(entrada, '%d/%m/%Y %H:%M')
    diferenca = saida - c1
    return diferenca

 def formatar_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} horas, {minutes} minutos, {seconds} segundos"

 def ponto_entrada(entrada):
    """Guarda a data e horário de entrada no arquivo de texto."""
    with open('entradas.txt', 'w') as guardando:
        guardando.write(entrada)

 def lendo_arquivo():
    """Pega a data e a hora que está guardada na função ponto_entrada."""
    with open('entradas.txt', 'r') as lendo:
        valores = lendo.readline().strip()
    return valores

 def pega_data(data, df):
    """Escreve a data e o horário de entrada e saída no arquivo CSV."""
    diferenca = covertendo(datetime.strptime(df, '%d/%m/%Y %H:%M'), data)
    with open('Folha de ponto.csv', 'a', newline='') as novo:
        escrevendo = csv.writer(novo)
        escrevendo.writerow([data, df, formatar_timedelta(diferenca)])
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
    def comando():
       escolhido=combobox.get()
       if escolhido=="INICIO":
        data = datetime.now()
        data_formatada = data.strftime('%d/%m/%Y %H:%M')
        ponto_entrada(data_formatada)
        label1=tk.Label(root,text="Registrado")
        label1.place(x=630,y=460)
       else:
        da = datetime.now()
        df = da.strftime('%d/%m/%Y %H:%M')
        entrada = lendo_arquivo()
        pega_data(entrada, df)
        diferenca = covertendo(da, entrada)
        formatar_timedelta(diferenca)
        label1=tk.Label(root,text="Registrado")
        label1.place(x=630,y=460)
        os.remove("entradas.txt") 
    # Adicionar o botão
    butao= ctk.CTkButton(root, text="REGISTRAR",command=comando)
    butao.place(x=630, y=420)
    
    
    
    #--------------
    #Adicionando outro botão
    
    
    # Loop principal da interface gráfica
    root.mainloop()
 create_interface()
main()
