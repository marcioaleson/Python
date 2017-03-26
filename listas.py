lista = []
if lista:
    print("Nunca sou executado")
else:
    print("Sempre sou executado")

impostos = ['MEI', 'Simples']
for imposto in impostos:
    print(imposto)


impostos = ['MEI', 'Simples']
for imposto in impostos:
	if imposto.startswith("S"):
	    continue
	print(imposto)

lista = [0,1,2,3,4,5,6,7,8,9]
for i in lista:
	print(i)