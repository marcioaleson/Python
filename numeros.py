import os
#encoding: utf-8
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

#Comversões implícitas

print(3+2)
print(3+3.2)
print(4/2.0)
print(5/2)
print(5//2)
print(complex(1,2) + 2)
print(complex(2,0) + 0+1j)

#Operadores aritméticos

print(1+2)
print(3-1)
print(2*2)
print(3/3)
print(3//2)
print(3%2)
print(2**8)

#Operadores de bits

print(1 | 0)
print(1 | 5)
print(1 ^ 5)
print(4 & 1)
print(1 << 2)
print(4 >> 2)


#Coerção

print(100 * 1.3)
print(type(1 + 2.0))
print(type(1 + 2J))
print(type(1.0 + 2J))

#Manipulando Strings

print("Copa 2014")
print('Copa do Mundo 2014')
print('''2014 - Copa do mundo''')
print("Copa 'padrão fifa'")
print('Copa "padrão fifa"')
print("""\
	Uso: conculta_base [OPCOES]
	-h Exibe áida de ajuda
	-U url Uraldo dataset
	""")

str = "maracana"
print(str[0])
print(str[1:4])
print(len(str))
print("m" in "maracana")
print("x" not in "maracana")
print("m" + "aracana")
print("a" * 3)
minha_str = "Livro de python 3"
print(minha_str)
minha_str = minha_str[0:13] + "2"
print(minha_str)
minha_str = "Livro de python 3"
minha_str = minha_str.replace("3", "2")
print(minha_str.capitalize())
print(minha_str.count("a"))
print(minha_str.startswith("m"))
print(minha_str.endswith("z"))
print(minha_str.split(" "))
print(" ".join(["Copa", "de", "2014"]))

#Interpolando Strings

print("%d dias para a copa do mundo."%(100))
print("{} dias para a copa do mundo.".format(100))
print("{dias} para a copa do mundo.".format(dias=100))


#Alinhamento

print('{:<60}'.format('Alinhamento à esquesda, acupando 60 posições.'))
print('{:>60}'.format('Alinhamento à direita, ocupando 60 posições.'))
print('{:^60}'.format('Centralizando, ocupando 60 posições.'))
print('{:.^60}'.format('Centralizando ao alterar caracter de espaço.'))
