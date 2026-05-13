#try:
    #n = int(input("idade: "))
#except:
    #print("erro: digite apenas numeros: ")

try:
    res = 10 / 0
except ZeroDivisionError:
    print("nao pode dividir por zero!")
except ValueError:
    print("valor invalido! ")