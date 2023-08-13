import sqlite3



#conn = sqlite3.connect('xledger.db')
#c = conn.cursor()
#c.execute("INSERT INTO xledgers VALUES ('qaz', 'wsx', 'good', 'library')")
#print("command executer")#, (book_code, book_name, description, current)
#conn.commit()
#conn.close()

def add_book(book_code, book_name, description, current):
  conn = sqlite3.connect('xledger.db')
  c = conn.cursor()
  c.execute("INSERT INTO xledgers VALUES ('qaz', 'wsx', 'good', 'library')")
  print("command executer")#, (book_code, book_name, description, current)
  conn.commit()
  conn.close()

def search_code(x):
  conn = sqlite3.connect('xledger.db')
  c = conn.cursor()
  c.execute("SELECT * FROM xledgers WHERE book_code = ? ",(x))
  return c.fetchone()
  conn.commit()
  conn.close()


def search_name(book_name):
  conn = sqlite3.connect('xledger.db')
  c = conn.cursor()
  c.execute("SELECT * FROM xledgers WHERE book_name LIKE ?",(book_name))
  return c.fetchone()
  conn.commit()
  conn.close()

def update_current(book_code):
  conn = sqlite3.connect('xledger.db')
  c = conn.cursor()
  c.execute("UPDATE xledgers SET current = [] WHERE current = [] AND book_code = []")
  conn.commit()
  conn.close()
  