from typing import Dict, List


def mantine_stacked_bar_chart(
    dmc,
    data: List[Dict],
    data_key: str,
    series: List[Dict],
    h: int = 300,
    type: str = "stacked",
    with_legend: bool = True,
):
    chart = dmc.BarChart(
        h=h,
        dataKey=data_key,
        data=data,
        type=type,
        series=series,
        withLegend=with_legend,
    )
    return chart
