import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, callback, Input, Output
import dash_bootstrap_components as dbc


DATA=pd.read_csv("../DATA/DATA_oliimpiadas.csv", index_col=0)
def dashboard():

    data_Pais=DATA.groupby("country",as_index=False).sum(numeric_only=True)
    g1=px.line(data_Pais,x="country",y=["gold","silver","bronze"])
    body=html.Div([
        html.H2("Datos Olimpiadas"),html.P("Objetivo Dashboard: Mostrar los resultados de las medallas de los paises."),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H3("Filtros"),
                        tarjeta_filtros()
                    ]),width=3
                ),
                dbc.Col(
                    html.Div([
                        dbc.Row(dcc.Graph(figure=g1,id="figMedal")),
                        dbc.Row(dash_table.DataTable(data=DATA.to_dict("records"),page_size=10),#records es para procesarlos a un diccionario como lo requiere la funcion DataTable,
)
                    ])
                ),
            ]
        ),
    ])
    return body

def tarjeta_filtros():
    control=dbc.Card([
        html.Div([
            dbc.Label("Gender: "),
            dcc.Dropdown(options=["All","Male","Female"],value="All")
        ]),
        html.Div([
            dbc.Label("Medalla: "),
            dcc.Dropdown(options=["all", "gold", "silver", "bronze"],
                         value="all", id="ddMedal"),
        ]),
        html.Div([dbc.Label("Year: "),
                 dbc.Input(type="number",min=1940,max=2023)])
    ])
    return control

if __name__=="__main__":
    app=Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
    app.layout=dashboard()
    app.run(debug=True)