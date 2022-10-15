#Programinha para fins de estudos, automatizar a tarefa de bater ponto online
#Já consigo treinar Python e WebScrapping na mesma paulada
#Inicio: 14/10/22 (faz input nos dois campos)


from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

#Instalando driver do browser
service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

#Requisitando a URL desejada
driver.get("https://app.tangerino.com.br/Tangerino/pages/baterPonto")

#Variaveis para registrar o ponto (codigo empregador e senha do funcionario)
employee_code = 'woooo'
employee_passwd = str("1341")

#Input na página
employee_box = driver.find_element(By.ID, 'codigoEmpregador').send_keys(employee_code)
employee_box2 = driver.find_element(By.ID, 'codigoPin').send_keys(employee_passwd)

#clicando na confirmação
confirm_box = driver.find_element(By.CLASS_NAME, 'btnLogin ladda-button').click

