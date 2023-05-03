"""
Utiltities: Provides chunks of code as supplement to the main scrip inside `script.py`.
"""

import os


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
                string = f"""pc.link('{filename}', href='/'),"""
            else:
                string = f"""pc.link('{filename}', href='/{filename}'),"""

            route_list.append(string)

    return route_list
