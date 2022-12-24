'''
app.py: Entry point to our file
'''

from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import dash
import sys
sys.path.append("layout_components/")
#from navbar import navbar_simple
from navbar import NavBar

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


navbar = NavBar(navbar_title="Covid Dashboard")
navbar_simple = navbar.simpleNavBar(linkinfo_list = [{"link_name": "Link", "link_url": "#"}, {"link_name": "Link1", "link_url": "#"}])

#default = dbc.NavbarSimple(children=[dbc.NavItem(dbc.NavLink("Link", href="#"))], brand="Covid Dashboard", brand_href="#", sticky="top", color="dark", dark=True, className="mb-5")

app.layout = html.Div([navbar_simple])

if __name__ == '__main__':
    app.run_server(debug=True)
