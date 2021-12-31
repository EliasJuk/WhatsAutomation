from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
import pandas as pd
import os

root_path = os.getcwd()

driver = webdriver.Chrome()

# INICIA AUTOMATIZAÇÃO
def iniciar():
  planilha_contatos()

# CARREGA A PLANILHA COM CONTATOS
def planilha_contatos():
  tabela = pd.read_excel('contatos.xlsx', sheet_name='contatos')
  buscar_contatos(tabela)

def buscar_contatos(tabela):
  maxContatos = len(tabela.index)  
  for x in range(maxContatos):
    whatsapp(tabela.Nome[x], tabela.Numero[x])

def whatsapp(nome, numero):
  # ENTRAR NO SITE DO WHATSAPP
  driver.get('https://web.whatsapp.com/')
  time.sleep(4)

  # ENVIA MENSAGEM DE TEXTO
  texto = quote(f'olá {nome}, tudo bem com você')
  link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
  driver.get(link)
  time.sleep(4)
  enviar_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
  enviar_msg.send_keys(Keys.ENTER)
  time.sleep(2)
  enviar_img()
  
def enviar_img():
  time.sleep(4)
  driver.find_element_by_css_selector("span[data-icon='clip']").click()
  attach = driver.find_element_by_css_selector("input[type='file']")
  attach.send_keys(f'{root_path}/midia.png')
  time.sleep(1)
  send = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')
  send.send_keys(Keys.ENTER)
  time.sleep(2)

iniciar()