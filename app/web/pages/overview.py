import dash
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
from app.data import (
    total_videos,
    avg_videos_per_day,
    avg_yt_music_per_day,
    total_yt_music,
    category_counts,
    heatmap_data,
    preferred_durations,
)
from app.web.components import heatmap, indicator, pie_chart
from app.web.components.bar_chart import bar_chart

dash.register_page(__name__, path="/overview", name="Overview")

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [indicator(dcc, go, total_videos, "Total Videos Watched")],
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
                            dcc,
                            go,
                            avg_yt_music_per_day,
                            "Average YT Music Videos per Day",
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
            pie_chart(category_counts, "category_title", "count", "Video Categories"),
            style={
                "backgroundColor": "#f8f9fa",
                "borderRadius": "10px",
                "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "padding": "15px",
            },
        ),
        html.Div(
            heatmap(
                px,
                heatmap_data,
                title="Watch Times Heatmap",
                legend_label="Videos Watched",
            ),
            style={
                "backgroundColor": "#f8f9fa",
                "borderRadius": "10px",
                "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "padding": "15px",
            },
        ),
        html.Div(
            [
                html.H1(
                    "Preferred Durations", className="text-xl font-bold text-center"
                ),
                bar_chart(
                    dcc,
                    go,
                    data_x=preferred_durations["duration_group"],
                    data_y=preferred_durations["videos"],
                    orientation="v",
                ),
            ]
        ),
    ],
    className="flex flex-col gap-y-3",
)
