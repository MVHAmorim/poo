from classe import Automoveis

corsa = Automoveis('Verde', 'GM', 'SL', 140)
print( corsa.veloAtual) # 0
print( corsa.ligado) # False

corsa.acelerar(20)
print(corsa.veloAtual) # 20

corsa.ligado = True

for a in range(3):
    corsa.acelerar(50)
    
print(corsa.veloAtual)

for a in range(3):
    corsa.frear(50)

print(corsa.veloAtual)