import os
from logic.cli import initialize_pynecone_file_script
from logic.utilities import set_up_pynecone_file
import unittest


class TestCLI(unittest.TestCase):
    def test_initialize_pynecone_file_script(self):
        # Create a temporary directory for testing
        test_dir = "test_dir"
        os.mkdir(test_dir)
        os.chdir(test_dir)

        # Create a file for testing
        target_dir = "test_dir"
        target_file = "test_file.py"
        os.mkdir(target_dir)
        file_path = os.path.join(target_dir, target_file)
        with open(file_path, "w") as f:
            f.write("")

        # Test the function
        initialize_pynecone_file_script()

        # Assert the changes made by the function
        with open(file_path, "r") as f:
            contents = f.read()
            self.assertEqual(contents, set_up_pynecone_file())

        # Clean up the test environment
        os.remove(file_path)
        os.rmdir(target_dir)
        os.chdir("..")
        os.rmdir(test_dir)
