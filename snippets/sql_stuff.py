<<<<<<< HEAD
import sqlite3
import time

def prompt():
    prod_id = raw_input('id ')
    quantity = int(raw_input('quantity '))
    return unicode(time.asctime()), prod_id, quantity


def main():
    while True:
        db.execute('INSERT INTO Product VALUES (?, ?, ?)', (prompt()))
        base.commit()
        again = raw_input('another one? ')
        if not again:
            break
    base.close()


base = sqlite3.connect('../static/database.sqlite')
db = base.cursor()
# db.execute('CREATE TABLE Product (time text, id text, quantity int)')
# db.execute('''CREATE TABLE Parts (id text, quantity int)''')

main() 
=======
import sqlite3
import time

def prompt():
    prod_id = raw_input('id ')
    quantity = int(raw_input('quantity '))
    return unicode(time.asctime()), prod_id, quantity


def main():
    while True:
        db.execute('INSERT INTO Product VALUES (?, ?, ?)', (prompt()))
        base.commit()
        again = raw_input('another one? ')
        if not again:
            break
    base.close()


base = sqlite3.connect('../static/database.sqlite')
db = base.cursor()
# db.execute('CREATE TABLE Product (time text, id text, quantity int)')
# db.execute('''CREATE TABLE Parts (id text, quantity int)''')

main() 
>>>>>>> 5d67aefaf7fb349cc4275cc67b614f6e10122b35
