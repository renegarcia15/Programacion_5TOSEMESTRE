"""Garcia Soto Rene
Fecha: 09/09/23
Realizar una función en python que reciba el nombre de un producto en Amazon y automatice la busqueda del producto.
 El script debe tomar una impresión de pantalla despues de realizar la busqueda."""
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
navegador.get("https://www.amazon.com.mx/")
txt=navegador.find_element(By.ID,"twotabsearchtextbox")
producto=input("Que producto vas a buscar---> ")
txt.send_keys(producto)
time.sleep(2)
buscar=navegador.find_element(By.ID,"nav-search-submit-button")
buscar.click()
navegador.find_elements()
navegador.save_screenshot("Producto.png")
print(navegador.title)
time.sleep(3)