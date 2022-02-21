import sqlite3

def connect():
    conn = sqlite3.connect('ports.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, port text,'
                'country text, last text, visit text)')
    conn.commit()
    conn.close()

def insert(port, country, last, visit):
    conn = sqlite3.connect('ports.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book VALUES (NULL,?,?,?,?)',(port,country,last,visit))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('ports.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
insert('Abidjan', 'Cote D\'Ivore', 'Jul-2019', '')
print(view())