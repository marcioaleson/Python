import sqlite3
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()
#Lendo os dados do banco.
cursor.execute("""DELETE  FROM clientes WHERE id = 4;""")
conn.commit()
print("Registro deletado com sucesso!")
conn.close()
