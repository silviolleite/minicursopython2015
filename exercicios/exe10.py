__author__ = 'Silvio'

"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo

"""


def verificaNumero(valor):
    if valor > 0:
        return "P"
    else:
        return "N"


numero = int(input("Digite um número: "))
print(verificaNumero(numero))
