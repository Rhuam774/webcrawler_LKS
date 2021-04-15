import PySimpleGUI as sg
import requests
import re
from os import system
nP = 1
class Tela:
    def __init__(self):
        layout = [
            [sg.T("URL"), sg.Input('http://www.',key="URL")],
            [sg.Checkbox("mostrar toda a pagina", key="mostrar_pg")],
            [sg.Checkbox("mostrar todos os links da pagina", key="mostrar_lks")],
            [sg.Output(size=(80, 15))],
            [sg.Button('comecar')]
        ]
        self.janela = sg.Window("webC").layout(layout)

    def Iniciar(self):
        global nP
        
        while True:
            self.event, self.values = self.janela.Read()

            if self.event == sg.WIN_CLOSED:
                break
            mostrar_lks = self.values["mostrar_lks"]
            mostrar_pg = self.values["mostrar_pg"]
            url = self.values["URL"]
#=========================================================================================================
            pagina = requests.get(url)
            pagina_fld = pagina.text

            if mostrar_pg == True:
                print(f"{pagina_fld} ")

            if mostrar_lks == True:
                links_pg = re.findall(r'(?<=href=["\'])https?://.+?(?=["\'])', pagina_fld, re.IGNORECASE)
                system('cls')
                print('\n======================================================================')
                print(f'============================ {nP}° pesquisa ================================\n')
                print(f'Resultados de:   {url}\n----------------------------------------------------------------------------------------------------------\n')

                for link in links_pg:
                    print(f'\n{link}')
                print('======================================================================\n')
                nP += 1
#===========================================================================================================
tela = Tela()
tela.Iniciar()