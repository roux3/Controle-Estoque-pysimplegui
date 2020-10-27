import sqlite3

dbestoque = sqlite3.connect('Estoque.db')

cursor = dbestoque.cursor()

dbestoque.execute(''' CREATE TABLE IF NOT EXISTS produtos(
                    Nome TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    Preco FLOAT NOT NULL,
                    Id TEXT NOT NULL
                    )''')


dbestoque.commit()

def escreve(Nome, Quantidade, Preco, Id):
    cursor.execute(''' INSERT INTO produtos (Nome, Quantidade, Preco, Id) VALUES(?, ?, ?, ?)''', (Nome, Quantidade, Preco, Id))
    dbestoque.commit()

def delete(x):
    cursor.execute('''delete from produtos where Nome = ?''', (x,))
    dbestoque.commit


def read_task():
    cursor = dbestoque.cursor()
    cursor.execute('''SELECT Nome from produtos''')
    data = cursor.fetchall()
    dbestoque.commit()
    return data
def read_task1():
    cursor = dbestoque.cursor()
    cursor.execute('''SELECT Quantidade from produtos''')
    data1 = cursor.fetchall()
    dbestoque.commit()
    return data1
def read_task2():
    cursor = dbestoque.cursor()
    cursor.execute('''SELECT Preco from produtos''')
    data2 = cursor.fetchall()
    dbestoque.commit()
    return data2
def read_task3():
    cursor = dbestoque.cursor()
    cursor.execute('''SELECT Id from produtos''')
    data3 = cursor.fetchall()
    dbestoque.commit()
    return data3


def vender(q, v):
    cursor.execute('''update produtos set Quantidade =? where Nome=?''', (q, v))
    dbestoque.commit()


def busca0(c):
    cursor.execute('''SELECT Id from produtos where Nome = ?''',(c,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def busca1(c):
    cursor.execute('''SELECT Nome from produtos where Nome = ?''',(c,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def busca2(c):
    cursor.execute('''SELECT Quantidade from produtos where Nome = ?''',(c,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def busca3(c):
    cursor.execute('''SELECT Preco from produtos where Nome = ?''',(c,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado