import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup



s= Service(ChromeDriverManager().install())
opc=Options()
opc.add_argument("--windows-size=1020,1200")

navegador=webdriver.Chrome(service=s,options=opc)
navegador.get("http://www.olympedia.org/statistics/medal/country")


cb_year= navegador.find_element(By.NAME,"edition_id")
cb_genero=navegador.find_element(By.NAME, "athlete_gender")
genero_opc=cb_genero.find_elements(By.TAG_NAME,"option")

grupos_year=cb_year.find_elements(By.TAG_NAME,"optgroup")
lista_year=grupos_year[0].find_elements(By.TAG_NAME,"option")

datos={
    "country":[],
    "year":[],
    "gender":[],
    "gold":[],
    "silver":[],
    "bronze":[],
    "total":[]
}


for gender in genero_opc[1:2]:
    gender.click()
    for year in lista_year:
        year.click()
        time.sleep(2)


        sopas=BeautifulSoup(navegador.page_source,"html.parser")
        tabla=sopas.find("table",attrs={"class":"table table-striped"})
        list_Rows=tabla.find_all("tr")

        for row in list_Rows[1:]:
            datos["gender"].append(gender.text)
            datos["year"].append(year.text)
            values=row.find_all("td")
            datos["country"].append(values[0].text)
            datos["gold"].append(values[2].text)
            datos["silver"].append(values[3].text)
            datos["bronze"].append(values[4].text)
            datos["total"].append(values[5].text)


navegador.close()


data_df=pd.DataFrame(datos)


data_df.to_csv("DATA/DATA_OLIMPIADAS.csv")