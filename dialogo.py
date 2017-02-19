try:
    dialogo = open("dialogo.txt")
    dialogo.seek(0)
    for linha in doalogo:
	    try:
	        if not linha.find(":") == -1
	            ator, fala = linha.split(":", 1)
	            print(ator, end="")
	            print(" fala", end="")
	            print(fala, end="")
	    except ValueError:
            print("Erro na leitura do arquivo.")
    dialogo.close()
except:
	print("Arquivo nao pode ser encontrado...")