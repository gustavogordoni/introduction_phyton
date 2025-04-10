import sqlite3
con = sqlite3.connect("database.sqlite") 

cur = con.cursor() 

cur.execute("CREATE TABLE contato(nome, endereco, telefone)") 

res = cur.execute("SELECT name FROM sqlite_master")

res.fetchone()
('contato',)

print("Tabela criada com sucesso")