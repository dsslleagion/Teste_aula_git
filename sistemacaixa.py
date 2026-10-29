def calcularValorFinal(valor_base,taxa_desconto):
    valor_com_desconto = valor_base - (valor_base*(taxa_desconto/100))
    return valor_com_desconto


def exibir_recibo(nome_produto, valor_original, valor_pago):
    economia = valor_original - valor_pago
    print("-----------------------")
    print("Produto: ",nome_produto)
    print(f"Valor original: R${valor_original:.2f}")
    print(f"Valor pago: R${valor_pago:.2f}")
    print(f"Economia: R${economia:.2f}")



#Produto 1
print("\n CADASTRO DE PRODUTO")
nome1 = input("Nome do produto: ")
preco1 = float(input("Preço do produto: "))
desconto1 = float(input("Desconto(%): "))

#Produto 2
print("\n CADASTRO DE PRODUTO")
nome2 = input("Nome do produto: ")
preco2 = float(input("Preço do produto: "))
desconto2 = float(input("Desconto(%): "))

#Produto 3
print("\n CADASTRO DE PRODUTO")
nome3 = input("Nome do produto: ")
preco3 = float(input("Preço do produto: "))
desconto3 = float(input("Desconto(%): "))


# utlizar a função calcular_valor_final
preco_final1 = calcularValorFinal(preco1,desconto1)
preco_final2 = calcularValorFinal(preco2,desconto2)
preco_final3 = calcularValorFinal(preco3,desconto3)

# utiliza a função exibir recibo
exibir_recibo(nome1,preco1,preco_final1)
exibir_recibo(nome2,preco2,preco_final2)
exibir_recibo(nome3,preco3,preco_final3)