import pandas as pd
from dash import dcc


def line_chart(px, df: pd.DataFrame, x_col_name: str, y_col_name, title: str):
    return dcc.Graph(figure=px.line(df, x=x_col_name, y=y_col_name, title=title))
