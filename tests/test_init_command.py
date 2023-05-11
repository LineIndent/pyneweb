import click
from click.testing import CliRunner
import os
from logic.utilities import set_up_yaml_file, set_up_pynecone_file
from pathlib import Path


def test_init_command():
    runner = CliRunner()
    result = runner.invoke(init)
    assert result.exit_code == 0
    assert "Generated 4 files in the 'logic' directory:" in result.output
    assert "__init__.py" in result.output
    assert "script.py" in result.output
    assert "utilities.py" in result.output
    assert "states.py" in result.output
    assert "Status: OK" in result.output
