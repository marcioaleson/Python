salario = int(input('Salario? '))
imposto = float(input('Imposto em % (ex: 27.5)? '))
print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

#Comparações

print(1>2)
print(2<1)
print(9 == 9)
print(9 != 8)
print(2 <= 3)


#Condicionais

salario = int(input('Salario? '))
imposto = input('Imposto em % (ex: 27.5)? ')
if imposto == '':
    imposto = 27.5
else:
    imposto = float(imposto)
print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

imposto = float(input("Imposto: "))
if imposto < 10:
    print("Medio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito alto")

#Operações lógicas

imposto = float(input("Imposto: "))
if imposto < 10.:
    print("Baixo")
elif imposto >= 10. and imposto <= 27.:
    print("Médio")
elif imposto > 27. and imposto < 100:
    print("Alto")
else:
    print("Imposto inválido")