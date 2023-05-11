"""
Utilities: Provides chunks of code as supplement to the main scrip inside `script.py`.
"""

import os


def navigation(route, title, fn_name):
    string = f"""import pynecone as pc

from logic.states import State

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
                            # start #
                            
                            # end #
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
                        pc.button("Close", on_click=State.left)
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
                            cursor="pointer",
                            color="white",
                            on_click=lambda: State.left,
                        ),
                        width="2rem",
                        padding_left="10px",
                    ),
                    pc.heading(
                        # start #

                        # end #
                        font_size=["lg", "lg", "lg", "xl", "xl"],
                        font_weight="700",
                        color="white",
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
                    "0px 5px",
                    "0px 5px",
                    "0px 5px",
                    "10px 5px",
                    "10px 100px",
                ],
                width="100%",
                transition="height 150ms ease",
                overflow="hidden",
                height= ["0", "0", "0", "3rem", "3rem",],
                spacing="1.25rem",
            ),
            # start #
            
            # end #
            width="100%",
        ),
        width="100%",
        # start #

        # end #
        box_shadow="0px 10px 20px 0px rgba(0, 0, 0, 0.35)",
        height="100vh",
        box_sizing="border-box",
        overflow="hidden",
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
                string = f"""pc.link('{cap}', href='/', font_size="12px", color="white", font_weight="600",
                opacity=["0", "0", "0", "100", "100"],
                transition="opacity 700ms ease",
                ),"""
            else:
                cap = filename.capitalize()
                string = f"""pc.link('{cap}', href='{filename}', font_size="12px", font_weight="600", color="white",
                opacity=["0", "0", "0", "100", "100"],
                transition="opacity 700ms ease",
                ),"""

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

    def left(self):
        self.show_left = not (self.show_left)
"""

    return string


############################################
######### Create config file YAML ##########
############################################


def set_up_yaml_file():
    string = """
site-name: ""
repo-url: ""

theme:
  - bgcolor: "#2e2f3e"
  - primary: ""

nav:
  - Home: "index.py"
  - About: "about.py"
  - Contact: "contact.py"

"""
    return string


############################################
######### Update pynecone init file ########
############################################


def set_up_pynecone_file():
    string = """# Pynecone && Pyneweb modules
import pynecone as pc
from logic.script import script
from logic.states import State

# Import pages from routes dir
from routes import *

# Setup for script
app = pc.App(state=State)
app.compile()
script(app)
"""

    return string
