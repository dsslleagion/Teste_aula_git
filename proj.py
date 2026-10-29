import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.resizable(False, False)
janela.configure(bg="#610c93")

expressao = ""

def adicionar(v):
    global expressao
    expressao += v
    visor.delete(0, tk.END)
    visor.insert(0, expressao)

def calcular():
    global expressao
    try:
        expressao = str(eval(expressao))
        visor.delete(0, tk.END)
        visor.insert(0, expressao)
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")
        expressao = ""

def limpar():
    global expressao
    expressao = ""
    visor.delete(0, tk.END)

visor = tk.Entry(janela, font=("Arial", 18), justify="right")
visor.grid(row=0, column=0, columnspan=4, sticky="nsew")

botoes = [
    "7", "8", "9", "-",
    "4", "5", "6", "+",
    "1", "2", "3", "C",
    "0", "", "=", ""
]

for i, texto in enumerate(botoes):
    if texto == "":
        continue

    comando = calcular if texto == "=" else limpar if texto == "C" else lambda v=texto: adicionar(v)

    tk.Button(
        janela,
        text=texto,
        font=("Arial", 16),
        command=comando,
        bg="#333",
        fg="white",
        bd=1
    ).grid(
        row=i // 4 + 1,
        column=i % 4,
        sticky="nsew"
    )

for coluna in range(4):
    janela.grid_columnconfigure(coluna, weight=1)

for linha in range(1, 5):
    janela.grid_rowconfigure(linha, weight=1)

janela.grid_rowconfigure(0, weight=0)

janela.mainloop()