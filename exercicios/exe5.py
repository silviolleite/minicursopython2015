__author__ = 'Silvio'

"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada
"""

tabuada = int(input("Qual tabuada deseja imprimir? [1-10] :"))
for i in range(1,11):
    print("{} X {} = {}".format(tabuada,i,tabuada*i))