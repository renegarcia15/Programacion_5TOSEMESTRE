import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--windows-size=1020,1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://www.amazon.com.mx/")

producto = input("Qué producto vas a buscar---> ")
num_paginas = int(input("Número de páginas a buscar---> "))

txt = navegador.find_element(By.ID, "twotabsearchtextbox")
txt.send_keys(producto)
buscar = navegador.find_element(By.ID, "nav-search-submit-button")
buscar.click()

datos_totales = pd.DataFrame()

for _ in range(num_paginas):
    sopas = BeautifulSoup(navegador.page_source, "html.parser")
    resultados = sopas.find_all("div", class_="s-result-item")

    datos = {
        "nombre": [],
        "rating": [],
        "precio": [],
        "fecha de entrega": []
    }

    for resultado in resultados:
        nombre_producto = resultado.find("span", class_="a-text-normal")
        calificacion = resultado.find("span", class_="a-icon-alt")
        precio = resultado.find("span", class_="a-price")
        fecha_entrega_elemento = resultado.find("span", class_="a-text-bold")

        nombre = nombre_producto.text.strip() if nombre_producto else "N/A"
        rating = calificacion.text.strip() if calificacion else "N/A"
        precio = precio.find("span", class_="a-offscreen").text.strip() if precio else "N/A"
        fecha_entrega = fecha_entrega_elemento.text.strip() if fecha_entrega_elemento else "N/A"

        datos["nombre"].append(nombre)
        datos["rating"].append(rating)
        datos["precio"].append(precio)
        datos["fecha de entrega"].append(fecha_entrega)

    informacion_pagina = pd.DataFrame(datos)
    datos_totales = pd.concat([datos_totales, informacion_pagina], ignore_index=True)

    siguiente_pagina = navegador.find_element(By.PARTIAL_LINK_TEXT, "Siguiente")
    siguiente_pagina.click()

navegador.close()

nombre_archivo ="Amazon.csv"
datos_totales.to_csv(nombre_archivo, index=False)

#SPLIT EN LA CALIFICACION APRA QUE SOLO SALGA EL NUMERO