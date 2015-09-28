__author__ = 'Silvio'

def soma(a,b):
    return a+b

def subtrai(a,b):
    return a-b

def mutiplica(a,b):
    return a*b

def divide(a,b):
    return a/b

def calcula(op,a,b):
    if op == "+":
        return soma(a,b)
    elif op == "-":
        return subtrai(a,b)
    elif op == "*":
        return mutiplica(a,b)
    elif op == "/":
        return divide(a,b)
    else:
        return "Operação inválida!"


operacao = input("Qual operação deseja fazer [-+*/]: ")
num = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
print(calcula(operacao,num,num2))