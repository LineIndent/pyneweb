"""
Utiltities: Provides chunks of code as supplement to the main scrip inside `script.py`.
"""

import os


def navigation(route, title, fn_name):
    string = f"""import pynecone as pc
    
@pc.route(route='/{route}', title='{title}')
def {fn_name}():
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
        ),
        width="100%",
        height="100vh",
        box_sizing="border-box",
        # start #
            
        # end #
        overflow="hidden",
    )
"""
    return string


def set_route_default_page(route, title, fn_name):
    string = f"""import pynecone as pc
    
    
@pc.route(route='/{route}', title='{title}')
def {fn_name}():
    return pc.vstack(
        pc.hstack(
            
            width="100%",
            padding="5%",
            bg="blue",    
        ),
        # start #
        
        # end #
        width="100%",
        height="100vh",
        box_sizing= "border-box",
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
                string = f"""pc.link('{filename}', href='/', font_size="12px", font_weight="500",),"""
            else:
                string = f"""pc.link('{filename}', href='/{filename}', font_size="12px", font_weight="500",),"""

            route_list.append(string)

    return route_list
