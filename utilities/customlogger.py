import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        # Define the logs folder and the log file path
        logs_dir = os.path.join(os.path.abspath(os.curdir), "logs")
        logs_path = os.path.join(logs_dir, "test_log.log")

        # Print the log file path to the console for debugging
        print(f"Log file will be created at: {logs_path}")

        try:
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)

            # Configure logging
            logging.basicConfig(
                filename=logs_path,  # Correctly setting the filename argument
                format="%(asctime)s: %(levelname)s: %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p",  # Corrected date format
                level=logging.DEBUG  # Ensure logging is set to DEBUG level
            )

            # Create a logger
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)

            return logger

        except Exception as e:
            print(f"Error setting up logging: {e}")
