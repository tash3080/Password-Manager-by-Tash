import sqlite3

db = "password.db"

def create_table():
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS credentials(
        site TEXT,
        email TEXT,
        username TEXT,
        password TEXT
    )''')
    con.commit()
    con.close()

def save(website, username, email, password):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''
    INSERT INTO credentials (site, email, username, password) VALUES ( ?, ?, ?, ? )
    ''', 
    (website, email, username, password))
    con.commit()
    con.close()

def search(website):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('SELECT * FROM credentials WHERE site=?', (website,))
    search_result = cur.fetchall()
    con.commit()
    con.close()
    return search_result

def show_all():
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''SELECT * FROM credentials''')
    all_data = cur.fetchall()
    con.commit()
    con.close()
    return all_data

def update(password, website, email):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('UPDATE credentials SET password=? WHERE site=? AND email=?', (password, website, email))
    cur.execute('SELECT * FROM credentials WHERE site=? AND password=?', (website, password))
    updated_cred = cur.fetchall()
    con.commit()
    con.close()
    return updated_cred

def delete(website, email, password):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('DELETE FROM credentials WHERE site=? AND email=? AND password=?', (website, email, password))
    con.commit()
    con.close()
