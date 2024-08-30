import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import sys

def resource_path(relative_path):
    """Obtenha o caminho absoluto ao recurso, trabalhando para desenvolvimento e compilado"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    
    def cabecalho():
        if not os.path.exists('Folha de ponto.csv') or os.path.getsize('Folha de ponto.csv') == 0:
            with open('Folha de ponto.csv', 'w', newline='') as file:
                csv.register_dialect('my_dialect', delimiter=';')
                cabecalho_ = csv.writer(file, dialect='my_dialect')
                cabecalho_.writerow(["INICIO", "TERMINO", "TEMPO ESTUDADO"])
    
    cabecalho()
    
    def calculando(saida, entrada):
        diferenca = saida - entrada
        return diferenca

    def formatar_timedelta(td):
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours} horas, {minutes} minutos, {seconds} segundos"

    def pega_data(data, df, s, e):
        diferenca = calculando(s, e)
        with open('Folha de ponto.csv', 'a', newline='') as novo:
            csv.register_dialect('my_dialect', delimiter=';')
            escrevendo = csv.writer(novo, dialect='my_dialect')
            escrevendo.writerow([data, df, formatar_timedelta(diferenca)])

    def create_interface():
        def registrando():
            usuario = entrada1.get()
            cd_user = entrada2.get()
            if not usuario or not cd_user.isdigit():
                messagebox.showwarning("FLOOR DIZ:", "Preencha todos os campos corretamente. O código de usuário deve ser numérico.")
                return
            
            cd_user = int(cd_user)

            conexao = mysql.connector.connect(
                host='autorack.proxy.rlwy.net', 
                port=35695,
                user='root',
                password='HwxRPcthWWGmOcfLZsiyBTpeKlKewPkf', 
                database='railway',  
            )
        
            cursor = conexao.cursor()

            comando = 'INSERT INTO tabela_usuarios (nome_user, cd) VALUES (%s, %s)'
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
                host='autorack.proxy.rlwy.net',
                user='root',
                port=35695,
                password='HwxRPcthWWGmOcfLZsiyBTpeKlKewPkf',
                database='railway',
            )
            cursor = conexao.cursor()
            consulta = 'SELECT * FROM tabela_usuarios WHERE nome_user = %s AND cd = %s'
            cursor.execute(consulta, (valor, valor1))
            registro = cursor.fetchone()
            if not valor or not valor1:
                messagebox.showwarning("FLOOR DIZ:", "Preencha todos os campos.")
                return
            if registro:
                escolhido = combobox.get()  
                if escolhido == "INICIO":
                    data_inicio = [datetime.now()]
                    comando = 'INSERT INTO tabela_registros (entradas) VALUES (%s)'
                    valores = data_inicio
                    cursor.execute(comando, valores)
                    conexao.commit()
                    messagebox.showinfo("FLOOR DIZ:", "REGISTRADO!")
                else:  
                    data_final = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute('SELECT id FROM tabela_registros WHERE saidas IS NULL ORDER BY id DESC LIMIT 1')
                    registro_id = cursor.fetchone()
                    if registro_id:
                        comando = 'UPDATE tabela_registros SET saidas = %s WHERE id = %s'
                        cursor.execute(comando, (data_final, registro_id[0]))
                        conexao.commit()
                        messagebox.showinfo("FLOOR DIZ:", "TÉRMINO REGISTRADO!")
                        

                        comando = 'SELECT * FROM tabela_registros WHERE exportado = FALSE'
                        cursor.execute(comando)
                        en_sa = cursor.fetchall()
                        for k in en_sa:
                            entrada = k[1]
                            saida = k[2]     
                            if not entrada or not saida:
                                continue
                            entra_format = entrada.strftime('%d/%m/%Y %H:%M:%S')
                            sai_format = saida.strftime('%d/%m/%Y %H:%M:%S')
                            pega_data(entra_format, sai_format, saida, entrada) 
                            #pega_id=registro[0]
                           # ver_registro= ttk.Button(root,text='VER MEU REGISTRO',command=lambda:registros(pega_id))
                            comando = 'UPDATE tabela_registros SET exportado = TRUE WHERE id = %s'
                            cursor.execute(comando, (k[0],))
                            conexao.commit()
                            
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
            recupera_senha.place(x=640, y=610)
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
            recupera_senha.place_forget()
        
        def fechar_janela_principal():
            root.destroy()

        def nova_janela(event):  
            janela2 = tk.Toplevel(root)  
            janela2.grab_set() 
            
            
            def procurando():
                conexao = mysql.connector.connect(
                    host='autorack.proxy.rlwy.net',
                    user='root',
                    port=35695,
                    password='HwxRPcthWWGmOcfLZsiyBTpeKlKewPkf',
                    database='railway',
                )
                cursor = conexao.cursor()
                valor = input_recupera.get()
                consulta = 'SELECT * FROM tabela_usuarios WHERE nome_user = %s'
                cursor.execute(consulta, [valor])
                registro = cursor.fetchone()
                if registro:
                    messagebox.showinfo("FLOOR DIZ:", "USUÁRIO ENCONTRADO")
                    input_recupera.place_forget()
                    procurar.place_forget()
                    input_criar = customtkinter.CTkEntry(janela2, placeholder_text='CRIE SUA NOVA SENHA:', width=210, height=30)
                    input_criar._set_appearance_mode('light') 
                    input_criar.place(x=160, y=60)  #############################3
                    def salvo():
                        conexao = mysql.connector.connect(
                      host='autorack.proxy.rlwy.net',
                      user='root',
                      port=35695,
                      password='HwxRPcthWWGmOcfLZsiyBTpeKlKewPkf',
                      database='railway',
                      )
                        cursor = conexao.cursor()
                        new_pass = input_criar.get()
                        
                        if new_pass.isdigit():
                         try:
                           comando = 'UPDATE tabela_usuarios SET cd = %s WHERE nome_user = %s'
                           cursor.execute(comando, [new_pass, valor])
                           conexao.commit()
                           messagebox.showinfo("FLOOR DIZ:", "Senha alterada com sucesso")
                         except mysql.connector.Error as err:
                          messagebox.showerror("FLOOR DIZ:", f"Erro: {err}")
                         finally:
                          cursor.close()
                          conexao.close()
                          janela2.destroy()
                        else:
                         messagebox.showwarning("FLOOR DIZ:", "A senha deve conter apenas números.")

                    criar = customtkinter.CTkButton(janela2, text='SALVAR',command=salvo)
                    criar.place(x=160, y=110)
                else:
                    messagebox.showerror("FLOOR DIZ:", "Usuário não encontrado")
                cursor.close()
                conexao.close()

            input_recupera = customtkinter.CTkEntry(janela2, placeholder_text='DIGITE SEU USUÁRIO:', width=210, height=30)
            input_recupera._set_appearance_mode('light') 
            input_recupera.place(x=130, y=60)#----------------------------------

            procurar = customtkinter.CTkButton(janela2, text='PROCURAR', command=procurando)
            procurar.place(x=160, y=110)

            botao_saida = customtkinter.CTkButton(janela2, text='SAIR', command=janela2.destroy)
            botao_saida.place(x=160, y=150)
            janela2.geometry("500x500")  
            janela2.title("ALTERAR SENHA")  
            

        root = tk.Tk()
        root.geometry("1994x834")
        root.title("FLOOR")

        logo_path = resource_path("resources/LOGO.png")
        image = Image.open(logo_path)
        image = image.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(root, image=photo)
        image_label.image = photo  # Mantém a referência à imagem
        image_label.place(x=550, y=-20)

        escolha_entrada = ttk.Label(root, text="TIPO DE ENTRADA::")
        escolha_entrada.place(x=440, y=280)

        combobox = ttk.Combobox(root, values=["INICIO", "TERMINO"], state="readonly")
        combobox.place(x=440, y=300, width=500, height=35)
        combobox.set("INICIO")
        digite_user = ttk.Label(root, text="DIGITE O SEU USUARIO:")
        digite_user.place(x=440, y=350)

        entry2 = ttk.Entry(root)
        entry2.place(x=440, y=370,width=500, height=35)

        label_pass = ttk.Label(root, text="DIGITE SEU CODIGO DE USUÁRIO:")
        label_pass.place(x=440, y=420)

        senha = ttk.Entry(root)
        senha.place(x=440, y=440,width=500, height=35)

        butao = customtkinter.CTkButton(root, text="REGISTRAR" ,command=comando)
        butao.place(x=630, y=500)

        cria_user = customtkinter.CTkButton(root, text="CRIAR USUÁRIO", command=janela_registro)
        cria_user.place(x=630, y=580)

        butao_sair = customtkinter.CTkButton(root, text="SAIR", command=fechar_janela_principal,width=100)
        butao_sair.place(x=650, y=540)
         
        recupera_senha = ttk.Label(root, text='ESQUECI A SENHA', font=('Arial', 9, "underline"))
        recupera_senha.place(x=640, y=610)
        recupera_senha.bind("<Button-1>", nova_janela)
        
        entrada1 = customtkinter.CTkEntry(root, placeholder_text="Digite o nome de usuário:", width=500, height=35)
        entrada2 = customtkinter.CTkEntry(root, placeholder_text="Crie um código de usuário (Apenas números):", show="*", width=500, height=35)

        criando = customtkinter.CTkButton(root, text="CRIAR",command=registrando)
        bt_voltar = customtkinter.CTkButton(root, text="VOLTAR", command=voltar)
        root.mainloop()
        
        

    create_interface()
    
main() 

