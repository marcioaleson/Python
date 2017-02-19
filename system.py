import os
resposta = int(input("1 limpar;\n 2 criar;\n 3 acessar;\n 4 informacoes; \n"))
if resposta == 1:
	 os.system("clear")
if resposta == 2:
	os.mkdir("teste")
if resposta == 3:
	os.chdir("/home/professor/Documentos/Python/Exemplos aula/leia")
if resposta == 4:
	print("Voce esta no diretorio:",os.getcwd())
print("Fim!!")
