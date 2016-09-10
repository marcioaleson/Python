import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
#Lendo os dados
cursor.execute("""SELECT * FROM clientes;""")
for linha in cursor.fetchall():
	print(linha)

conn.close()