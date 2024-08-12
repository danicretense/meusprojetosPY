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
            csv.register_dialect('my_dialect', delimiter=';')
            cabecalho_ = csv.writer(file, dialect='my_dialect')
            cabecalho_.writerow(["INICIO", "TERMINO", "TEMPO ESTUDADO"])

    def calculando(saida, entrada):
        diferenca = saida - entrada
        return diferenca

    def formatar_timedelta(td):
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours} horas, {minutes} minutos, {seconds} segundos"

    

    def pega_data(data, df,s,e):
        diferenca= calculando(s,e)
        with open('Folha de ponto.csv', 'a', newline='') as novo:
            csv.register_dialect('my_dialect', delimiter=';')
            escrevendo = csv.writer(novo, dialect='my_dialect')
            escrevendo.writerow([data, df, formatar_timedelta(diferenca)])

    def create_interface():
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

        def comando():
            valor = entry2.get()
            valor1 = senha.get()
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='765FHJyjd$_@',
                database='db_floor',
            )
            cursor = conexao.cursor()
            consulta = 'SELECT * FROM usuarios WHERE nome_user = %s AND cd = %s'
            cursor.execute(consulta, (valor, valor1))
            registro = cursor.fetchone()
            if not valor or not valor1:
                messagebox.showwarning("FLOOR DIZ:", "Preencha todos os campos.")
                return
            if registro:
                escolhido = combobox.get()  
                if escolhido == "INICIO":
                    data_inicio = [datetime.now()]
                    comando = 'INSERT INTO registros (entradas) VALUES (%s)'
                    valores = data_inicio
                    cursor.execute(comando, valores)
                    conexao.commit()
                    messagebox.showinfo("FLOOR DIZ:", "REGISTRADO!")
                else:
                    data_final = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute('SELECT id FROM registros WHERE saidas IS NULL ORDER BY id DESC LIMIT 1')
                    registro_id = cursor.fetchone()
                    if registro_id:
                     comando = 'UPDATE registros SET saidas = %s WHERE id = %s'
                     cursor.execute(comando, (data_final, registro_id[0]))
                     conexao.commit()
                     messagebox.showinfo("FLOOR DIZ:", "TÉRMINO REGISTRADO!")
                     comando= 'SELECT *FROM registros'
                     cursor.execute(comando)
                     en_sa=cursor.fetchall()
                     for k in en_sa:
                         entrada=k[1]
                         saida=k[2]
                         entra_format=entrada.strftime('%d/%m/%Y %H:%M:%S')
                         sai_format=saida.strftime('%d/%m/%Y %H:%M:%S')
                         pega_data(entra_format,sai_format,saida,entrada)
                    else:
                     messagebox.showwarning("FLOOR DIZ:", "Nenhum registro de início encontrado.")

            else:
                messagebox.showinfo("FLOOR DIZ:", "USUÁRIO NÃO ENCONTRADO")
            cursor.close()
            conexao.close()

        def voltar():
            combobox.place(x=440, y=300, width=500, height=35)
            entry2.place(x=440, y=370, width=500, height=35)
            butao.place(x=630, y=500)
            cria_user.place(x=630, y=580)
            butao_sair.place(x=650, y=540)
            digite_user.place(x=440, y=350)
            escolha_entrada.place(x=440, y=280)
            label_pass.place(x=440, y=420)
            senha.place(x=440, y=440, width=500, height=35)
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

        root = tk.Tk()
        root.geometry("1994x834")
        root.title("FLOOR")
        image = Image.open("LOGO.png")
        image = image.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(root, image=photo)
        image_label.place(x=550, y=-20)
        
        escolha_entrada = ttk.Label(root, text="TIPO DE ENTRADA: ")
        escolha_entrada.place(x=440, y=280)
        options = ["INICIO", "TÉRMINO"]
        combobox = ttk.Combobox(root, values=options, state='readonly')
        combobox.place(x=440, y=300, width=500, height=35)
        combobox.set("INICIO")
        
        digite_user = ttk.Label(root, text="DIGITE SEU USUÁRIO: ")
        digite_user.place(x=440, y=350)
        
        entry2 = ttk.Entry(root)
        entry2.place(x=440, y=370, width=500, height=35)
        
        label_pass = ttk.Label(root, text="DIGITE SEU CÓDIGO DE USUÁRIO: ")
        label_pass.place(x=440, y=420)
        
        senha = ttk.Entry(root)
        senha.place(x=440, y=440, width=500, height=35)
        
        butao = customtkinter.CTkButton(root, text="REGISTRAR", command=comando)
        butao.place(x=630, y=500)

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
