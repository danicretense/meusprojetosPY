import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

def main():
    def cabecalho():
        with open('Folha de ponto.csv', 'w', newline='') as file:
            cabecalho_ = csv.writer(file)
            cabecalho_.writerow(["INICIO", "TERMINO", "TEMPO ESTUDADO"])

    cabecalho()
    def covertendo(saida, entrada):
        c1 = datetime.strptime(entrada, '%d/%m/%Y %H:%M:%S')
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
        diferenca = covertendo(datetime.strptime(df, '%d/%m/%Y %H:%M:%S'), data)
        with open('Folha de ponto.csv', 'a', newline='') as novo:
            csv.register_dialect('my_dialect', delimiter=';')
            escrevendo = csv.writer(novo, dialect='my_dialect')
            escrevendo.writerow([data, df, formatar_timedelta(diferenca)])

    def create_interface():
        # Função para registrar o usuário
        def registrando():
            usuario = entrada1.get()
            cd_user = entrada2.get()
            if not usuario or not cd_user:
                messagebox.showwarning("FLOOR DIZ:", "Preencha todos os campos.")
                return

            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='765FHJyjd$_@',
                database='db_floor',
            )
            cursor = conexao.cursor()

            comando = 'INSERT INTO usuarios (nome_user, cd) VALUES (%s, %s)'
            valores = (usuario, cd_user)
            
            try:
                cursor.execute(comando, valores)
                conexao.commit()
                messagebox.showinfo("FLOOR DIZ:", "Usuário criado com sucesso!")
            except mysql.connector.Error as err:
                messagebox.showerror("FLOOR DIZ:", f"Erro: {err}")
            finally:
                cursor.close()
                conexao.close()

        # Função para o comando de registro de entrada/saída
        def comando():
            valor = entry2.get()
            #valor1= senha.get()
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='765FHJyjd$_@',
                database='db_floor',
            )
            cursor = conexao.cursor()
            consulta = 'SELECT * FROM usuarios'
            cursor.execute(consulta)
            registros = cursor.fetchall()
            cursor.close()
            conexao.close()

            for i in registros:
                registro_user = i[1]
               
                if valor==registro_user:
                    escolhido = combobox.get()
                    if escolhido == "INICIO":
                        data = datetime.now()
                        data_formatada = data.strftime('%d/%m/%Y %H:%M:%S')
                        ponto_entrada(data_formatada)
                        messagebox.showinfo("FLOOR DIZ: ", "REGISTRADO!")
                    else:
                        da = datetime.now()
                        df = da.strftime('%d/%m/%Y %H:%M:%S')
                        entrada = lendo_arquivo()
                        pega_data(entrada, df)
                        diferenca = covertendo(da, entrada)
                        formatar_timedelta(diferenca)
                        messagebox.showinfo("FLOOR DIZ:", "REGISTRADO!")
                        os.remove("entradas.txt")
                    return
            messagebox.showinfo("FLOOR DIZ:", "USUARIO NÃO ENCONTRADO")

        def voltar():
            combobox.place(x=440, y=300, width=500, height=35)
            entry2.place(x=440, y=370, width=500, height=35)
            butao.place(x=630, y=500)
            cria_user.place(x=630, y=580)
            butao_sair.place(x=650, y=540)
            digite_user.place(x=440,y=350)
            escolha_entrada.place(x=440,y=280)
            label_pass.place(x=440,y=420)
            senha.place(x=440,y=440,width=500,height=35)
            entrada1.place_forget()
            entrada2.place_forget()
            bt_voltar.place_forget()
            criando.place_forget()

        def janela_registro():
            combobox.place_forget()
            entry2.place_forget()
            butao.place_forget()
            cria_user.place_forget()
            escolha_entrada.place_forget()
            digite_user.place_forget()
            label_pass.place_forget()
            senha.place_forget()
            entrada1.place(x=440, y=300)
            entrada1._set_appearance_mode('light')
            entrada2.place(x=440, y=350)
            entrada2._set_appearance_mode('light')
            criando.place(x=630, y=420)
            bt_voltar.place(x=630, y=460)
            butao_sair.place(x=650, y=500)
        
        def fechar_janela_principal():
            root.destroy()

        # Criação da janela principal
        root = tk.Tk()
        root.geometry("1994x834")  # Define o tamanho da janela (ajuste conforme necessário)
        root.title("FLOOR")
        image = Image.open("LOGO.png")
        image = image.resize((300, 300), Image.Resampling.LANCZOS)  # Redimensionar a imagem (ajuste conforme necessário)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(root, image=photo)
        image_label.place(x=550, y=-20)
        #Adicionando Label
        escolha_entrada=ttk.Label(root,text="TIPO DE ENTRADA: ")
        escolha_entrada.place(x=440,y=280)
        # Adicionando combo box
        options = ["INICIO", "TÉRMINO"]
        combobox = ttk.Combobox(root, values=options, state='readonly')
        combobox.place(x=440, y=300, width=500, height=35)
        combobox.set("INICIO")
        #Adicionando outro Label
        digite_user=ttk.Label(root,text="DIGITE SEU USUÁRIO: ")
        digite_user.place(x=440,y=350)
        # Adicionar o campo de entrada de texto
        entry2 = ttk.Entry(root)
        entry2.place(x=440, y=370, width=500, height=35)
        #Label pedindo senha
        label_pass= ttk.Label(root,text="DIGITE SEU CÓDIGO DE USUÁRIO: ")
        label_pass.place(x=440,y=420)
        #Entrada Para senha
        senha=ttk.Entry(root)
        senha.place(x=440,y=440,width=500,height=35)
        # Adicionar o botão
        butao = customtkinter.CTkButton(root, text="REGISTRAR", command=comando)
        butao.place(x=630, y=500)

        # Adicionando outros botões
        butao_sair = customtkinter.CTkButton(root, text='SAIR', command=fechar_janela_principal, width=100)
        butao_sair.place(x=650, y=540)

        cria_user = customtkinter.CTkButton(root, text="CRIAR USUÁRIO", command=janela_registro)
        cria_user.place(x=630, y=580)

        entrada1 = customtkinter.CTkEntry(root, placeholder_text='DIGITE SEU NOME: ', width=500, height=35)
        entrada2 = customtkinter.CTkEntry(root, placeholder_text='CRIE SEU CÓDIGO DE USUARIO: ', width=500, height=35)
        bt_voltar = customtkinter.CTkButton(root, text="VOLTAR", command=voltar)
        criando = customtkinter.CTkButton(root, text='SALVAR', command=registrando)

        root.mainloop()
    
    create_interface()

main()
