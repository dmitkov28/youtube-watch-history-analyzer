import dash
from dash import html
from dash import dcc
from pandas import Series
import plotly.graph_objects as go
from app.web.components import bar_chart, indicator
from app.data import total_videos_watched, avg_videos_per_day, top_videos

dash.register_page(__name__, path="/videos", name="Videos")


layout = html.Div(
    [
        html.H1(children="Videos", style={"textAlign": "center"}),
        html.Div(
            [
                indicator(dcc, go, total_videos_watched, "Total Videos Watched"),
                indicator(dcc, go, avg_videos_per_day, "Average Videos per Day"),
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "maxHeight": "320px",
            },
        ),
        html.Div(
            [
                html.Div(
                    [
                        bar_chart(
                            dcc,
                            go,
                            data_x=Series(top_videos.values),
                            data_y=Series(top_videos.index),
                            orientation="h",
                            options={
                                "title": "Most Watched YouTube Videos",
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
        ),
    ]
)
