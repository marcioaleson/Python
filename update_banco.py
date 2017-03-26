import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
# Lendo os dados da tabela.
cursor.execute("""UPDATE clientes SET nome = "Marcio Aleson" WHERE id = 1; """)
conn.commit()
print("Registro atualizado com sucesso!")
conn.close()