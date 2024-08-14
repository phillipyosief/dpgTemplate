# utils/error_handler.py
import logging

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def handle_error(self, error):
        self.logger.error(f"An error occurred: {error}")