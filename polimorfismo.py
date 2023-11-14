class Animal:
    def locomove(self):
        return "Método de Locomoção: "

class Peixe(Animal):
    def locomove(self) -> str:
        return "Um peixe nada."

class Elefante(Animal):
    def locomove(self) -> str:
        return super().locomove() + "Um elefante anda."

class Passaro(Animal):
    def locomove(self) -> str:
        return "um pássaro voa."

# Teste de Mesa:
peixe = Peixe()
elefante = Elefante()
passaro = Passaro()
print(peixe.locomove())
print(elefante.locomove())
print(passaro.locomove())