# utils/logger.py
import logging
from colorama import Fore, Style, init
import os
import datetime

from user_data.directories import DirectoryManager

# Initialize colorama
init(autoreset=True)

def configure_logger():
    log_dir = DirectoryManager().app_dirs.user_log_dir

    if not isinstance(log_dir, str):
        raise TypeError(f"Expected log_dir to be a string, but got {type(log_dir).__name__}")

    # Ensure the log directory exists
    os.makedirs(log_dir, exist_ok=True)

    class CustomFormatter(logging.Formatter):
        def format(self, record):
            module_name = f"{record.name:^35}"  # Centered and fixed width for module name
            timestamp = self.formatTime(record, '%Y-%m-%d %H:%M:%S')
            log_format = f"{Fore.GREEN}[{module_name}] {Fore.YELLOW}[{timestamp}] {Fore.CYAN}[{record.levelname}]{Style.RESET_ALL} {record.getMessage()}"
            return log_format

    class PlainFormatter(logging.Formatter):
        def format(self, record):
            module_name = f"{record.name:^35}"  # Centered and fixed width for module name
            timestamp = self.formatTime(record, '%Y-%m-%d %H:%M:%S')
            log_format = f"[{module_name}] [{timestamp}] [{record.levelname}] {record.getMessage()}"
            return log_format

    # Configure logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(message)s',
                        handlers=[logging.StreamHandler()])

    # Set custom formatter for console handler
    for handler in logging.getLogger().handlers:
        handler.setFormatter(CustomFormatter())

    # Add a plain file handler
    plain_file_handler = logging.FileHandler(
        os.path.join(log_dir, f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'))
    plain_file_handler.setFormatter(PlainFormatter())
    logging.getLogger().addHandler(plain_file_handler)

# Configure the logger
configure_logger()

# Create a logger instance
logger = logging.getLogger(__name__)
logger.info(f"Logs will be saved in: {DirectoryManager().app_dirs.user_log_dir}")