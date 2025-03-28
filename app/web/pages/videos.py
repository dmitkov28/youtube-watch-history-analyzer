import dash
import datetime
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html
from pandas import Series

from app.data import (
    top_videos,
    videos_timeline,
    subbed_vs_unsubbed,
    word_cloud_data,
    longest_video,
)
from app.web.components import bar_chart, card, line_chart, pie_chart, word_cloud

dash.register_page(__name__, path="/videos", name="Videos")

layout = html.Div(
    [
        html.H1(
            children="Videos Dashboard",
            style={
                "textAlign": "center",
                "marginBottom": "30px",
                "marginTop": "20px",
                "color": "#2c3e50",
                "fontWeight": "bold",
            },
        ),
        html.Div(
            [
                line_chart(
                    px,
                    videos_timeline,
                    x_col_name="timestamp",
                    y_col_name="count",
                    title="Weekly Videos Watched",
                )
            ],
            style={
                "marginBottom": "30px",
                "padding": "15px",
                "backgroundColor": "#f8f9fa",
                "borderRadius": "10px",
                "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
            },
        ),
        html.Div(
            pie_chart(
                subbed_vs_unsubbed,
                "is_subscribed",
                "count",
                "Watched Videos (Subscribed vs Unsubscribed Channels)",
            )
        ),
        html.Div(
            word_cloud(
                go,
                word_cloud_data,
                "Video Titles Wordcloud",
            )
        ),
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
                        "margin": dict(l=300, r=50, t=70, b=50),
                    },
                )
            ],
            style={
                "backgroundColor": "#f8f9fa",
                "borderRadius": "10px",
                "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "padding": "15px",
            },
        ),
        html.Div(
            card(
                title=f"{longest_video["video_title"]} ({str(datetime.timedelta(seconds=longest_video["video_duration"]))})",
                description=longest_video["video_description"][:150],
                image_url=longest_video["video_thumbnail_url"],
            ),
            style={"marginTop": "20px"},
        ),
    ],
    style={
        "fontFamily": "Arial, sans-serif",
        "padding": "20px",
        "maxWidth": "1200px",
        "margin": "0 auto",
    },
)
