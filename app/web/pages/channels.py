from pandas import Series
import plotly.graph_objects as go
import dash
from dash import html, dcc
from app.data import top_channels
from app.web.components import bar_chart

dash.register_page(__name__, path="/channels", name="Channels")

layout = html.Div(
    [
        html.H1(children="Channels", style={"textAlign": "center"}),
        html.Div(
            [
                bar_chart(
                    dcc,
                    go,
                    data_x=Series(top_channels.values),
                    data_y=Series(top_channels.index),
                    orientation="h",
                    options={
                        "title": "Most Watched YouTube Channels",
                        "title_x": 0.5,
                        "height": 1200,
                        "yaxis": dict(
                            automargin=True,
                            tickmode="linear",
                            showticklabels=True,
                        ),
                        "margin": dict(
                            l=300,
                        ),
                    },
                )
            ]
        ),
    ]
)
