class Bolo:
    def __init__(self,sabor,cobertura):
        self.sabor = sabor
        self.cobertura = cobertura
    def assar(self):
        print(f"o bolo de {self.sabor} com {self.cobertura} está assando a 120° ")
bolo1 = Bolo("chocolate", "brigadeiro")
bolo2 = Bolo("morango", "chantily")
bolo1.assar()
bolo2.assar()


class Animal:
    def __init__(self, nome,especie,idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    def mostrar(self):
        print(f"olá me chamo {self.nome} e sou um {self.especie}, e tenho {self.idade} aninhos")

animal1 = Animal("Lulu","cachorro","6")
animal2 = Animal("Betty","tartaruga","3")
animal3 = Animal("chris","lobo","4")
        
    
    