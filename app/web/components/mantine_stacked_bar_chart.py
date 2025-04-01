from typing import Dict, List


def mantine_stacked_bar_chart(
    dmc, data: List[Dict], data_key: str, series: List[Dict], h: int = 300
):
    chart = dmc.BarChart(
        h=h,
        dataKey=data_key,
        data=data,
        type="stacked",
        series=series,
    )
    return chart
