from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path=r'C:\Users\pc\Downloads\edgedriver_win64\msedgedriver.exe')

driver.get("https://app.tangerino.com.br/Tangerino/pages/baterPonto/")

codigo_emprega = 'PWDIU'
pin_code = str(6462)

driver.find_element(By.ID("codigoEmpregador")).send_keys("ola")
driver.find_element(By.ID("codigoPin")).send_keys("123")
