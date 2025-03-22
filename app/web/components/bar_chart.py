from typing import Dict, Literal, Optional

from pandas import Series
from dash import dcc


def bar_chart(
    dcc,
    go_module,
    data_x: Series,
    data_y: Series,
    options: Optional[Dict] = None,
    orientation: Literal["h", "v"] = "h",
) -> dcc.Graph:
    fig = go_module.Figure(go_module.Bar(x=data_x, y=data_y, orientation=orientation))

    if options:
        fig.update_layout(**options)

    return dcc.Graph(figure=fig)
