__author__ = 'Silvio'

"""
Faça um programa que leia 5 números e informe o maior número.
"""

for i in range(5):
    numero = int(input("Digite o {}º número: ".format(i+1)))
    if i == 0:
        maior = numero
    else:
        if numero > maior:
            maior = numero
print("O maior número digitado foi: ", maior)