import logging
import os

LOG_DIR = "logs"
LOG_FILE = "app.log"

# Create logs directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_logger():
    logger = logging.getLogger("CareerAdvisorBot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE))
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger