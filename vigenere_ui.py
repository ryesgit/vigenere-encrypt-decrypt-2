import PySimpleGUI as sg

sg.theme('DarkBlue')

title = 'VIGENÉRE ENCODER & DECODER'
layout = [
    [sg.Text('', size=(20, 1)), sg.Text(title, justification='center', font=('Helvetica', 20)), sg.Text('', size=(20, 1))],
    [sg.Text('Enter text to encode or decode'), sg.Input(border_width=5, key='input')],
    [sg.T(' ', size=(1,1))],
    [sg.Text('Key: '), sg.Input(pad=(10, 0), border_width=5, key='key')],
    [sg.Text('', key='decode-or-encode', font=('Roboto', 20)), sg.Text(key='value', font=('Roboto', 20)), sg.Button('Copy', visible=False)],
    [sg.Button('Encrypt'), sg.Button('Decrypt')],
    [sg.Button('Quit')]
]

window = sg.Window(title, layout, element_justification='center')

while True:
    event, values = window.read()

    if event == 'Quit' or event == sg.WIN_CLOSED:
        break

    if event == 'Copy':
        sg.clipboard_set(window['value'].get())

    if ((event == 'Encrypt' or event == 'Decrypt') and ' ' in values['key']):
        sg.popup('There must be no spaces in key!', non_blocking=True)
        continue

    if (event == 'Encrypt' or event == 'Decrypt') and (values['input'] == '' or values['key'] == ''):
        sg.popup('Text and key must be filled first!', non_blocking=True)
        continue