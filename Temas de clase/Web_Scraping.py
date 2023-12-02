#Selenium


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s= Service(ChromeDriverManager().install())
opc=Options()
opc.add_argument("--windows-size=1020,1200")



navegador=webdriver.Chrome(service=s,options=opc)
navegador.get("https://es-la.facebook.com/")
txt=navegador.find_element(By.NAME,"email")
txt.send_keys("usuario@yahoo.com")
time.sleep(2)
password=navegador.find_element(By.NAME,"pass")
password.send_keys("Tainy")
time.sleep(2)
navegador.save_screenshot("prueba.png")
sesion=navegador.find_element(By.NAME,"login")
sesion.click()

navegador.find_elements()


print(navegador.title)

time.sleep(5)