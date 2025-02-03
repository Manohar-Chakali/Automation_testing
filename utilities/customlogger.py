import logging
import os


class LogGen():

    @staticmethod
    def loggen():
        # Define the log file path
        path = os.getcwd() + "\\logs\\automation.log"  # Removed redundant parentheses

        # Print the path where the log file will be created
        print(f"Log file will be created at: {path}")

        try:
            # Ensure the logs directory exists
            if not os.path.exists(os.path.dirname(path)):
                print(f"Creating directory: {os.path.dirname(path)}")  # Print statement to check
                os.makedirs(os.path.dirname(path))

            # Configure logging
            logging.basicConfig(
                filename=path,  # Correctly setting the filename argument
                format="%(asctime)s: %(levelname)s: %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p"  # Corrected date format
            )

            # Create a logger
            logger = logging.getLogger()

            # Set logging level to DEBUG
            logger.setLevel(logging.DEBUG)

            return logger

        except Exception as e:
            print(f"Error setting up logging: {e}")
