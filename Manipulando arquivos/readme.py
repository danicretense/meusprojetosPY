import tkinter as tk

# Função que será chamada quando o evento ocorrer
def on_key_press(event):
    print(f"Tecla pressionada: {event.keysym}")

# Função para remover o binding do evento
def remove_event():
    widget.event_delete("<<CustomKeyEvent>>")
    print("Evento personalizado removido.")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de event_delete")
root.geometry("300x150")

# Criação de um widget (um campo de entrada, por exemplo)
widget = tk.Entry(root)
widget.pack(pady=20)

# Adicionando um evento personalizado
widget.event_add("<<CustomKeyEvent>>", "<KeyPress>")

# Binding do evento personalizado a uma função
widget.bind("<<CustomKeyEvent>>", on_key_press)

# Botão para remover o binding do evento personalizado
remove_button = tk.Button(root, text="Remover Evento", command=remove_event)
remove_button.pack(pady=10)

# Execução da janela principal
root.mainloop()
