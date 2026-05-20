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

    
    
