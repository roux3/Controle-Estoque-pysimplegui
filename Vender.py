import PySimpleGUI as sg 
import criaBanco
import base64
with open("logo.ico", "rb") as f:
    my_icon = base64.b64encode(f.read())
sg.set_options(icon=my_icon)

def JanelaVenda():
    def popup():
        sg.change_look_and_feel('DarkGreen')

        playout = [
            [sg.popup('Selecione um item primeiro!')]
        ]
        janelinha = sg.Window("Popup",playout)
        
        event, values = janelinha.read()
        window.close()
    
    def popupConfirma(QuantiTrat):#mexer depois
        sg.change_look_and_feel('DarkGreen')

        clayout = [
            [sg.Text('Segue abaixo o Valor Total:')],
            [sg.Output(size=(30,10))],
            [sg.Text('Deseja mesmo efetuar a venda?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

        window = sg.Window('Confirmação', clayout)
        button,values = window.read()

        print("teste")
        if button == 'Sim':
            window.close()
        if button == 'Não':
            window.exit()
        
    
        

    def Avenda():
        sg.change_look_and_feel('DarkGreen')
        #layout
        tlayout = [
            [sg.Text('Digite a quantidade:',size=(15,0)),sg.Input(size=(20,0), key='InQuanti')],
            [sg.Button('Vender')]
            
            ]
        #janela
        janela = sg.Window("Controle de estoque", tlayout)


        button,values = janela.read()
        global Quanti
        Quanti = values['InQuanti']
        if button == 'Vender':
            janela.close()
        return Quanti


    sg.change_look_and_feel('DarkGreen')
    
    
    Nome = criaBanco.read_task0()

    vlayout = [
        [sg.Text('Selecione o item que deseja fazer a venda')],
        [sg.Listbox(Nome, size=(30, 10), key='-BOX-')],
        [sg.Button('Realizar uma venda')],
        [sg.Button('Sair')]
    ]

    window = sg.Window('Controle de estoque',vlayout)
    while True:
        button,values = window.read()
        try:
            if button == 'Realizar uma venda':
                if Nome:
                    Avenda()
                    QuantiTrat = int(Quanti)
                    popupConfirma(QuantiTrat)#mexer depois
                    y = values['-BOX-'][0] 
                    v = (y[0])
                    Vquantidade = (y[1])
                    subtration = Vquantidade - QuantiTrat
                    q = subtration
                    criaBanco.vender(q, v)
                    Nome = criaBanco.read_task0()
                    window.find_element('-BOX-').Update(Nome)
        except IndexError as erro:
            print('Erro')


        if sg.WIN_CLOSED or button == 'Sair':
            window.close()
            break

    