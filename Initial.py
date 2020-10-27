import PySimpleGUI as sg 
import base64
import Vender
import main
import consulta


with open("logo.ico", "rb") as f:
    my_icon = base64.b64encode(f.read())
sg.set_options(icon=my_icon)


sg.change_look_and_feel('DarkGreen')

ilayout = [
    [sg.Text('Olá seja Bem-vindo, Oque deseja fazer?')],
    [sg.Button('Adicionar ao Estoque')],
    [sg.Button('Realizar uma venda')],
    [sg.Button('Fazer uma consulta')],
    [sg.Button('Sair')]
]

window = sg.Window('Controle de estoque',ilayout)

button, values = window.read()
if button == 'Adicionar ao Estoque':
    window.close()
    main.AdicionarItem()
if button == 'Realizar uma venda':
    window.close()
    Vender.JanelaVenda()
if button == 'Fazer uma consulta':
    window.close()
    consulta.Consultar()
if button == 'Sair':
    window.exit()
