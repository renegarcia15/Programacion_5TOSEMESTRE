"""
Alumno: Garcia Soto Rene Grupo: 951
Fecha:24/09/23
Descripcion: Automatizar el proceso de login en la pagina de https://pypi.org/account/login/.
La cual contiene una caja de texto con id username para el nombre de usuario; una caja de texto con id password para la contraseña y el botón de acceder
 (loging) con la clase “button.button—primary”. Después de loguearse debe tomar una impresión de pantalla.
"""
#Selenium para facebook
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
navegador.get("https://pypi.org/account/login/")
txt=navegador.find_element(By.ID,"username")
txt.send_keys("examen@outlook.com")
time.sleep(2)
password=navegador.find_element(By.ID,"password")
password.send_keys("Tainy")
time.sleep(2)
navegador.save_screenshot("prueba.png")
sesion=navegador.find_element(By.CLASS_NAME,"button.button--primary")
sesion.click()

navegador.find_elements()


print(navegador.title)

time.sleep(5)

time.sleep(5)





















