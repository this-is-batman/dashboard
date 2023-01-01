'''
app.py: Entry point to our file
'''

from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import dash
import sys
sys.path.append("layout_components/")
from navbar import NavBar

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

# ----- Components of the app are defined here ---------------------

navbar = NavBar(navbar_title="My Dashboard")
navbar_simple = navbar.simpleNavBar(linkinfo_list = [{"link_name": "Link", "link_url": "/"}, {"link_name": "Card Analysis", "link_url": "/cards"}])

# -------- defining the layout of the app ---------------------------
app.layout = html.Div([navbar_simple, dash.page_container])

if __name__ == '__main__':
    app.run_server(debug=True)
