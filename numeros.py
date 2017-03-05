import os

#Formas literais de escrever números

print(1)#int
print(1.0)#float
print(1.)#também float
print(1+2j)#número complexo

#Funções embutidas

print(int(1.0))
print(int('9'))
print(float(1))
print(float('9.2'))
print(float('-inf'))
print(float('+inf'))
print(float('nan'))
print(complex('1,2'))

#Comverções implícitas

print(3+2)
print(3+3.2)
print(4/2.0)
print(5/2)
print(5//2)
print(complex(1,2) + 2)
print(complex(2,0) + 0+1j)
