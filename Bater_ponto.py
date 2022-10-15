from argparse import Action
from selenium.webdriver.common.keys import Keys
from ssl import Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

#Instalando driver do browser
service = FirefoxService(executable_path=GeckoDriverManager().install())
options = FirefoxOptions()
options.set_preference("dom.push.enabled", False); options.set_preference("dom.webnotifications.enabled", False)
options.set_preference('javascript.enabled', True) #se ficar false o site n da a confirmacao
driver = webdriver.Firefox(options=options, service=service)

#Requisitando a URL desejada
driver.get("https://app.tangerino.com.br/Tangerino/pages/baterPonto")

#Variaveis para registrar o ponto (codigo empregador e senha do funcionario)
employee_code = 'woooo'
employee_passwd = str("1341")

#Input na página
employee_box = driver.find_element(By.ID, 'codigoEmpregador').send_keys(employee_code)
employee_box2 = driver.find_element(By.ID, 'codigoPin').send_keys(employee_passwd)


driver.find_element(By.ID, 'codigoPin').send_keys(Keys.TAB)

driver.find_element(By.ID, 'registraPonto').click

#driver.find_element(By.ID, 'registraPonto').send_keys(Keys.ENTER)



