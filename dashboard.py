import plotly.graph_objects as go
from dash import Dash, dcc, html

from analyze import load_json_as_df

df = load_json_as_df("./watch_history.json")
app = Dash()


watched_videos_count = df.groupby(df["timestamp"].dt.to_period("W")).agg(
    {"video_id": "count"}
)
watched_videos_count = watched_videos_count.reset_index()
watched_videos_count["timestamp"] = watched_videos_count["timestamp"].dt.to_timestamp()

watched_videos_count_chart = go.Figure(
    go.Bar(
        x=watched_videos_count["timestamp"],
        y=watched_videos_count["video_id"],
    )
)

watched_videos_count_chart.update_layout(
    title="Weekly Watched Videos Count",
    title_x=0.5,
    xaxis_title="Week",
    yaxis_title="Number of Videos Watched",
)

top_channels = df["channel_title"].value_counts().head(50).sort_values(ascending=True)
channels_fig = go.Figure(
    go.Bar(
        y=top_channels.index,
        x=top_channels.values,
        orientation="h",
        width=0.7,
    )
)
channels_fig.update_layout(
    title="Most Watched YouTube Channels",
    title_x=0.5,
    height=1200,
    yaxis=dict(
        automargin=True,
        tickmode="linear",
        showticklabels=True,
    ),
    margin=dict(
        l=300,
    ),
)

top_videos = df["video_title"].value_counts().head(50).sort_values(ascending=True)
videos_fig = go.Figure(
    go.Bar(
        y=top_videos.index,
        x=top_videos.values,
        orientation="h",
        width=0.7,
    )
)
videos_fig.update_layout(
    title="Most Watched Videos",
    title_x=0.5,
    height=1200,
    yaxis=dict(
        automargin=True,
        tickmode="linear",
        showticklabels=True,
    ),
    margin=dict(
        l=300,
    ),
)

app.layout = html.Div(
    [
        html.H1(children="YouTube Watch History", style={"textAlign": "center"}),
        html.Div(
            [
                dcc.Graph(figure=watched_videos_count_chart),
            ]
        ),
        html.Div(
            [
                dcc.Graph(figure=channels_fig),
                dcc.Graph(figure=videos_fig),
            ],
            style={"display": "flex"},
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
