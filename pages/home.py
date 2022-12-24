'''
home.py: Script containing the layout of the home page
'''

import dash
from dash import html, dcc, Dash, Input, Output, callback
import pandas as pd
import plotly.express as px
import os.path
path = os.path.abspath(__file__)
source_code_location = os.path.dirname(os.path.dirname(path))

dash.register_page(__name__, path='/')

df = pd.read_csv(source_code_location + "/data/avocado-updated-2020.csv")

geo_locations = df["geography"].unique()

geo_dropdown = dcc.Dropdown(options = geo_locations, value="New York")

layout = html.Div(children=[html.H1(children="This is our Home page."), html.Div(children='''This is our Home page content.'''), geo_dropdown, dcc.Graph(id='price-graph')])

@callback(
        Output(component_id = 'price-graph', component_property='figure'),
        Input(component_id = geo_dropdown, component_property = 'value')
    )

def update_graph(selected_geo):
    filtered_loc = df[df["geography"] == selected_geo]
    fig = px.scatter(filtered_loc, x = "date", y = "average_price", color="type", title = f"Avocado prices in {selected_geo}")
    return fig

