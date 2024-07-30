import tkinter as tk

# Função que será chamada após o atraso
def callback():
    print("Ação agendada foi executada!")

# Função para cancelar a ação agendada
def cancel_callback():
    root.after_cancel(after_id)
    print("Ação agendada foi cancelada!")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de after_cancel")
root.geometry("300x150")

# Agendando a execução da função callback após 5000 milissegundos (5 segundos)
after_id = root.after(5000, callback)

# Botão para cancelar a ação agendada
cancel_button = tk.Button(root, text="Cancelar Ação", command=cancel_callback)
cancel_button.pack(pady=20)

# Execução da janela principal
root.mainloop()
