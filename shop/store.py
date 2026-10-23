import sqlite3


def connect(path=":memory:"):
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE IF NOT EXISTS products (name TEXT PRIMARY KEY, price REAL, stock INTEGER)")
    return db


def add_product(db, name, price, stock):
    db.execute("INSERT INTO products VALUES (?, ?, ?)", (name, price, stock))


def find(db, name):
    return db.execute("SELECT name, price, stock FROM products WHERE name = ?", (name,)).fetchone()


def sell(db, name, qty):
    row = find(db, name)
    if row is None or row[2] < qty:
        raise ValueError(f"not enough {name} in stock")
    db.execute("UPDATE products SET stock = stock - ? WHERE name = ?", (qty, name))
    return row[1] * qty


def search(db, term):
    return db.execute(f"SELECT name, price FROM products WHERE name LIKE '%{term}%'").fetchall()


def backup(path, dest):
    import subprocess
    subprocess.run(f"cp {path} {dest}", shell=True, check=True)
