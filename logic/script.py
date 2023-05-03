import yaml
import os
from logic.utilities import set_route_default_page, navigation_list
import pynecone as pc

def get_yaml_object() -> dict:
    with open("config.yml", "r") as file:
        docs = yaml.safe_load(file)
    return docs


def check_pages_directory_script():
    # Check if "pages" directory exists
    pages_dir = None
    for root, dirs, files in os.walk("."):
        if "routes" in dirs:
            pages_dir = os.path.join(root, "routes")
            break

    if not pages_dir:
        # Create "pages" directory in the root folder
        pages_dir = os.path.join(os.getcwd(), "routes")
        os.mkdir(pages_dir)


def update_pages_directory_script(docs: dict):
    # Loop over files in the pages directory and delete any files that are not listed in the nav
    for file in os.listdir("routes"):
        if file.endswith(".py"):
            found = False
            for page in docs["nav"]:
                if page.get(next(iter(page))) == file:
                    found = True
                    break
            if not found:
                os.remove(os.path.join("routes", file))


def set_default_methods_script(docs: dict):
    # Loop over the nav list and create/update files
    # 1. Temp. list to store the filepaths in + the modules dict
    file_list: list = []

    # 2. Loop through navigation tree and append the file_list with the filepaths
    for page in docs["nav"]:
        for key in page:
            filename = f"{page[key]}"
            filepath = os.path.join("routes", filename)
            fileName = os.path.splitext(page[key])[0]
            file_list.append((filepath, fileName))


    # 3. Loop through the file_list and create the corresponding pages
    for filepath, filename in file_list:
        if filename == "index":
            method = set_route_default_page("", filename, filename)
        else:
            method = set_route_default_page(filename, filename, filename)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(f"{method}")


    # 4. Update/create the route.pickles file for modules setup
    for file in os.listdir("routes"):
        # Set the path of the file to loop over folders and only include files
        path = os.path.join("routes", file)

        # If the path is NOT a folder, continue ...
        if not os.path.isdir(path):
            # Open the file and read it's content before seeking index points
            with open(f"./routes/{file}", "r") as f:
                code = f.read()
                
            # Find the start and end index of the `<start>` and `<end>` marks
            start_idx = code.index("# start #")
            end_idx = code.index("# end #")

            # Write your code to add between the `<start>` and `<end>` marks here
            nav_string = "\n".join(navigation_list())
            
            code_to_add = f"""pc.text('Hello! This is the', 
            pc.span(' {file} ', as_='mark'), 
            'page!!'),
            pc.hstack(
                {nav_string}
                width="100%",
                display='flex',
                align_items='center',
                justify_content='center',                
            ),
            """

            # Modify the function string by inserting the new code between the start and end index
            modified_string = (
                code[:start_idx] + "# start #\n" + code_to_add + code[end_idx:]
            )

            with open(f"./routes/{file}", "w") as f:
                f.write(modified_string)

        else:
            pass
    
    
def update_init_file():
    # Update the __init__.py file to import the corresponding  routes in the main aplication page
    with open("./routes/__init__.py", "w") as f:
        for file in os.listdir("routes"):
            path = os.path.join("routes", file)
            if not os.path.isdir(path) and path != "routes/__init__.py":
                file = os.path.splitext(file)[0]
                string = f"from routes.{file} import {file}\n"
                f.write(string)
                

# Main automation script...
def script(app: pc.Component):
    # 1. Store the YAML data as a python dict object
    try:
        docs: dict = get_yaml_object()
        
    except FileNotFoundError as err:
        print(err)

    # 2. Check for a `routes` dir and create one if it doesn't exist'
    try:
        check_pages_directory_script()
    
    except Exception as err:
        print(err)
        
    # 3. Clean up `routes` dir
    try:
        update_pages_directory_script(docs)
    
    except Exception as err:
        print(err)
        
    # 4. Create the pages as defined by the `nav` header in the config.yml file
    try:
        set_default_methods_script(docs)
    
    except Exception as err:
        print(err)
        
    # 5. Update the `__init__.py` file 
    try:
        update_init_file()
    
    except Exception as err:
        print(err)  
        
    
    app.compile()