import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, callback, Input, Output


DATA=pd.read_csv("../DATA/DATA_oliimpiadas.csv", index_col=0)
def dashboard():

    data_Pais=DATA.groupby("country",as_index=False).sum(numeric_only=True)
    g1=px.line(data_Pais,x="country",y=["gold","silver","bronze"])
    body=html.Div([
        html.H2("Datos Olimpiadas"),html.P("Objetivo Dashboard: Mostrar los resultados de las medallas de los paises."),
        html.Hr(),
        dash_table.DataTable(data=DATA.to_dict("records"),page_size=10),#records es para procesarlos a un diccionario como lo requiere la funcion DataTable,
        dcc.Graph(figure=g1,id="figMedal"),
        dcc.Dropdown(options=["all","gold","silver","bronze"],
                     value="all",id="ddMedal")
    ])
    return body


@callback(
    Output(component_id="figMedal",component_property="figure"),
    Input(component_id="ddMedal",component_property="value")
)

def update_grafica(value_chosen):
    print(value_chosen)
    data_Pais = DATA.groupby("country", as_index=False).sum(numeric_only=True)
    col_chosen=value_chosen
    if value_chosen=="all":
       col_chosen =["gold", "silver", "bronze"]
       fig = px.line(data_Pais, x="Country", y=value_chosen)
    return fig

if __name__=="__main__":
    app=Dash(__name__)
    app.layout=dashboard()
    app.run(debug=True) #El debug es que esta en desarrollo, si vas a vender le debes de quitar el debug
