import subprocess
import time
import unittest
from unittest.mock import MagicMock, mock_open, patch

from mockup.functions import (
    execute_command,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestReadDataFromFile(unittest.TestCase):
    """
    Test the read_data_from_file function
    """

    @patch("builtins.open", new_callable=mock_open, read_data="test data")
    def test_read_data_from_file_success(self, mock_file):
        """
        Test reading data from a file successfully.
        """
        # Call the function under test
        result = read_data_from_file("dummy_filename.txt")

        # Assert that the function returns the expected result
        self.assertEqual(result, "test data")

        # Assert that open was called with the correct parameters
        mock_file.assert_called_once_with("dummy_filename.txt", "r")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_data_from_file_failure(self, mock_file):
        """
        Test the function raising a FileNotFoundError.
        """
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("non_existent_file.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Test the execute_command function
    """

    @patch("subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Test executing a command successfully.
        """
        # Set up the mock to return a process result with a stdout attribute
        mock_run.return_value = MagicMock(stdout="command output")

        # Call the function under test with a dummy command
        result = execute_command(["echo", "hello"])

        # Assert that the function returns the expected result
        self.assertEqual(result, "command output")

        # Assert that subprocess.run was called with the correct parameters
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, text=True
        )

    @patch("subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """
        Test the function raising a CalledProcessError.
        """
        # Set up the mock to raise a CalledProcessError when the subprocess runs
        mock_run.side_effect = subprocess.CalledProcessError(
            1, ["exit", "1"], output="error"
        )

        # Use assertRaises to check that a CalledProcessError is raised
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["exit", "1"])


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Test the perform_action_based_on_time function
    """

    @patch("time.time", return_value=5)
    def test_perform_action_before_cutoff(self, mock_time):
        """
        Test that 'Action A' is returned when current time is less than 10.
        """
        # Call the function under test
        action = perform_action_based_on_time()

        # Assert that the function returns 'Action A'
        self.assertEqual(action, "Action A")

        # Assert that time.time was called
        mock_time.assert_called_once()

    @patch("time.time", return_value=15)
    def test_perform_action_after_cutoff(self, mock_time):
        """
        Test that 'Action B' is returned when current time is 10 or greater.
        """
        # Call the function under test
        action = perform_action_based_on_time()

        # Assert that the function returns 'Action B'
        self.assertEqual(action, "Action B")

        # Assert that time.time was called
        mock_time.assert_called_once()


if __name__ == "__main__":
    unittest.main()
