# utils/uninstall.py
import os
import shutil
import logging

from config import UPDATE_CONFIG, APP_CONFIG, app_dirs


class DeleteManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.logger = logging.getLogger(__name__)

    def delete_file(self, file_path):
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                self.logger.info(f"Deleted file: {file_path}")
            else:
                self.logger.warning(f"File not found: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to delete file {file_path}: {e}")

    def delete_directory(self, dir_path):
        try:
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)
                self.logger.info(f"Deleted directory: {dir_path}")
            else:
                self.logger.warning(f"Directory not found: {dir_path}")
        except Exception as e:
            self.logger.error(f"Failed to delete directory {dir_path}: {e}")

    def delete_all(self):
        try:
            if os.path.exists(self.base_dir):
                shutil.rmtree(self.base_dir)
                self.logger.info(f"Deleted all contents in: {self.base_dir}")
            else:
                self.logger.warning(f"Base directory not found: {self.base_dir}")
        except Exception as e:
            self.logger.error(f"Failed to delete all contents in {self.base_dir}: {e}")


if __name__ == '__main__':
    delete_manager = DeleteManager(app_dirs.user_data_dir)
    delete_manager.delete_all()
