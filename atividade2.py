def somar(a,b):
    return a+b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b == 0:
        return "não se pode dividir por zero"
    else:
        return a // b
    
print("escolha uma opção: ")
print("1 - somar")
print("2- subtrair")
print("3- multiplicar")
print("4- dividir")

opcao = input("Digite a opção desejada: ")
try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o ultimo numero: "))
    if opcao == "1":
        print("a soma é igual a: ",somar(num1,num2))
    if opcao == "2":
        print("a subtração é igual a: ", subtrair(num1,num2))
    if opcao == "3":
        print("a multiplicação é igual a : ", multiplicar(num1,num2))
    if opcao == "4":
        print("a divisão é igual a: ", dividir(num1,num2))
except ValueError:
    print("valor invalido!")
