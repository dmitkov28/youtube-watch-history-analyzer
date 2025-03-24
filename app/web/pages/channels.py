from pandas import Series
import plotly.graph_objects as go
import dash
from dash import html, dcc
from app.data import top_channels
from app.web.components import bar_chart

dash.register_page(__name__, path="/channels", name="Channels")

layout = html.Div(
    [
        html.Div(
            html.H1("Top YouTube Channels", className="dashboard-title"),
            className="header-container",
        ),
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
                            tickfont={"size": 14, "family": "Arial, sans-serif"},
                        ),
                        "xaxis": dict(
                            title="Views",
                            tickfont={"size": 14},
                        ),
                        "margin": dict(
                            l=300,
                            r=50,
                            t=80,
                            b=50,
                        ),
                        "paper_bgcolor": "rgba(0,0,0,0)",
                        "plot_bgcolor": "rgba(0,0,0,0)",
                        "colorway": [
                            "#636EFA",
                            "#EF553B",
                            "#00CC96",
                            "#AB63FA",
                            "#FFA15A",
                        ],
                    },
                )
            ],
            className="chart-container",
        ),
    ],
    className="dashboard-container",
    style={
        "maxWidth": "1200px",
        "margin": "0 auto",
        "padding": "20px",
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f9f9f9",
        "borderRadius": "10px",
        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
    },
)
