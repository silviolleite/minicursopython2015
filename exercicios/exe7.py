__author__ = 'Silvio'

"""
Crie um dicionário e armazene nele os seus dados: nome, idade, telefone, endereço. Imprima todos os dados usando o padrão chave: valor.

"""

dados = {}
dados["nome"] = input("Digite o seu nome: ")
dados["idade"] = int(input("Digite a sua idade: "))
dados["telefone"] = input("Digite o seu telefone: ")
dados["endereco"] = input("Digite o seu endereço: ")

for chave,valor in dados.items():
    print("{}: {}".format(chave, valor))
