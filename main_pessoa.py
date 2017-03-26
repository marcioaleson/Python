from pessoa import Pessoa
from filho import Filho
p1 = Pessoa("Marcio Aleson", "Rosario", 30)
print("Dados do usuario:")
print("Nome:",p1.nome)
print("Mae:", p1.mae)
print("Idade:",p1.idade)
f1 = Filho(nome="Joao", mae="Mae do joao",idade=15)
print("Dados pessoais:")
print("Nome:", f1.nome)
print("Mae:", f1.mae)
print("Idade:",f1.idade)