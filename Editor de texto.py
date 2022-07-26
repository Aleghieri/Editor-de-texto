import PySimpleGUI as sg
import os
import pathlib

def create_main_window():
    sg.theme('DarkTeal6')
    layout = [         
        [
            sg.Text('Bem vindo ao nosso editor de texto'),
        ],
        [
            sg.Text('Nome do arquivo'),
            sg.Input(key= '-NAME-'),
            sg.Radio('.py', group_id='extension', key='-PY-', default=True),
            sg.Radio('.txt', group_id='extension', key='-TXT-'),
        ],
        [
            sg.Multiline(key='-CONTENT-', size=(150,30))
        ],
        [
            sg.Button(('Salvar arquivo'), key='-SAVE-', size=(133, None))
        ]
        
    ]
       
        
    title = 'Editor de Texto Simples'

    window = sg.Window(title, layout,element_justification='center')

    return window


window = create_main_window()

while True:
    event, values = window.read()

    if event == '-SAVE-':
        if values['-PY-']:
            extension = '.py'
        else:
            extension = '.txt'
        
        filename = values['-NAME-'] + extension
        content = values['-CONTENT-']
        
        folder = 'Arquivos Salvos'
        
        parent_path = pathlib.Path(__file__).parent.resolve()
        
        path = os.path.join(parent_path,folder)
        
        
        
        if not os.path.isdir(path):
            os.makedirs(path)
        
        fullpath = os.path.join(path,filename)
        
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    if event == sg.WIN_CLOSED:
        break

