import logging
import os
from datetime import datetime

# Generate the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory path
log_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it does not exist
try:
    os.makedirs(log_path, exist_ok=True)
    print(f"Directory created successfully: {log_path}")
except Exception as e:
    print(f"Error creating directory: {log_path} - {e}")

# Generate the full log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

# Log a test message
