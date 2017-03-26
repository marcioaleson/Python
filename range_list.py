from datetime import date
import math as matematica
from math import log2 as l2
import os


#Variables
impostos = ['MEI', 'Simples']

for i in range(5):
    print(i)

for i, impostos in enumerate(impostos):
    print(i, impostos)

def sum(num1, num2):
    return num1 + num2

c = sum(1,3)

print(c)

def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)

print(salario_descontado_imposto(5000))

print(salario_descontado_imposto(5000, imposto=0.10))

d = (2017, 3, 25)
print(date(d[0], d[1], d[2]))
print(*d)

def new_user(active=False, admin=False):
    print(active)
    print(admin)

config = {"active": False, "admin": True}

new_user(config.get('active'), config.get('admin'))

new_user(**config)

def unpacking_experiment(self, *args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)

unpacking_experiment(1,2,3,4,5,6)

def unpacking_experiment2(**args):
    print(args)

unpacking_experiment2(named = "Test", others = "Others")

#print(math.sqrt(9))

print(matematica.sqrt(9))

print(l2(1024))
