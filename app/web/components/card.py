import dash_mantine_components as dmc


def card(title: str, description: str, image_url: str) -> dmc.Card:
    card_component = dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Image(
                    src=image_url,
                    h=160,
                    alt="Norway",
                )
            ),
            dmc.Group(
                [
                    dmc.Text(title, fw=500),
                ],
                justify="space-between",
                mt="md",
                mb="xs",
            ),
            dmc.Text(
                description,
                size="sm",
                c="dimmed",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        w=350,
    )
    return card_component
