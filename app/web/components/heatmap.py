import pandas as pd
from dash import dcc


def heatmap(px, df: pd.DataFrame, title: str, legend_label: str):
    fig = px.density_heatmap(
        df,
        x="hour",
        y="day_of_week",
        z="count",
        color_continuous_scale="Blues",
        title=title,
        labels={
            "hour": "Hour of Day",
            "day_of_week": "Day of Week",
            "count": "Videos Watched",
        },
    )
    fig.update_layout(coloraxis_colorbar_title=legend_label)
    return dcc.Graph(figure=fig)
