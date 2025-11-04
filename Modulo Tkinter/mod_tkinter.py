import tkinter as tk

# Criar a janela
window = tk.Tk()
window.geometry("300x200")
window.title("Gerencia frases")

# Adiciona frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# Adicionando Label
label = tk.Label(frame, text="Olá mundo")
label.pack(fill="x", expand=True)

# Adicionando input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill="x", expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill="x", expand=True)

# Cria uma funcao para alterar o texto do label
def click():
    label.config(text=frase_inp.get())

# Adc botao
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()