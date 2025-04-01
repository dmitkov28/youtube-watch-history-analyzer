import datetime

import dash
import dash_mantine_components as dmc
import plotly.express as px
import plotly.graph_objects as go
from dash import html


from app.data import (
    longest_video,
    most_watched_videos,
    subbed_vs_unsubbed,
    video_with_most_comments,
    video_with_most_views,
    videos_timeline,
    word_cloud_data,
)
from app.web.components import card, line_chart, pie_chart, word_cloud

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
                html.H1(
                    "Most Watched Videos",
                    className="text-center text-xl font-bold my-12",
                ),
                html.Div(
                    [
                        dmc.Anchor(
                            card(
                                title=f"{row['video_title']} ({row['times_watched']} times)",
                                description="",
                                image_url=row["video_thumbnail_url"],
                            ),
                            href=row["video_url"],
                            target="_blank",
                        )
                        for _, row in most_watched_videos.iterrows()
                    ],
                    className="grid grid-cols-3 gap-2",
                ),
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H1(
                            "Longest Video",
                            className="text-center text-xl font-bold my-12",
                        ),
                        dmc.Anchor(
                            card(
                                title=f"{longest_video['video_title']} ({str(datetime.timedelta(seconds=longest_video['video_duration']))})",
                                description=longest_video["video_description"][:150],
                                image_url=longest_video["video_thumbnail_url"],
                            ),
                            href=longest_video["video_url"],
                            target="_blank",
                        ),
                    ],
                    className="flex flex-col items-center justify-center gap-3",
                ),
                html.Div(
                    [
                        html.H1(
                            "Video With Most Views",
                            className="text-center text-xl font-bold my-12",
                        ),
                        dmc.Anchor(
                            card(
                                title=f"{video_with_most_views['video_title']} ({video_with_most_views['video_views']:,} views)",
                                description=video_with_most_views["video_description"][
                                    :150
                                ],
                                image_url=video_with_most_views["video_thumbnail_url"],
                            ),
                            href=video_with_most_views["video_url"],
                            target="_blank",
                        ),
                    ],
                    className="flex flex-col items-center justify-center gap-3",
                ),
                html.Div(
                    [
                        html.H1(
                            "Video With Most Comments",
                            className="text-center text-xl font-bold my-12",
                        ),
                        dmc.Anchor(
                            card(
                                title=f"{video_with_most_comments['video_title']} ({video_with_most_comments['video_comments']:,} comments)",
                                description=video_with_most_comments[
                                    "video_description"
                                ][:150],
                                image_url=video_with_most_comments[
                                    "video_thumbnail_url"
                                ],
                            ),
                            href=video_with_most_comments["video_url"],
                            target="_blank",
                        ),
                    ],
                    className="flex flex-col items-center justify-center gap-3",
                ),
            ],
            className="grid grid-cols-3 gap-3",
        ),
    ],
    style={
        "fontFamily": "Arial, sans-serif",
        "padding": "20px",
        "maxWidth": "1200px",
        "margin": "0 auto",
    },
)
