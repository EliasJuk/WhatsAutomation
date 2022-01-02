import PIL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
import pandas as pd
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import threading

root_path = os.getcwd()

# CARREGA DRIVER E ENTRA NO SITE DO WHATSAPP
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# IMAGEM PADRÃO
image_path = f'{root_path}/midia.png'

root = Tk()

def gui():
  # CONFIGURAÇÕES DA GUI
  root.title('WhatsAutomation')
  root.geometry("400x600")
  root.resizable(False, False)
  root.configure(bg='#e1e1e1')
  root.grid_columnconfigure((0, 6), weight=1)
  
  # LABEL ACIMA DA CAIXA DE TEXTO
  text_label1 = Label(root, text='Mensagem a ser enviada:', bg='#e1e1e1', pady=10, padx=10)
  text_label1.grid(column=1, row=0)

  # CAIXA DE TEXTO
  textBox = Text(root, height = 10, width = 40, bg='#d4d4d4', pady=10, padx=10, font='sans-serif')
  textBox.grid(column=1, row=1, pady=10)

  # FUNÇÃO PARA CARREGAR A IMAGEM
  
  def file_open():
    try:
      path=filedialog.askopenfilename(initialdir='C://')
      new_image = ImageTk.PhotoImage(Image.open(path))
      panel.configure(image=new_image)
      panel.image = new_image
      
      global image_path
      image_path = path
      
    except AttributeError:
      print('Selecione uma imagem')
    except PIL.UnidentifiedImageError:
      print('Formato invalido')

  # FUNÇÃO QUE DESABILITA O ENVIO DE IMAGENS
  def print_selection():
    if (var1.get() == 1):
      button_open_file.config(state=NORMAL)
      panel.config(state=NORMAL)

    else:
      button_open_file.config(state=DISABLED)
      panel.config(state=DISABLED)
  
  # BOTÃO OPEN FILE
  button_open_file = Button(root, text='Open file', bg='#d4d4d4', command=file_open, state=DISABLED)
  button_open_file.grid(column=1, row=2)

  #CHECK BOX
  global var1
  var1 = IntVar()
  checkbox = Checkbutton(root, text='Enviar Imagem',variable=var1, onvalue=1, offvalue=0, command=print_selection, bg='#e1e1e1', pady=10)
  checkbox.grid(column=1, row=3)

  # CARREGA A IMAGEM
  image_path = Image.open('midia.png')
  imagem = ImageTk.PhotoImage(image_path)
  panel = Label(root, image=imagem, bg='#d4d4d4', state= DISABLED, width=200, height=200)
  panel.place(x=0, y=0)
  panel.grid(column=1, row=4)

  def send_mensagem():
    textBox_inputValue=textBox.get("1.0","end-1c")
    checkbox_value = var1.get()

    # IMPLEMENTAR THREADS
    threading.Thread(target=automacao, args=(textBox_inputValue, checkbox_value)).start()
    #automacao(inputValue, checkbox_value)
  
  # BOTÃO SEND FILE
  button_send_msg = Button(root, text='ENVIAR', command=send_mensagem, bg='#54EF6F', padx=5, pady=5, font=10)
  button_send_msg.grid(column=1, row=5, pady=10)

  # LOOP
  root.mainloop()

def automacao(msg, checkbox_value):
  root.update()
  mensagem = msg
  
  # CARREGA A PLANILHA COM CONTATOS
  def planilha_contatos():
    tabela = pd.read_excel('contatos.xlsx', sheet_name='contatos')
    buscar_contatos(tabela)

  # PEGA NOME E CONTATO NA PLANILHA
  def buscar_contatos(tabela):
    maxContatos = len(tabela.index)  
    for x in range(maxContatos):
      whatsapp(tabela.Nome[x], tabela.Numero[x])

  def whatsapp(nome, numero, ):
    # ENVIA MENSAGEM DE TEXTO
    texto = quote(f'{mensagem}')
    
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    driver.get(link)
    time.sleep(4)
    enviar_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    enviar_msg.send_keys(Keys.ENTER)
    time.sleep(2)
    enviar_img()
  
  def enviar_img():
    if checkbox_value == 1:
      time.sleep(4)
      driver.find_element_by_css_selector("span[data-icon='clip']").click()
      attach = driver.find_element_by_css_selector("input[type='file']")
      attach.send_keys(image_path)
      time.sleep(1)
      send = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')
      send.send_keys(Keys.ENTER)
      time.sleep(2)
    else:
      pass

  planilha_contatos()

#iniciar()
gui()