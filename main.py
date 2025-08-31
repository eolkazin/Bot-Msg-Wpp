from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Ler números
df = pd.read_excel('seu_arquivo.xlsx')
numeros = df['sua_coluna'].tolist()
mensagem = "Olá, tudo certo?"

# Abrir WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter")

for numero in numeros:
    url = f"https://web.whatsapp.com/send?phone=55{numero}&text={mensagem}"
    driver.get(url)
    time.sleep(8)  # esperar a página carregar
    send_btn = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/button')
    send_btn.click()
    time.sleep(2)

driver.quit()
