from dash import dcc
from wordcloud import WordCloud


def word_cloud(go, input_text: str, title: str):
    wordcloud = WordCloud(
        width=800, height=400, background_color="white", min_font_size=10
    ).generate(input_text)
    word_cloud_array = wordcloud.to_array()

    fig = go.Figure(go.Image(z=word_cloud_array))

    fig.update_layout(
        title=title,
        xaxis={"visible": False},
        yaxis={"visible": False},
        height=500,
    )

    return dcc.Graph(figure=fig)
