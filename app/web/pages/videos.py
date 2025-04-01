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
            className="mb-8 p-4 bg-gray-100 rounded-lg shadow-md",
        ),
        html.Div(
            pie_chart(
                subbed_vs_unsubbed,
                "is_subscribed",
                "count",
                "Watched Videos (Subscribed vs Unsubscribed Channels)",
            ),
            className="mb-8 p-4 bg-gray-100 rounded-lg shadow-md",
        ),
        html.Div(
            word_cloud(
                go,
                word_cloud_data,
                "Video Titles Wordcloud",
            ),
            className="mb-8 p-4 bg-gray-100 rounded-lg shadow-md",
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
    className="font-sans p-5 max-w-7xl mx-auto",
)
