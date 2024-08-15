# utils/installer.py
import os
import logging
import requests
import shutil
from utils.download import DownloadManager
from config import UPDATE_CONFIG, APP_CONFIG, app_dirs
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)

def get_latest_version():
    try:
        if UPDATE_CONFIG['METHOD'] == 'GITHUB':
            repo = UPDATE_CONFIG['GITHUB']['REPO']
            url = f"https://raw.githubusercontent.com/{repo}/main/version.txt"
            response = requests.get(url)
            if response.status_code == 200:
                logging.getLogger(__name__).info(f"Latest version: {response.text.strip()}")
                return response.text.strip()
        elif UPDATE_CONFIG['METHOD'] == 'LOCAL-PATH':
            version_file = os.path.join(UPDATE_CONFIG['LOCAL-PATH']['PATH'], 'version.txt')
            if os.path.exists(version_file):
                with open(version_file, 'r') as file:
                    logging.getLogger(__name__).info(f"Latest version: {file.read().strip()}")
                    return file.read().strip()
    except Exception as e:
        logging.getLogger(__name__).error(f"An error occurred: {e}")
    return None

def get_installed_version():
    try:
        version_file = os.path.join(app_dirs.user_data_dir, 'version.txt')
        if os.path.exists(version_file):
            with open(version_file, 'r') as file:
                return file.read().strip()
    except Exception as e:
        logging.getLogger(__name__).error(f"An error occurred: {e}")
    return None



class Installer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.download_manager = DownloadManager(app_dirs.user_data_dir)

    def is_update_needed(self):
        try:
            installed_version = get_installed_version()
            latest_version = get_latest_version()
            # check if installed version is older than the latest version if its same or newer return False
            if installed_version and latest_version and installed_version < latest_version:
                return True
            else:
                return False
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return False

    def download_resources_from_github(self):
        try:
            repo = UPDATE_CONFIG['GITHUB']['REPO']
            url = f"https://github.com/{repo}/archive/refs/heads/main.zip"
            filename = "resources.zip"
            zip_path = os.path.join(app_dirs.user_data_dir, filename)
            self.logger.info(f"Downloading resources from {url} to {zip_path}")
            self.download_manager.download(url, zip_path)
            self.logger.info("Resources downloaded from GitHub")

            # Extract the zip file
            extract_path = os.path.join(app_dirs.user_data_dir, 'extracted')
            self.logger.info(f"Extracting resources from {zip_path} to {app_dirs.user_data_dir}")
            shutil.unpack_archive(zip_path, app_dirs.user_data_dir)
            # rename the extracted folder to 'extracted'
            os.rename(os.path.join(app_dirs.user_data_dir, f"{repo.split('/')[1]}-main"), extract_path)

            self.logger.info("Resources extracted")

            # Move only version.txt and resources folder to the user_data_dir directory
            items_to_move = ['version.txt', 'resources']
            for item in items_to_move:
                src_path = os.path.join(extract_path, item)
                dest_path = os.path.join(app_dirs.user_data_dir, item)
                if os.path.exists(dest_path):
                    self.logger.debug(f"Replacing existing {dest_path}")
                    if os.path.isdir(dest_path):
                        shutil.rmtree(dest_path)
                    else:
                        os.remove(dest_path)
                self.logger.debug(f"Moving {src_path} to {dest_path}")
                shutil.move(src_path, dest_path)

            # Remove the extracted resources folder and the zip file
            self.logger.debug(f"Removing extracted resources folder {extract_path}")
            shutil.rmtree(extract_path)
            self.logger.debug(f"Removing zip file {zip_path}")
            os.remove(zip_path)
            self.logger.info("Resources moved to user_data_dir directory and cleanup done")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

    def copy_resources_from_local_path(self):
        try:
            local_path = UPDATE_CONFIG['LOCAL-PATH']['PATH']
            dest_dir = os.path.join(app_dirs.user_data_dir, 'resources')
            self.logger.info(f"Copying resources from {local_path} to {dest_dir}")
            self.download_manager.copy_directory(local_path, dest_dir)
            self.logger.info("Resources copied from local path")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

    def install_resources(self):
        self.logger.info("Checking if an update is needed")
        self.logger.info(f"Installed version: {get_installed_version()}")
        try:
            if self.is_update_needed():
                method = UPDATE_CONFIG['METHOD']
                self.logger.info(f"Update method: {method}")
                if method == 'GITHUB':
                    self.download_resources_from_github()
                elif method == 'LOCAL-PATH':
                    self.copy_resources_from_local_path()
                else:
                    self.logger.error(f"Unknown update method: {method}")
                latest_version = get_latest_version()
                if latest_version:
                    version_file = os.path.join(app_dirs.user_data_dir, 'version.txt')
                    self.logger.info(f"Writing latest version {latest_version} to {version_file}")
                    with open(version_file, 'w') as file:
                        file.write(latest_version)
                    self.logger.info(f"New version {latest_version} installed")
                else:
                    self.logger.error("Failed to get the latest version")
            else:
                self.logger.info("No update needed")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    installer = Installer()
    installer.install_resources()