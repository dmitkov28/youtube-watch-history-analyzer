import dash
from dash import html

dash.register_page(__name__, path="/", name="Home")

layout = html.H1(children="Home", style={"textAlign": "center"})
