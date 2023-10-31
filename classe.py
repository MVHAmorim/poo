class Automoveis:
    # Método Construtor:
    def __init__(self, cor, marca, tipo, maxima):
        self.cor = cor
        self.marca = marca
        self.modelo = tipo
        self.veloAtual = 0
        self.veloMax = maxima
        self.ligado = False
    
    def acelerar(self, velo):
        if self.ligado:
            if (self.veloAtual + velo) > self.veloMax:
                self.veloAtual = self.veloMax
            else:
                self.veloAtual+= velo

    def frear(self, frenagem):
        if self.ligado:
            if (self.veloAtual - frenagem) < 0:
                self.veloAtual = 0                
            else:
                self.veloAtual -= frenagem                

# Exoplicsção de herança
class Motocicletas(Automoveis):
    pass
