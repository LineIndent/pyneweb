"""
Utiltities: Provides chunks of code as supplement to the main scrip inside `script.py`.
"""

import os


def navigation(route, title, fn_name):
    string = f"""import pynecone as pc
    
@pc.route(route='/{route}', title='{title}')
def {fn_name}():
    return pc.vstack(
        pc.drawer(
            pc.drawer_overlay(
                pc.drawer_content(
                    pc.drawer_header(
                        pc.container(
                            pc.heading(
                                # start #

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

            # end #
            box_shadow="0px 10px 20px 0px rgba(0, 0, 0, 0.35)",
            height="100vh",
            box_sizing="border-box",
            overflow="hidden",
        )
    )
"""
    return string


def navigation_list():
    route_list: list = []
    for file in os.listdir("routes"):
        # Set the path of the file to loop over folders and only include files
        path = os.path.join("routes", file)

        # If the path is NOT a folder, continue ...
        if not os.path.isdir(path):
            filename = os.path.splitext(file)[0]
            if filename == "index":
                cap = filename.capitalize()
                string = f"""pc.link('{cap}', href='/', font_size="12px", font_weight="600",),"""
            else:
                cap = filename.capitalize()
                string = f"""pc.link('{cap}', href='/{filename}', font_size="12px", font_weight="600",),"""

            route_list.append(string)

    return route_list


def side_navigation_list():
    route_list: list = []
    for file in os.listdir("routes"):
        # Set the path of the file to loop over folders and only include files
        path = os.path.join("routes", file)

        # If the path is NOT a folder, continue ...
        if not os.path.isdir(path):
            filename = os.path.splitext(file)[0]
            if filename == "index":
                cap = filename.capitalize()
                string = f"""pc.link('{cap}', href='/', font_size="12px", font_weight="600", color='white', width='100%', padding='5%',),"""
            else:
                cap = filename.capitalize()
                string = f"""pc.link('{cap}', href='/{filename}', font_size="12px", font_weight="600", color='white', width='100%', padding='5%',),"""

            route_list.append(string)

    return route_list


def app_states():
    string = """import pynecone as pc

class State(pc.State):
    # Main state where all other states inherit from.#
    show_left: bool = False

    def right(self):
        self.show_left = not (self.show_left)
"""

    return string
