def verificar_idade(idade):
    if idade >=18:
        return f"entrada permitida"
    else:
        return f"entrada não permitida"
    
try:
    idade = int(input("Digite sua idade: "))
    resultado = verificar_idade(idade)
    print(resultado)
except ValueError:
    print("erro: digite um numero inteiro!")