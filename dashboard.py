from dash import Dash, html, dcc
import plotly.graph_objects as go

from analyze import load_json_as_df

df = load_json_as_df("./watch_history.json")

app = Dash()

top_channels = df["channel_title"].value_counts().head(50).sort_values(ascending=True)
top_videos = df["video_title"].value_counts().head(50).sort_values(ascending=True)

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

app.layout = [
    html.H1(children="Youtube Watch History", style={"textAlign": "center"}),
    html.Div(
        [
            dcc.Graph(figure=channels_fig),
            dcc.Graph(figure=videos_fig),
        ],
        style={"display": "flex"},
    ),
]

if __name__ == "__main__":
    app.run(debug=True)
