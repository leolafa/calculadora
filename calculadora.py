import tkinter as tk #biblioteca grafica
from tkinter import messagebox

# Função de conversão, binario para decimal
def bin_to_dec():
    bin_num = entry_input.get() #"pega" o texto digitado na caixa
    try:
        #verifica se tem apenas 0 e 1
        if not set(bin_num).issubset({'0', '1'}):
            raise ValueError(" O número deve conter apenas 0 ou 1!")
        dec_num = int(bin_num, 2) #converte binario para decimal, por meio da base 2    
        label_result.config(text=f" Decimal: {dec_num}") #exibe resultado
    except ValueError as e:
        messagebox.showerror("Erro", str(e)) #mensagem de erro 
#Função de conversão, decimal para binario
def dec_to_bin():
    dec_num = entry_input.get() #pega o texto digitado na caixa
    try:
        dec_int = int(dec_num) #converte para um numero inteiro
        if dec_int < 0:
            raise ValueError(" Apenas números positivos!")
        bin_num = bin(dec_int)[2:] #converte de binario para decimal
        label_result.config(text=f"Binário: {bin_num}") #mostra resultado
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Criação da janela
root = tk.Tk()
root.title("Calculadora em python") #titulo da janela
root.geometry("400x300") #tamanho
root.configure(bg="#E0F7FA") #cor do fundo

# Título
label_title = tk.Label(root, text="Conversor Binário 🔁 Decimal", font=("Comic Sans MS", 16, "bold"), bg="#E0F7FA", fg="#00796B")
label_title.pack(pady=10)

# Campo de entrada
entry_input = tk.Entry(root, font=("Comic Sans MS", 14), width=20, justify="center")
entry_input.pack(pady=10)

# Botões
btn_frame = tk.Frame(root, bg="#E0F7FA")
btn_frame.pack(pady=10)
#Botão binario para decimal
btn_bin_to_dec = tk.Button(btn_frame, text="➡️ Binário → Decimal", font=("Comic Sans MS", 12), bg="#81D4FA", fg="#004D40", command=bin_to_dec)
btn_bin_to_dec.grid(row=0, column=0, padx=10)
#Botão decimal para binario
btn_dec_to_bin = tk.Button(btn_frame, text="⬅️ Decimal → Binário", font=("Comic Sans MS", 12), bg="#FFCC80", fg="#4E342E", command=dec_to_bin)
btn_dec_to_bin.grid(row=0, column=1, padx=10)

# Resultado
label_result = tk.Label(root, text="", font=("Comic Sans MS", 14), bg="#E0F7FA", fg="#00695C")
label_result.pack(pady=20)

# Rodapé
label_footer = tk.Label(root, text="Feito por leonardo lafayette em Python + Tkinter", font=("Comic Sans MS", 10), bg="#E0F7FA", fg="#00796B")
label_footer.pack(side="bottom", pady=5)

# Executa a aplicação
root.mainloop()
