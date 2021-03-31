import PySimpleGUI as sg
import requests
import re
from os import system

class Tela:
    def __init__(self):
        layout = [
            [sg.T("URL"), sg.Input('http://www.',key="URL")],
           # [sg.Checkbox("procurar por kinks", key="links")],
            [sg.Checkbox("mostrar toda a pagina", key="mostrar_pg")],
            [sg.Checkbox("mostrar todos os links da pagina", key="mostrar_lks")],
            [sg.Output(size=(80, 15))],
            [sg.Button('comecar')]
            

        ]
        self.janela = sg.Window("webC").layout(layout)

    def Iniciar(self):
        while True:
        
            self.event, self.values = self.janela.Read()
            if self.event == sg.WIN_CLOSED:
                break
            
            #sair = self.values["sair"]
            #confirmar = self.values["comecar"]
            mostrar_lks = self.values["mostrar_lks"]
            mostrar_pg = self.values["mostrar_pg"]
            #links = self.values["links"]
            url = self.values["URL"]

#=========================================================================================================
            pagina = requests.get(url)
            pagina_fld = pagina.text
            if mostrar_pg == True:
                print(f"{pagina_fld} ")
            if mostrar_lks == True:
                links_pg = re.findall(r'(?<=href=["\'])https?://.+?(?=["\'])', pagina_fld, re.IGNORECASE)
                system('cls')
                for i in range(20):
                    print('\n')
                for link in links_pg:
                    print(f'\n{link}')
                    
                    
                    

#===========================================================================================================                                    


            
tela = Tela()
tela.Iniciar()