'''
navbar.py: Script containing the code to create a navbar in Dash
'''

import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, Dash
from dash_bootstrap_components._components.Container import Container

class NavBar:
    def __init__(self, navbar_title,navbar_href = "#",color="#4d46d2"):
        '''
        Input: Title of the navbar, default color of the navbar
        '''
        self.navbar_title = navbar_title
        self.navbar_href = navbar_href
        self.color = color

    def simpleNavBar(self,linkinfo_list):
        '''
        Input: List containing the dictionaries containing information about the links (name and url) 
        output: Return the simple nav bar
        '''
        links_list = [dbc.NavItem(dbc.NavLink(link_inf["link_name"], href=link_inf["link_url"])) for link_inf in linkinfo_list]
        navbar_simple = dbc.NavbarSimple(children=links_list, brand=self.navbar_title, brand_href=self.navbar_href, color = self.color, dark=True, id="navbar")
        return navbar_simple


if __name__ == '__main__':
    pass
