
class Animal:
    def __init__(self, nome,especie,idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    def mostrar(self):
        print(f"olá me chamo {self.nome} sou um(a) {self.especie}, e tenho {self.idade} aninhos")

animal1 = Animal("Lulu","cachorro","6")
animal2 = Animal("Betty","tartaruga","3")
animal3 = Animal("chris","lobo","4")
animal1.mostrar()
animal2.mostrar()
animal3.mostrar()