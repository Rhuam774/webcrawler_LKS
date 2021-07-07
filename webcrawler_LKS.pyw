#RHUAM PFC
#webcrawler_LINKS                         #--/--/---
#------------------------------------------------------------

from os import system
from time import sleep
import re
from tkinter import Label, colorchooser
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import COLOR_SCHEME, COLOR_SYSTEM_DEFAULT, CUSTOM_TITLEBAR_TEXT_COLOR, theme_text_color, theme_text_element_background_color
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
##########################################

nP = 1
class Tela:
    def __init__(self):
        layout = [
            [sg.T("URL"), sg.Input('http://www.',key="URL")],
            [sg.Checkbox("mostrar toda a pagina", key="mostrar_pg")],
            [sg.Checkbox("mostrar todos os links da pagina", key="mostrar_lks")],
            [sg.Checkbox('-'*23+"\n**ir para o site**\n"+'-'*23, text_color=('lightblue'), key="ir_site",), sg.Checkbox('manter navegadores abertos.',key="nvd_A", text_color=('lightblue'))],
            
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
            ir_site = self.values["ir_site"]
            url = self.values["URL"]
            nvg_A = self.values["nvd_A"]
#=========================================================================================================
            try:
                pagina = requests.get(url)
                pagina_fld = pagina.text
            except Exception as erro:
                print(f"Erro: {erro}\n Tente colocar uma url valida usando https://")

            if mostrar_pg == True:
                try:   
                    print(f"{pagina_fld} ")
                except Exception as erro:
                    print(f"Erro: {erro}\n Tente colocar uma url valida usando https://")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!            
            if ir_site == True:
                if nvg_A == False:
                    try:
                        navegador.quit()
                        navegador.quit()
                        navegador.quit()
                    except Exception as erro:
                        print('\n')
                try:
                    navegador = webdriver.Chrome()
                    navegador.get(url)
                except Exception as erro:
                    print(f"Erro: {erro}\n Tente colocar uma url valida usando https://")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if mostrar_lks == True:
                try:
                    links_pg = re.findall(r'(?<=href=["\'])https?://.+?(?=["\'])', pagina_fld, re.IGNORECASE)
                    system('cls')
                    print('\n'+'~' * 70)
                    print(f'============================ {nP}° pesquisa ================================\n')
                    Rps = (f' Resultados de {url}:\n')
                    print(Rps +'/'+'T' * len(Rps) + '\ \n')

                    for link in links_pg:
                        print(f'\n{link}')
                    print('=' * 70 + '\n')
                    nP += 1
                except Exception as erro:
                    print(f"Erro: {erro}\n Tente colocar uma url valida usando https://")
#===========================================================================================================
tela = Tela()
tela.Iniciar()