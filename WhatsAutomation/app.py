from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

driver = webdriver.Chrome()

# ENTRAR NO SITE DO WHATSAPP
driver.get('https://web.whatsapp.com/')
time.sleep(4)

# ENVIA MENSAGEM DE TEXTO
nome = 'Elias'
numero = '554200000000'
texto = quote(f'olá {nome}, tudo bem com você')
link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
driver.get(link)
time.sleep(4)
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)