
import semana18 as semana;

print(semana.valor_final)


def cadProd(nome,preco,desconto,precoFinal):
    nome = nome
    preco = preco
    desconto = desconto
    precoFinal = precoFinal
    print(f"Produto criado: {nome}, preco: {preco}, desconto{desconto}, precoFinal{precoFinal}")
# Criando um objeto da classe Produto
produto1 = cadProd("Cadeira",23.5, 0.1, 20.5)
produto2 = cadProd("gabinete",250.5, 0.2, 230.5)
produto3 = cadProd("mouse",75.9, 0.1, 67.9 )


def calculaValorFinal(valorBase,taxaDesconto):
    valorComDesconto = valorBase - (valorBase * (taxaDesconto / 100))
    return valorComDesconto

print(produto1)


# def exibirRecibo(nomeProduto, valorOriginal, valorPago):
#     print(f"nome produto: {nomeProduto},  {}")
