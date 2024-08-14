# utils/installer.py
import os
import logging
import requests
import shutil
from utils.download import DownloadManager
from utils.error_handler import ErrorHandler
from config import UPDATE_CONFIG, app_dirs

def get_latest_version():
    try:
        if UPDATE_CONFIG['METHOD'] == 'GITHUB':
            repo = UPDATE_CONFIG['GITHUB']['REPO']
            url = f"https://raw.githubusercontent.com/{repo}/main/version.txt"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
        elif UPDATE_CONFIG['METHOD'] == 'LOCAL-PATH':
            version_file = os.path.join(UPDATE_CONFIG['LOCAL-PATH']['PATH'], 'version.txt')
            if os.path.exists(version_file):
                with open(version_file, 'r') as file:
                    return file.read().strip()
    except Exception as e:
        ErrorHandler().handle_error(e)
    return None

def get_installed_version():
    try:
        version_file = os.path.join(app_dirs.user_data_dir, 'version.txt')
        if os.path.exists(version_file):
            with open(version_file, 'r') as file:
                return file.read().strip()
    except Exception as e:
        ErrorHandler().handle_error(e)
    return None

class Installer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.download_manager = DownloadManager(app_dirs.user_data_dir)
        self.error_handler = ErrorHandler()

    def is_update_needed(self):
        try:
            installed_version = get_installed_version()
            latest_version = get_latest_version()
            if installed_version and latest_version:
                return installed_version != latest_version
            return True
        except Exception as e:
            self.error_handler.handle_error(e)
            return False

    def download_resources_from_github(self):
        try:
            repo = UPDATE_CONFIG['GITHUB']['REPO']
            url = f"https://github.com/{repo}/archive/refs/heads/main.zip"
            filename = "resources.zip"
            zip_path = os.path.join(app_dirs.user_data_dir, filename)
            self.download_manager.download(url, zip_path)
            self.logger.info("Resources downloaded from GitHub")

            # Extract the zip file
            extract_path = os.path.join(app_dirs.user_data_dir, 'resources')
            shutil.unpack_archive(zip_path, extract_path)
            self.logger.info("Resources extracted")

            # Move files to root folder and remove the extra folder
            for item in os.listdir(extract_path):
                item_path = os.path.join(extract_path, item)
                if os.path.isdir(item_path):
                    for sub_item in os.listdir(item_path):
                        shutil.move(os.path.join(item_path, sub_item), extract_path)
                    os.rmdir(item_path)

            # Remove the zip file
            os.remove(zip_path)
            self.logger.info("Zip file removed")
        except Exception as e:
            self.error_handler.handle_error(e)

    def copy_resources_from_local_path(self):
        try:
            local_path = UPDATE_CONFIG['LOCAL-PATH']['PATH']
            dest_dir = os.path.join(app_dirs.user_data_dir, 'resources')
            self.download_manager.copy_directory(local_path, dest_dir)
            self.logger.info("Resources copied from local path")
        except Exception as e:
            self.error_handler.handle_error(e)

    def install_resources(self):
        try:
            if self.is_update_needed():
                method = UPDATE_CONFIG['METHOD']
                if method == 'GITHUB':
                    self.download_resources_from_github()
                elif method == 'LOCAL-PATH':
                    self.copy_resources_from_local_path()
                else:
                    self.logger.error(f"Unknown update method: {method}")
                latest_version = get_latest_version()
                if latest_version:
                    version_file = os.path.join(app_dirs.user_data_dir, 'version.txt')
                    with open(version_file, 'w') as file:
                        file.write(latest_version)
                else:
                    self.logger.error("Failed to get the latest version")
            else:
                self.logger.info("No update needed")
        except Exception as e:
            self.error_handler.handle_error(e)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    installer = Installer()
    installer.install_resources()