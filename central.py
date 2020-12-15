import PySimpleGUI as sg 
import base64
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

def read_task0():
    cursor = dbestoque.cursor()
    cursor.execute('''SELECT * from produtos''')
    data = cursor.fetchall()
    dbestoque.commit()
    return data
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


def vender(q, h):
    cursor.execute('''update produtos set Quantidade =? where Nome= ?''', (q,h,))
    dbestoque.commit()

def add_estoque(add_q, h):
    cursor.execute('''update produtos set Quantidade =? where Nome= ?''', (add_q,h,))
    dbestoque.commit()

def Editar(p, h):
    cursor.execute('''update produtos set Preco =? where Nome=?''', (p, h))
    dbestoque.commit()

def EditarID(p, h):
    cursor.execute('''update produtos set Id =? where Nome=?''', (p, h))
    dbestoque.commit()



def busca0(c):
    cursor.execute('''SELECT Id from produtos where Nome LIKE ?''',('%'+c+'%',))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def busca1(c):
    cursor.execute('''SELECT Nome from produtos WHERE Nome LIKE ? ''',('%'+c+'%',))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def busca2(c):
    cursor.execute('''SELECT Quantidade from produtos where Nome LIKE ?''',('%'+c+'%',))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def busca2_teste(y):
    cursor.execute('''SELECT Quantidade from produtos where Nome=?''',(y,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def busca3(c):
    cursor.execute('''SELECT Preco from produtos where Nome LIKE ?''',('%'+c+'%',))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

def filtrar(f):
    cursor.execute('''SELECT Nome from produtos where Quantidade <= ?''',(f,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado
def filtrar2(f):
    cursor.execute('''SELECT Id from produtos where Quantidade <= ?''',(f,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado
def filtrar3(f):
    cursor.execute('''SELECT Quantidade from produtos where Quantidade <= ?''',(f,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado
def filtrar4(f):
    cursor.execute('''SELECT Preco from produtos where Quantidade <= ?''',(f,))
    resultado = cursor.fetchall()
    dbestoque.commit()
    return resultado

    
##############################################main############################################


def AdicionarItem():
    with open("logo.ico", "rb") as f:
        my_icon = base64.b64encode(f.read())
        sg.set_options(icon=my_icon)



    #mudar tema
    sg.change_look_and_feel('DarkGreen')


    Nome = read_task()
    Quantidade = read_task1()
    Preco = read_task2()
    Id = read_task3()
    
    #layout
    layout = [
        [sg.Text('Digite o nome do item:',size=(15,0)),sg.Input(do_not_clear=False, size=(20,0),key='add_item')],
        [sg.Text('A quantidade:'), sg.Text("      "),sg.Input(do_not_clear=False, size=(20,0),key='add_quantidade')],
        [sg.Text('Digite o preço do item:',size=(15,0)),sg.Input(do_not_clear=False,size=(20,0),key='add_preco')],
        [sg.Text('Digite o codigo de ID',size=(15,0)),sg.Input(do_not_clear=False,size=(20,0),key='Cod_id')],
        [sg.Button('Adicionar')], 
        [sg.Text('ID'),sg.Text('                      '),sg.Text('Produto'),sg.Text('                    '),sg.Text('Quantidade'),sg.Text('  '),sg.Text('Preço')],
        [sg.Listbox(Id, size=(5,10), key='-BOX0-'),
        sg.Listbox(Nome, size=(25, 10), key='-BOX-'),
        sg.Listbox(Quantidade, size=(10, 10), key='-BOX2-'),
        sg.Listbox(Preco, size=(10, 10), key='-BOX3-')],
        [sg.Button('Deletar'),sg.Button('Voltar')],
        [sg.Button('Sair')]
        ]
    #janela
    window = sg.Window("adicionar ao Estoque",layout)

    while True:
        event,values = window.read()

            
        if event == 'Adicionar':
            try: 
                Nome = values['add_item']
                quantidadeIntra = values['add_quantidade']
                precoIntra = values['add_preco']
                Id = values['Cod_id']
            
                Quantidade = int(quantidadeIntra)
                Preco = float(precoIntra)

                if Nome != '':
                    escreve(Nome, Quantidade, Preco, Id)
                Nome = read_task()
                Quantidade = read_task1()
                Preco = read_task2()
                Id = read_task3()
                window.find_element('-BOX-').Update(Nome)
                window.find_element('-BOX2-').Update(Quantidade)
                window.find_element('-BOX3-').Update(Preco)
                window.find_element('-BOX0-').Update(Id)

            except ValueError as erro:
                print("Coloque os valores corretamente")


        if event == 'Deletar':
            if Nome:
                y = values['-BOX-'][0]
                x = (y[0])
                delete(x)
                Nome = read_task()
                Quantidade = read_task1()
                Preco = read_task2()
                Id = read_task3()
                window.find_element('-BOX-').Update(Nome)
                window.find_element('-BOX2-').Update(Quantidade)
                window.find_element('-BOX3-').Update(Preco)
                window.find_element('-BOX0-').Update(Id)


                
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            break

        if event == 'Voltar':
            window.close()
            initi()
            
            
            
        
####################################venda###################################################

with open("logo.ico", "rb") as f:
    my_icon = base64.b64encode(f.read())
    sg.set_options(icon=my_icon)


def JanelaEdit():
    sg.change_look_and_feel('DarkGreen')
    elayout = [
        [sg.Text('Digite o novo Preço:'),sg.Input(key='edit_item')],
        [sg.Button('Enviar')]
              ]
    window = sg.Window('Novo Preço',elayout)
    event, values = window.read()
    global edit
    edit = values['edit_item']
    window.close()

        

def JanelaVenda():
    sg.change_look_and_feel('DarkGreen')


    Nome = '' 
    Quantidade = ''
    Preco = ''
    Id = ''

    vlayout = [
        [sg.Text('Digite o item que deseja fazer a venda'), sg.Input(do_not_clear=False, size=(20,0),key='vender')],
        [sg.Text('ID'),sg.Text('                      '),sg.Text('Produto'),sg.Text('                    '),sg.Text('Quantidade'),sg.Text('  '),sg.Text('Preço')],
        [sg.Listbox(Id, size=(5,10), key='-BOX0-'),
        sg.Listbox(Nome, size=(25, 10), key='-BOX-'),
        sg.Listbox(Quantidade, size=(10, 10), key='-BOX2-'),
        sg.Listbox(Preco, size=(10, 10), key='-BOX3-')],
        [sg.Button('Consultar'), sg.Button('Realizar venda'),sg.Button('Deletar'),sg.Text('        '),sg.Button('Editar'),sg.Button('Add estoque'),sg.Button('Identifição')],
        [sg.Button('Sair'),sg.Button('Voltar')]
    ]

    window = sg.Window('Controle de estoque',vlayout)
    while True:
        event,values = window.read()

        if event == 'Consultar':
            c = values['vender']
            Id = busca0(c)
            Nome = busca1(c)
            Quantidade = busca2(c)
            Preco = busca3(c)
            window.find_element('-BOX0-').Update(Id)
            window.find_element('-BOX-').Update(Nome)
            window.find_element('-BOX2-').Update(Quantidade)
            window.find_element('-BOX3-').Update(Preco)
        try:
            if event == 'Realizar venda':
                if Nome:
                    x = values['-BOX-'][0]
                    y = (x[0])
                    Avenda()
                    QuantiTrat = int(Quanti)
                    print(QuantiTrat)
                    Quantidade = busca2_teste(y)
                    Vquantidade0 = (Quantidade[0])
                    Vquantidade = (Vquantidade0[0])
                    subtration = Vquantidade - QuantiTrat
                    q = subtration
                    h = y
                    vender(q, h)
                    Quantidade = busca2(c)
                    window.find_element('-BOX2-').Update(Quantidade)
                    
            if event == 'Add estoque':
                if Nome:
                    x = values['-BOX-'][0]
                    y = (x[0])
                    Add_Quanti()
                    AddQuantiTrat = int(AddQuanti)
                    AddQuantidade = busca2_teste(y)
                    Vquantidade1 = (AddQuantidade[0])
                    Vquantidade2 = (Vquantidade1[0])
                    addition = Vquantidade2 + AddQuantiTrat
                    q = addition
                    h = y
                    add_estoque(q, h)
                    Quantidade = busca2(c)
                    window.find_element('-BOX2-').Update(Quantidade)
        except ValueError:
            print('erro')
                



        if event == 'Deletar':
            if Nome:
                y = values['-BOX-'][0]
                x = (y[0])
                delete(x)
                Id = busca0(c)
                Nome = busca1(c)
                Quantidade = busca2(c)
                Preco = busca3(c)
                window.find_element('-BOX0-').Update(Id)
                window.find_element('-BOX-').Update(Nome)
                window.find_element('-BOX2-').Update(Quantidade)
                window.find_element('-BOX3-').Update(Preco)
        
        if event == 'Editar':
            if Nome:
                x = values['-BOX-'][0]
                y = (x[0])
                JanelaEdit()
                p = edit
                h = y
                Editar(p, h)
                Preco = busca3(c)
                window.find_element('-BOX3-').Update(Preco)

        if event == 'Identifição':
            if Nome:
                x = values['-BOX-'][0]
                y = (x[0])
                JanelaEdit()
                p = edit
                h = y
                EditarID(p, h)
                Id = busca0(c)
                window.find_element('-BOX0-').Update(Id)

        
           


        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            break
        if event == 'Voltar':
            window.close()
            initi()
        
def Avenda():
    sg.change_look_and_feel('DarkGreen')
    #layout
    tlayout = [
        [sg.Text('Digite a quantidade:',size=(15,0)),sg.Input(size=(20,0), key='InQuanti')],
        [sg.Button('Vender')]
        
        ]
    #janela
    window = sg.Window("Controle de estoque", tlayout)


    event,values = window.read()
    global Quanti
    Quanti = values['InQuanti']
    if event == 'Vender':
        window.close()

def Add_Quanti():
    sg.change_look_and_feel('DarkGreen')
    #layout
    ylayout = [
        [sg.Text('Digite a quantidade:',size=(15,0)),sg.Input(size=(20,0), key='Adicionar_Quanti')],
        [sg.Button('Adicionar')]
        
        ]
    #janela
    window = sg.Window("Controle de estoque", ylayout)


    event,values = window.read()
    global AddQuanti
    AddQuanti = values['Adicionar_Quanti']
    if event == 'Adicionar':
        window.close()
    
#########################################filtragem##############################################
def Filtrar():
    with open("logo.ico", "rb") as f:
        my_icon = base64.b64encode(f.read())
        sg.set_options(icon=my_icon)       

    #mudar tema
    sg.change_look_and_feel('DarkGreen')


    Nome = ''
    Quantidade = ''
    Preco = ''
    Id = ''
    
    #layout
    layout = [
        [sg.Text('Digite a quantidade que deseja filtrar:',size=(15,0)),sg.Input(do_not_clear=False, size=(20,0),key='fil_item')],
        [sg.Button('Consultar')], 
        [sg.Text('ID'),sg.Text('                      '),sg.Text('Produto'),sg.Text('                    '),sg.Text('Quantidade'),sg.Text('  '),sg.Text('Preço')],
        [sg.Listbox(Id, size=(5,10), key='-BOX0-'),
        sg.Listbox(Nome, size=(25, 10), key='-BOX-'),
        sg.Listbox(Quantidade, size=(10, 10), key='-BOX2-'),
        sg.Listbox(Preco, size=(10, 10), key='-BOX3-')],
        [sg.Button('Deletar')],
        [sg.Button('Sair'),sg.Button('Voltar')]
        ]
    #janela
    window = sg.Window("adicionar ao Estoque",layout)

    while True:
        event,values = window.read()

        
        if event == 'Consultar':
            f = values['fil_item']
            Id = filtrar2(f)
            Nome = filtrar(f)
            Quantidade = filtrar3(f)
            Preco = filtrar4(f)
            window.find_element('-BOX-').Update(Nome)
            window.find_element('-BOX0-').Update(Id)
            window.find_element('-BOX2-').Update(Quantidade)
            window.find_element('-BOX3-').Update(Preco)
            






        if event == 'Deletar':
            if Nome:
                y = values['-BOX-'][0]
                x = (y[0])
                delete(x)
                Id = busca0(c)
                Nome = busca1(c)
                Quantidade = busca2(c)
                Preco = busca3(c)
                window.find_element('-BOX0-').Update(Id)
                window.find_element('-BOX-').Update(Nome)
                window.find_element('-BOX2-').Update(Quantidade)
                window.find_element('-BOX3-').Update(Preco)

                
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            break

        if event == 'Voltar':
            window.close()
            initi()

########################################################################################
def initi():
    with open("logo.ico", "rb") as f:
        my_icon = base64.b64encode(f.read())
        sg.set_options(icon=my_icon)



    sg.change_look_and_feel('DarkGreen')

    ilayout = [
        [sg.Text('Olá seja Bem-vindo, Oque deseja fazer?')],
        [sg.Button('Adicionar ao Estoque')],
        [sg.Button('Realizar uma venda')],
        [sg.Button('Fazer uma filtragem')],
        [sg.Button('Sair')]
    ]

    window = sg.Window('Controle de estoque',ilayout)

    button, values = window.read()
    if button == 'Adicionar ao Estoque':
        window.close()
        AdicionarItem()
    if button == 'Realizar uma venda':
        window.close()
        JanelaVenda()
    if button == 'Fazer uma filtragem':
        window.close()
        Filtrar()
    if button == 'Sair':
        window.close()
initi()