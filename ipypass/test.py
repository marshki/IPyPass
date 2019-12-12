import PySimpleGUI as sg      

layout = [ [sg.Txt('Enter IP address:')],      
            [sg.In(size=(8,1), key='eight_bit')],      
            [sg.Txt('', size=(8,1), key='output')  ],      
            [sg.Button('Convert', bind_return_key=True)]]      

window = sg.Window('IPyPass', layout)      

while True:      
    event, values = window.read()      

    if event is not None:      
        try:      
            eight_bit = str(values['eight_bit'])      
            calc = eight_bit  
        except:      
            calc = 'Invalid'      

        window['output'].update(calc)      
    else:      
        break      
