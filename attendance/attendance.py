import sqlite3

conn = sqlite3.connect("data")

def create():
	try:
		conn.execute('CREATE TABLE candidate (id integer PRIMARY KEY AUTOINCREMENT , Name varchar)')
	except:
		pass

def insert_once():
	create()
	try:
		cur = conn.cursor()
		cur.execute('INSERT INTO candidate (id , name ) VALUES (1,"admin")')
	except:
		pass
def Insert(name):
	cur = conn.cursor()
	cur.execute('INSERT INTO candidate (Name) VALUES (?)',(name,))
	conn.commit()
	print("sucess")

def Search(ids , name):
	create()
	cur = conn.cursor()
	data = cur.execute('SELECT * FROM candidate WHERE id = ? and name = ?',(ids , name))
	info = data.fetchall()
	return info
def Search_by_id(idss):
	create()
	cur = conn.cursor()
	data = cur.execute('SELECT * FROM candidate WHERE id = ?',(idss,))
	info = data.fetchall()
	return info
def Search_by_name(name):
	create()
	cur = conn.cursor()
	data = cur.execute('SELECT * FROM candidate WHERE name = ?',(name,))
	info = data.fetchall()
	return info


def Show_all_data():
	create()
	cur = conn.cursor()
	data = cur.execute('SELECT * FROM candidate')
	info = data.fetchall()
	return info

def update(id , name , new_id , new_name):
	create()
	cur = conn.cursor()
	data = cur.execute('UPDATE candidate SET id = 4 , name = "Dipesh" WHERE id = 1')
	conn.commit()

def delete(id , name):
	create()
	cor = conn.cursor()
	cor.execute('DELETE FROM candidate where id = 2 and name = "diwas"')
	conn.commit()
insert_once()
# print(Show_all_data())