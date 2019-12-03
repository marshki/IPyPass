#!/usr/bin/env python3

import PySimpleGUI as sg      

sg.change_look_and_feel('Reddit')    

layout = [[sg.Text('Enter IP address:')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('IPyPass:', layout)      

while True:                             
    event, values = window.read() 
    print(event, values)       
    if event in (None, 'Exit'):      
        break      

window.close()
