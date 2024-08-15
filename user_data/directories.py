# user_data/directories.py
import os
import shutil
from appdirs import AppDirs
import logging

import config

# Create a logger instance
logger = logging.getLogger(__name__)


class DirectoryManager:
    def __init__(self):
        self.app_dirs = config.app_dirs

    def validate_directory_path(self, directory):
        # Ensure the directory path is absolute and within the allowed base directory
        base_dir = os.path.abspath(self.app_dirs.user_data_dir)
        abs_directory = os.path.abspath(directory)
        if not abs_directory.startswith(base_dir):
            raise ValueError(f"Invalid directory path: {directory}")

    def create_app_dirs(self):
        # List of directories to create
        directories = [
            self.app_dirs.user_data_dir,
            self.app_dirs.user_config_dir,
            self.app_dirs.user_cache_dir,
            self.app_dirs.user_log_dir,
            self.app_dirs.user_state_dir
        ]

        # Create directories if they do not exist
        for directory in directories:
            logger.debug(f"Checking if directory exists: {directory}")
            if not os.path.exists(directory):
                logger.info(f"Created Directory: {directory}")
            else:
                logger.info(f"Directory already exists: {directory}")

    def delete_app_dirs(self):
        # List of directories to delete
        directories = [
            self.app_dirs.user_data_dir,
            self.app_dirs.user_config_dir,
            self.app_dirs.user_cache_dir,
            self.app_dirs.user_log_dir,
            self.app_dirs.site_data_dir,
            self.app_dirs.site_config_dir,
            self.app_dirs.user_state_dir
        ]

        # Delete directories if they exist
        for directory in directories:
            self.validate_directory_path(directory)
            if os.path.exists(directory):
                shutil.rmtree(directory)
                print(f"Deleted directory: {directory}")
            else:
                print(f"Directory does not exist: {directory}")

    def is_directory_empty(self, directory):
        self.validate_directory_path(directory)
        return len(os.listdir(directory)) == 0


# Initialize app_dirs globally
directory_manager = DirectoryManager()
app_dirs = directory_manager.app_dirs
