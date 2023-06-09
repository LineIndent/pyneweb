import click
import subprocess
from logic.utilities import set_up_yaml_file, set_up_pynecone_file
from pathlib import Path
import os


def initialize_pynecone_file_script():
    target_dir = None
    target_file = None

    base = os.path.basename(os.getcwd())

    for dir in os.listdir():
        if dir == base:
            target_dir = dir

    if target_dir:
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            if os.path.isfile(file_path) and file != "__init__.py":
                target_file = file

    if target_file:
        target_file_path = os.path.join(target_dir, target_file)
        string = set_up_pynecone_file()
        with open(target_file_path, "w") as f:
            f.write(string)

    else:
        pass


@click.command()
def init():
    # First, create the flet_config.yml file
    with open("config.yml", "w") as f:
        string = set_up_yaml_file()
        f.write(string)

    # Create 'logic' directory if it doesn't exist
    Path("logic").mkdir(exist_ok=True)

    # Define the list of files to be generated
    file_list = ["__init__.py", "script.py", "utilities.py", "states.py"]

    # Generate each file in the logic directory
    for file_name in file_list:
        file_path = Path("logic") / file_name
        file_path.touch()

        # Read the contents of the source file
        source_path = Path(__file__).parent / file_name
        with open(source_path, "r") as source_file:
            source_contents = source_file.read()

        # Write the contents to the new file
        with open(file_path, "w") as new_file:
            new_file.write(source_contents)

    click.echo()
    click.echo(f"Generated {len(file_list)} files in the 'logic' directory:")
    for files in file_list:
        click.echo(f"● {files}")

    click.echo("Status: OK")
    click.echo()

    # Run the 'pc init' command
    subprocess.run(["pc", "init"], capture_output=True, text=True)
    initialize_pynecone_file_script()
    click.echo("Command 'pc init' executed successfully.")


@click.group()
def pyneweb():
    pass


pyneweb.add_command(init)

if __name__ == "__main__":
    pyneweb()
