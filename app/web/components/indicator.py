from dash import dcc


def indicator(dcc, go_module, value: int | float, title: str) -> dcc.Graph:
    graph = dcc.Graph(
        figure=go_module.Figure(
            go_module.Indicator(
                mode="number",
                value=value,
                title={"text": title},
            )
        ),
        style={"height": "300px"},
    )
    return graph
