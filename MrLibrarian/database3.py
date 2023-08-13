import sqlite3




def status(username):
  conn = sqlite3.connect('xrecord.db')
  c = conn.cursor()
  c.execute("SELECT * FROM xrecords WHERE username = username")
  return c.fetchall()
  conn.commit()
  conn.close()

def add_record(username, book_code, date):
  conn = sqlite3.connect('xrecord.db')
  c = conn.cursor()
  c.execute("INSERT INTO xrecords VALUES (?,?,?)", (username, book_code, date))
  conn.commit()
  conn.close()

def del_record(username, book_code):
  conn = sqlite3.connect('xrecord.db')
  c = conn.cursor()
  c.execute("DELETE from xrecords WHERE username=[] AND book_code = []")
  conn.commit()
  conn.close()

