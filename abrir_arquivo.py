arquivo = open("mensagem.txt","r")
resposta = open("saida.txt","w")

for linha in arquivo.readlines():
	print(linha, end="")
	for letra in linha:
		if letra in "aeiou":
			resposta.write("*")
		else:
			resposta.write(letra)

arquivo.close()
resposta.close()