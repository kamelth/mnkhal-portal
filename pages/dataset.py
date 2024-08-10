import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/dataset', name="Dataset 📋")

####################### LOAD DATASET #############################
titanic_df = pd.read_csv("mnkhal_machine_data.csv")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=titanic_df.to_dict('records'),
                         page_size=20,
                         style_cell={"background-color": "lightgrey", "border": "solid 1px white"},
                         style_header={"background-color": "dodgerblue", "font-weight": "bold"},
                        ),
])