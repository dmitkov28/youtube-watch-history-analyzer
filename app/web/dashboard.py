import dash
import dash_mantine_components as dmc
from dash import Dash

app = Dash(__name__, use_pages=True, external_stylesheets=dmc.styles.ALL)

layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Title("YouTube Analytics", c="blue"),
                ],
                h="100%",
                px="md",
            )
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=[
                dmc.NavLink(
                    label="Videos",
                    href="/videos",
                ),
                dmc.NavLink(
                    label="Channels",
                    href="/channels",
                ),
            ],
            p="md",
        ),
        dmc.AppShellMain([dash.page_container]),
    ],
    header={"height": 60},
    padding="md",
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    id="appshell",
)


app.layout = dmc.MantineProvider(layout)
