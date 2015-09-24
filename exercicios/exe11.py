__author__ = 'Silvio'


"""
Crie uma função numero par que permita veriﬁcar um dado número  x  passado como parâmetro é número par
"""


def numero_par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False


numero = int(input("Digite um número maior que zero: "))
if numero_par(numero):
    print("Número é par!")
else:
    print("Número é impar!")
