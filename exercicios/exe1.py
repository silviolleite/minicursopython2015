__author__ = 'Silvio'

"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
numero1 = int(input("Entre com o 1º número: "))
numero2 = int(input("Entre com o 2º número: "))
numero3 = int(input("Entre com o 3º número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é o 1º número que vale ", numero1)
elif numero2 > numero3:
    print("O maior número é o 2º número que vale ", numero2)
else:
    print("O maior número é o 3º número que vale ", numero3)