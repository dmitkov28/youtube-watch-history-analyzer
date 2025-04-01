import dash
from dash import html
import dash_mantine_components as dmc

from app.web.components import card
from app.data import channels_with_most_videos_watched

dash.register_page(__name__, path="/channels", name="Channels")

layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Most Watched Channels",
                    className="text-center text-xl font-bold my-12",
                ),
                html.Div(
                    [
                        dmc.Anchor(
                            card(
                                title=f"{row['channel_title']} ({row['watched_videos']} videos watched)",
                                description="",
                                image_url=row["channel_thumbnail_url"],
                            ),
                            href=f"https://youtube.com/{row['channel_custom_url']}",
                            target="_blank",
                        )
                        for _, row in channels_with_most_videos_watched.iterrows()
                    ],
                    className="grid grid-cols-3 gap-2",
                ),
            ]
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
