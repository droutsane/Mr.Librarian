import sqlite3

def register(username, name, lib_id):
  conn = sqlite3.connect('xcredential.db')
  c = conn.cursor()
  params = (username, name, lib_id)
  c.execute("INSERT INTO xcredentials VALUES (?,?,?)",params)
  conn.commit()
  conn.close()
  