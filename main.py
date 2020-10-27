import PySimpleGUI as sg
import criaBanco
import base64


def AdicionarItem():
    with open("logo.ico", "rb") as f:
        my_icon = base64.b64encode(f.read())
    sg.set_options(icon=my_icon)

  
        
            

    #mudar tema
    sg.change_look_and_feel('DarkGreen')


    Nome = criaBanco.read_task()
    Quantidade = criaBanco.read_task1()
    Preco = criaBanco.read_task2()
    Id = criaBanco.read_task3()
    
    #layout
    layout = [
        [sg.Text('Digite o nome do item:',size=(15,0)),sg.Input(do_not_clear=False, size=(20,0),key='add_item')],
        [sg.Text('A quantidade:'), sg.Text("      "),sg.Input(do_not_clear=False, size=(20,0),key='add_quantidade')],
        [sg.Text('Digite o preço do item:',size=(15,0)),sg.Input(do_not_clear=False,size=(20,0),key='add_preco')],
        [sg.Text('Digite o codigo de ID',size=(15,0)),sg.Input(do_not_clear=False,size=(20,0),key='Cod_id')],
        [sg.Button('Adicionar')], 
        [sg.Text('Produto'),sg.Text('                                  '),sg.Text('Quantidade'),sg.Text('       '),sg.Text('Preço')],
        [sg.Listbox(Id, size=(5,10), key='-BOX0-'),
        sg.Listbox(Nome, size=(25, 10), key='-BOX-'),
        sg.Listbox(Quantidade, size=(10, 10), key='-BOX2-'),
        sg.Listbox(Preco, size=(10, 10), key='-BOX3-')],
        [sg.Button('Deletar')],
        [sg.Button('Sair')]
        ]
    #janela
    window = sg.Window("adicionar ao Estoque",layout)

    while True:
        button,values = window.read()

            
        if button == 'Adicionar':
            try: 
                Nome = values['add_item']
                quantidadeIntra = values['add_quantidade']
                precoIntra = values['add_preco']
                Id = values['Cod_id']
            
                Quantidade = int(quantidadeIntra)
                Preco = float(precoIntra)

                if Nome != '':
                    criaBanco.escreve(Nome, Quantidade, Preco, Id)
                Nome = criaBanco.read_task()
                Quantidade = criaBanco.read_task1()
                Preco = criaBanco.read_task2()
                Id = criaBanco.read_task3()
                window.find_element('-BOX-').Update(Nome)
                window.find_element('-BOX2-').Update(Quantidade)
                window.find_element('-BOX3-').Update(Preco)
                window.find_element('-BOX0-').Update(Id)

            except ValueError as erro:
                print("Coloque os valores corretamente")


        if button == 'Deletar':
            if Nome:
                y = values['-BOX-'][0]
                x = (y[0])
                criaBanco.delete(x)
                Nome = criaBanco.read_task()
                Quantidade = criaBanco.read_task1()
                Preco = criaBanco.read_task2()
                Id = criaBanco.read_task3()
                window.find_element('-BOX-').Update(Nome)
                window.find_element('-BOX2-').Update(Quantidade)
                window.find_element('-BOX3-').Update(Preco)
                window.find_element('-BOX0-').Update(Id)


                
        if sg.WIN_CLOSED or button == 'Sair':
            window.close()
            break

        if button == 'Voltar':
            
            window.close()

AdicionarItem()