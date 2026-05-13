
def somar(a,b):
    try:
        a = int(input("Digite um numero: "))
        b = int(input(" Digite outro numero: "))
    except:
        print("erro: digite apenas numeros inteiros")
    return f"o resultado da soma é igual a: {a+b}" 

def subtrair(a,b):
    try:
        a = int(input("Digite um numero: "))
        b = int(input(" Digite outro numero: "))
    except:
        print("erro: digite apenas numeros inteiros")
    return f"o resultado da multiplicação é igual a: {a - b}"

def multiplicar(a,b):
    try:
        a = int(input("Digite um numero: "))
        b = int(input(" Digite outro numero: "))
    except:
        print("erro: digite apenas numeros inteiros")
    return f" o resultado da multiplicação é igual a: {a * b}" 

def dividir(a,b):
    try:
        a = int(input("Digite um numero: "))
        b = int(input(" Digite outro numero: "))
    except ZeroDivisionError:
        print("nao pode dividir por zero")
    except ValueError:
        print("valor invalido")
        return f" o resultado da divisão é igual a: {a // b}"
print("Menu")
print("1 - soma")
print("2-multiplicação")
print("3- divisao")
print("4- multiplicação")

while True:
    opcao = input("escolha uma opção: ")
    if opcao == "1":
        def somar():
            break
    if opcao == "2":
        def subtrair()
            break