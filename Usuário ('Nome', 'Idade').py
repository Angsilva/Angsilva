#!/usr/bin/env python
# coding: utf-8

# In[4]:


import PySimpleGUI as sg

class telapyton:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button('OK')]
        ]
             
        # janela
        janela = sg.Window("Dados do Usuário").layout(layout)
               
        
        # dados
        self.Button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = telapyton()
tela.Iniciar()


# In[ ]:




