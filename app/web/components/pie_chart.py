from dash import dcc
import plotly.express as px
import pandas as pd


def pie_chart(df: pd.DataFrame, names: str, values: str, title: str):
    fig = px.pie(df, names=names, values=values, title=title)
    return dcc.Graph(figure=fig)
