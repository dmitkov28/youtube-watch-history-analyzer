import dash
from dash import html
import dash_mantine_components as dmc

from app.web.components import card, mantine_stacked_bar_chart
from app.data import channels_with_most_videos_watched, channel_videos_watched

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
        html.Div(
            [
                html.H2("Channels with most videos watched"),
                mantine_stacked_bar_chart(
                    dmc,
                    data=channel_videos_watched,
                    data_key="channel_title",
                    type="percent",
                    series=[
                        {"name": "channel_total_videos", "color": "teal.6"},
                        {"name": "videos_watched", "color": "blue.6"},
                    ],
                )
            ],
            className="my-8"
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
