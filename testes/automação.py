import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
 
def Objeto():
    options = webdriver.EdgeOptions()
    navegador = webdriver.Edge(options=options)
    navegador.get("https://lojasrenner.blip.ai/check")
    time.sleep(5)
    navegador.find_element(By.XPATH, '//button').click()
    time.sleep(3)
    actions = ActionChains(navegador)
    actions.send_keys(Keys.SPACE).perform()
    time.sleep(2)
    verificaBrowser = navegador.find_element(By.XPATH, 'li[1]')
    time.sleep(2)
    conexMsgin = navegador.find_element(By.XPATH, 'li[2]')
    time.sleep(2)
    conexBlip = navegador.find_element(By.XPATH, 'li[3]')
    time.sleep(2)
    conex0mn = navegador.find_element(By.XPATH, 'li[4]')
    time.sleep(2)
    conexExternal = navegador.find_element(By.XPATH, 'li[5]')
    time.sleep(1)
   
    formatVerificaBrowser = verificaBrowser.text[::-1][0:8][::-1]
    formatConexMsgin = conexMsgin.text[::-1][0:8][::-1]
    formatConexBlip = conexBlip.text[::-1][0:8][::-1]
    formatConex0mn = conex0mn.text[::-1][0:8][::-1]
    formatConexExternal = conexExternal.text[::-1][0:8][::-1]
    print(f'Verificação do Browser: {formatVerificaBrowser}')
    print('-=' * 10)
    print(f'Sua conexão com o lojasrenner.ws.msging.net: {formatConexMsgin}')
    print('-=' * 10)
    print(f'Sua conexão com o lojasrenner.ws.blip.ai: {formatConexBlip}')
    print('-=' * 10)
    print(f'Sua conexão com o lojasrenner.ws.blip.ai: {formatConex0mn}')
    print('-=' * 10)
    print(f'Sua conexão com o lojasrenner.ws.blip.ai: {formatConexExternal}')
 
Objeto()
