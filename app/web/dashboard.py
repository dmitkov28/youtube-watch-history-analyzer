import dash
import dash_mantine_components as dmc
from dash import Dash, html

app = Dash(__name__, use_pages=True, external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    html.Div(
        [
            dash.page_container,
        ]
    )
)
