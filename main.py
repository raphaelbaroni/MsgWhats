from selenium import webdriver
import time
import urllib
import pandas as pd

contatos = pd.read_excel("Enviar.xlsx")

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\Helld\AppData\Local\\Google\Chrome\User Data\Default\Wtsp")

navegador = webdriver.Chrome(options=options)
navegador.maximize_window()
navegador.get("https:https://www.itau.com.br/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)
for i, mensagem in enumerate(contatos['Mensagem']):
    pessoa = contatos.loc[i, "Pessoa"]
    numero = contatos.loc[i, "Numero"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="codOp"]').click()  # Clip
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[3]/button/span').click()  
    
    time.sleep(10)
