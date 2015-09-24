__author__ = 'Silvio'


"""
Monte um programa onde o usuário entra com 1 número decimal e o programa imprime a conversão em Binário, Hexadecimal, Octal e Caractere da tabela ASCII .

"""

numero = int(input("Entre com um número decimal: "))
print("Bin: {0:b}, Hex: {0:x}, Oct: {0:o}, Caractere: {0:c}".format(numero))