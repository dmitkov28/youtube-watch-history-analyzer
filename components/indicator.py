from dash import dcc


def indicator(dcc, go_module, value: int | float, title: str) -> dcc.Graph:
    graph = dcc.Graph(
        id="gauge-chart",
        figure=go_module.Figure(
            go_module.Indicator(
                mode="number",
                value=value,
                title={"text": title},
            )
        ),
    )
    return graph
