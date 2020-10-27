import PySimpleGUI as sg
import criaBanco
import base64


def Consultar():
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
        [sg.Text('Digite o nome do item:',size=(15,0)),sg.Input(do_not_clear=False, size=(20,0),key='consu_item')],
        [sg.Button('Consultar'), sg.InputCombo(('Capacitor', 'Ci'), size=(20, 1),key='-combo-')], 
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

        
        if button == 'Consultar':
            c = values['consu_item']
            Id = criaBanco.busca0(c)
            Nome = criaBanco.busca1(c)
            Quantidade = criaBanco.busca2(c)
            Preco = criaBanco.busca3(c)
            window.find_element('-BOX0-').Update(Id)
            window.find_element('-BOX-').Update(Nome)
            window.find_element('-BOX2-').Update(Quantidade)
            window.find_element('-BOX3-').Update(Preco)






        if button == 'Deletar':
            if Nome:
                y = values['-BOX-'][0]
                x = (y[0])
                criaBanco.delete(x)
                Id = criaBanco.busca0(c)
                Nome = criaBanco.busca1(c)
                Quantidade = criaBanco.busca2(c)
                Preco = criaBanco.busca3(c)
                window.find_element('-BOX0-').Update(Id)
                window.find_element('-BOX-').Update(Nome)
                window.find_element('-BOX2-').Update(Quantidade)
                window.find_element('-BOX3-').Update(Preco)

                
        if sg.WIN_CLOSED or button == 'Sair':
            window.close()
            break

        if button == 'Voltar':
            
            window.close()
