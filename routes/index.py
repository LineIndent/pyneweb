import pynecone as pc


@pc.route(route="/", title="index")
def index():
    return pc.vstack(
        pc.vstack(
            pc.hstack(
                pc.hstack(
                    pc.mobile_and_tablet(
                        pc.icon(
                            tag="hamburger",
                            font_size="xl",
                        ),
                        width="2rem",
                        padding_left="10px",
                    ),
                    pc.heading(
                        # start #












                        











# start #
'Pynescript',
# end #
                        font_size=["lg", "lg", "lg", "xl", "xl"],
                        font_weight="700",
                    ),
                    spacing="2rem",
                ),
                display="flex",
                width="100%",
                transition="padding 100ms ease",
                padding=[
                    "10px 5px",
                    "10px 5px",
                    "10px 5px",
                    "10px 5px",
                    "10px 100px",
                ],
            ),
            pc.hstack(
                pc.hstack(
                    pc.mobile_and_tablet(
                        width="1rem",
                    ),
                    











# start #
pc.link('index', href='/', font_size="12px", font_weight="500",),
pc.link('docs', href='/docs', font_size="12px", font_weight="500",),
pc.link('reference', href='/reference', font_size="12px", font_weight="500",),
pc.link('contact', href='/contact', font_size="12px", font_weight="500",),
# end #
                    spacing="2rem",
                ),
                padding=[
                    "10px 5px",
                    "10px 5px",
                    "10px 5px",
                    "10px 5px",
                    "10px 100px",
                ],
                width="100%",
                transition="all 100ms ease",
                overflow="hidden",
                display=["None", "None", "None", "flex", "flex"],
                spacing="1.25rem",
            ),
            width="100%",
            











# start #
bg='orange',
# end #
            box_shadow="0px 10px 20px 0px rgba(0, 0, 0, 0.35)",
        ),
        width="100%",
        height="100vh",
        box_sizing="border-box",
        











# start #
bg='#2e2f3e',
# end #
        overflow="hidden",
    )
