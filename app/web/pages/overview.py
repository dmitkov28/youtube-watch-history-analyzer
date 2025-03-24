import dash
from dash import html, dcc
import plotly.graph_objects as go
from app.data import (
    total_videos_watched,
    avg_videos_per_day,
    total_yt_music,
    avg_yt_music,
    categories,
)
from app.web.components import indicator, pie_chart

dash.register_page(__name__, path="/overview", name="Overview")

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [indicator(dcc, go, total_videos_watched, "Total Videos Watched")],
                    style={
                        "width": "48%",
                        "backgroundColor": "#f8f9fa",
                        "borderRadius": "10px",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        "padding": "15px",
                    },
                ),
                html.Div(
                    [indicator(dcc, go, avg_videos_per_day, "Average Videos per Day")],
                    style={
                        "width": "48%",
                        "backgroundColor": "#f8f9fa",
                        "borderRadius": "10px",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        "padding": "15px",
                    },
                ),
            ],
            className="flex justify-between max-h-fit",
        ),
        html.Div(
            [
                html.Div(
                    [
                        indicator(
                            dcc, go, total_yt_music, "Total YT Music Videos Watched"
                        )
                    ],
                    style={
                        "width": "48%",
                        "backgroundColor": "#f8f9fa",
                        "borderRadius": "10px",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        "padding": "15px",
                    },
                ),
                html.Div(
                    [
                        indicator(
                            dcc, go, avg_yt_music, "Average YT Music Videos per Day"
                        )
                    ],
                    style={
                        "width": "48%",
                        "backgroundColor": "#f8f9fa",
                        "borderRadius": "10px",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        "padding": "15px",
                    },
                ),
            ],
            className="flex justify-between max-h-fit",
        ),
        html.Div(
            pie_chart(categories, "category_title", "id", "Video Categories"),
            style={
                "backgroundColor": "#f8f9fa",
                "borderRadius": "10px",
                "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "padding": "15px",
            },
        ),
    ],
    className="flex flex-col gap-y-3",
)
