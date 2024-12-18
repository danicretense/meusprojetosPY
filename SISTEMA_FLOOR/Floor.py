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
    def conexao_bd():
       conect= mysql.connector.connect(
                host='autorack.proxy.rlwy.net', 
                port=58204,
                user='root',
                password='jzylbuYfAWXBkUwHOTiMDPYmaUXtjFWk', 
                database='railway',
       )
       return conect
    def create_interface():
        def registrando():
            usuario = entrada1.get()
            cd_user = entrada2.get()
            if not usuario or not cd_user.isdigit():
                messagebox.showwarning("FLOOR DIZ:", "Preencha todos os campos corretamente. O código de usuário deve ser numérico.")
                return
            
            cd_user = int(cd_user)

            conexao =conexao_bd()
            cursor = conexao.cursor()
            comando = 'INSERT INTO usuario (nome_user, cd) VALUES (%s, %s)'
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
        def janelinha(id):
             win=tk.Toplevel(root)
             win.resizable(False,False) 
             win.grab_set()
             def block_move(event):   
               win.geometry('190x90+630+300')  
               win.bind('<Configure>', block_move)
             win.geometry('190x90+630+300')  
             win.title("F")
                     
             label_termino=ttk.Label(win,text="TÉRMINO REGISTRADO",font=('Arial',10,'bold'))
             label_termino.place(x=20,y=20)
             
             def baixar():
              conexao = conexao_bd()
              cursor = conexao.cursor()
              comando = 'SELECT entrada, saida, id FROM registro WHERE id_user = %s AND exportado = FALSE'
              cursor.execute(comando, [id])
              resultado = cursor.fetchall()
              for k in resultado:
               entrada = k[0]
               saida = k[1]     
               if not entrada or not saida:
                continue
               entra_format = entrada.strftime('%d/%m/%Y %H:%M:%S')
               sai_format = saida.strftime('%d/%m/%Y %H:%M:%S')
               cabecalho()
               pega_data(entra_format, sai_format, saida, entrada) 
               comando = 'UPDATE registro SET exportado = TRUE WHERE id = %s'
               cursor.execute(comando, (k[2],))
              conexao.commit()
        
              cursor.close()
              conexao.close()
              messagebox.showinfo("FLOOR DIZ:", "Registro(s) exportado(s) com sucesso!")
             
              win.destroy()
             ver_registro = ttk.Button(win, text="BAIXAR REGISTRO", command=baixar)
             ver_registro.place(x=45, y=40)
             win.mainloop()
           
        def comando():
            valor = entry2.get()  
            valor1 = senha.get()
            conexao = conexao_bd()
            cursor = conexao.cursor()
            consulta = 'SELECT * FROM usuario WHERE nome_user = %s AND cd = %s'
            cursor.execute(consulta, (valor, valor1))
            registro = cursor.fetchone()
            if not valor or not valor1:
                messagebox.showwarning("FLOOR DIZ:", "Preencha todos os campos.")
                return
            if registro:
                escolhido = combobox.get()
                id_get=registro[0]  
                if escolhido == "INICIO":
                    data_inicio = datetime.now()
                    comando = 'INSERT INTO registro (id_user,entrada) VALUES (%s,%s)'
                    valores = (id_get,data_inicio)
                    cursor.execute(comando,valores)
                    conexao.commit()
                    messagebox.showinfo("FLOOR DIZ:", "REGISTRADO!")
                else:  
                    data_final = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute('SELECT id FROM registro WHERE saida IS NULL ORDER BY id DESC LIMIT 1')
                    registro_id = cursor.fetchone()
                    if registro_id:
                        comando = 'UPDATE registro SET saida = %s WHERE id = %s'
                        cursor.execute(comando, (data_final, registro_id[0]))
                        conexao.commit()
                        cursor.execute('SELECT entrada, saida FROM registro WHERE id_user = %s AND exportado = FALSE', [id_get])
                        resultado = cursor.fetchall()
                        if resultado:
                         janelinha(id_get)
                        else:
                         messagebox.showwarning("FLOOR DIZ:", "Nenhum registro de término encontrado para exportação.")    
                            
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
                conexao = conexao_bd()
                cursor = conexao.cursor()
                valor = input_recupera.get()
                consulta = 'SELECT * FROM usuario WHERE nome_user = %s'
                cursor.execute(consulta, [valor])
                registro = cursor.fetchone()
                if registro:
                    
                    messagebox.showinfo("FLOOR DIZ:", "USUÁRIO ENCONTRADO")
                    input_recupera.place_forget()
                    procurar.place_forget()
                    input_criar = customtkinter.CTkEntry(janela2, placeholder_text='CRIE SUA NOVA SENHA:',show='*', width=210, height=30)
                    input_criar._set_appearance_mode('light') 
                    input_criar.place(x=160, y=60)  #############################3
                    def salvo():
                        conexao = conexao_bd()
                        cursor = conexao.cursor()
                        new_pass = input_criar.get()
                        
                        if new_pass.isdigit():
                         try:
                           comando = 'UPDATE usuario SET cd = %s WHERE nome_user = %s'
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
            input_recupera.place(x=128, y=60)#----------------------------------

            procurar = customtkinter.CTkButton(janela2, text='PROCURAR', command=procurando)
            procurar.place(x=160, y=110)

            botao_saida = customtkinter.CTkButton(janela2, text='SAIR', command=janela2.destroy)
            botao_saida.place(x=160, y=150)
            janela2.geometry("500x500")  
            janela2.title("ALTERAR SENHA")  
            
        
        root = tk.Tk()
        root.geometry("1994x834")
        root.title("FLOOR")  
        logo_path = resource_path(r"resources/LOGO.png")
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

        senha = ttk.Entry(root,show='*')
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

