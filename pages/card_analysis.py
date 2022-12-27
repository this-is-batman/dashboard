'''
card_analysis.py: Script containing the layouy of the card analysis page
'''

import dash
from dash import html, dcc, Dash, Input, Output, callback
import pandas as pd
import plotly.express as px
import os.path
path = os.path.abspath(__file__)
source_code_location = os.path.dirname(os.path.dirname(path))

dash.register_page(__name__, path='/cards')

df = pd.read_csv(source_code_location + "/data/card_transact.csv")

df["Data_value"].fillna(0, inplace=True)

dropdown = dcc.Dropdown(options = df["Period"].unique(), value = 2022.03)

layout = html.Div(children=[dropdown, dcc.Graph(id='value_graph')])

@callback(
        Output(component_id = 'value_graph', component_property='figure'),
        Input(component_id = dropdown, component_property = 'value')
)

def update_graph(selected_period):
    filtered_period = df[df["Period"] == selected_period]
    fig = px.scatter(filtered_period, x = "Series_reference", y = "Data_value", color="STATUS", title = f"Card transactions in {selected_period}.")
    return fig


