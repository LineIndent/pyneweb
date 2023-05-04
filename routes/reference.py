import pynecone as pc
    
@pc.route(route='/reference', title='reference')
def reference():
    return pc.vstack(
        pc.drawer(
            pc.drawer_overlay(
                pc.drawer_content(
                    pc.drawer_header(
                        pc.container(
                            pc.heading(
                                # start #


















# start #
'Project Name',
# end #
                                size="md", 
                                color="white",
                            ),
                            bg="#2e2f3e",
                            width="100%",
                            padding="20px 5%",
                        ),
                        padding="0",
                    ),
                    pc.drawer_body(
                        pc.vstack(
                            









# start #
pc.link('Index', href='/', font_size="12px", font_weight="600", color='white', width='100%', padding='5%',),
pc.link('Docs', href='/docs', font_size="12px", font_weight="600", color='white', width='100%', padding='5%',),
pc.link('Reference', href='/reference', font_size="12px", font_weight="600", color='white', width='100%', padding='5%',),
pc.link('Contact', href='/contact', font_size="12px", font_weight="600", color='white', width='100%', padding='5%',),
# end #
                            spacing="0",
                        ),
                        padding="0",
                    ),
                    pc.drawer_footer(
                        pc.button("Close", on_click=State.right)
                    ),
                    bg="#2e2f3e",
                ),
            ),
            is_open=State.show_left,
            placement="left",
        ),
        pc.vstack(
            pc.hstack(
                pc.hstack(
                    pc.mobile_and_tablet(
                        pc.icon(
                            tag="hamburger",
                            font_size="xl",
                            on_click=lambda: State.show_left,
                        ),
                        width="2rem",
                        padding_left="10px",
                    ),
                    pc.heading(
                        









# start #
'Project Name',
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
pc.link('Index', href='/', font_size="12px", font_weight="600",),
pc.link('Docs', href='/docs', font_size="12px", font_weight="600",),
pc.link('Reference', href='/reference', font_size="12px", font_weight="600",),
pc.link('Contact', href='/contact', font_size="12px", font_weight="600",),
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
bg='teal',
# end #
            box_shadow="0px 10px 20px 0px rgba(0, 0, 0, 0.35)",
            height="100vh",
            box_sizing="border-box",
            overflow="hidden",
        )
    )
