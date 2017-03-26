import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO clientes (nome, idade)
VALUES ('Regis', 35)
""")

cursor.execute("""
INSERT INTO clientes (nome, idade)
VALUES ('Maria', 18)
""")

cursor.execute("""
INSERT INTO clientes (nome, idade)
VALUES ('Joao', 25)
""")

print("Clientes inseridos com sucesso!!")
conn.commit()
conn.close()