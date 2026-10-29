# funções em python 
# o que é uma função?
"""
Uma função é um bloco de codigo 
criado para realizar uma tarefa
especifica.
EX: a uma receita, porque 
criamos o passo a passo para executar
essa receita sempre que necessario.

vantagens de usar funções
O uso das funções evita
repetição de codigo e 
ajuda a organizar o programa
"""

# um comando para saudação 
# função de saudação

def saudacao():
    print("Olá")
    print("Seja bem vindo")


def saudacao_teste():
    saudacao()

#sintaxe de função
def soma_numeros(n1=1,n2=2):
    soma=n1+n2
    print(soma)

# executar 
soma_numeros()


# toda função possui um fluxo 
# que fluxo seria esse?

# iniciar o programa
# Encontrar a chamada de função(Nome_da_funcao)
# Executar a função (Chamando a função com o "()")
# Retornar ao ponto em que estava
# continua executando o programa

# vantagens 
# reutilização: uma função pode ser chamada varias vezes 
saudacao()
saudacao()
saudacao()
saudacao_teste()
soma_numeros()
# Organização: o programa pode ser lido em partes menores
# legibilidade: nomes claros de funções fica facil acesso e entendimento do que aquele codigo vai fazer
# Manutenção: uma alteração pode ser feita em um unico lugar

# # variaveis em funções
# # parametros e argumentos
# def saudacao_v(nome):
#     print("Olá",nome)

# saudacao_v()



# Returns - Retorno 
# O Return permite que uma função devolva
# o resultado para o programa que a chamou.
# isso é muito util quando realiza um 
# calculo

def somar(a,b):
    resultado = a + b
    return resultado

valor=somar(10,5)
print(valor)


# Escopo de variaveis
# Escopo de variaveis é a região onde 
# uma variavel existe e pode ser acessada.
# variavel Local: é criado dentro de uma função 
# e pertence ao contexto dessa função 
# variavel Global: é criada fora das funções 
# e pode ser acessada por diferentes partes do 
# programa. o seu uso deve ser controlado 
# para evitar efeitos colaterais e dificuldades de manutenção


def calcular_media (nota1,nota2):
    media=(nota1+nota2)/2
    return media

nota1 = 8
nota2 = 6
resultado = calcular_media(nota1,nota2)
print("Média: ",resultado)



def cadastroProd (nome,preco,desconto,precoFinal):
    print()

nome = ""
preco = 0
desconto = 0.1
precoFinal = 0.67













