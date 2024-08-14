# user_data/download.py
import os
import requests
import zipfile
import logging
import shutil


class DownloadManager:
    def __init__(self, download_dir):
        self.download_dir = download_dir
        os.makedirs(self.download_dir, exist_ok=True)
        self.logger = logging.getLogger(__name__)

    def download_file(self, url, filename):
        self.logger.info(f"Downloading file from {url}")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(self.download_dir, filename)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            self.logger.info(f"File downloaded: {file_path}")
            return file_path
        else:
            self.logger.error(f"Failed to download file: {response.status_code}")
            return None

    def extract_zip(self, file_path):
        self.logger.info(f"Extracting ZIP file: {file_path}")
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(self.download_dir)
        self.logger.info(f"Extracted to: {self.download_dir}")

    def download_and_extract(self, url, filename):
        file_path = self.download_file(url, filename)
        if file_path and file_path.endswith('.zip'):
            self.extract_zip(file_path)

    def copy_directory(self, src_dir, dest_dir):
        self.logger.info(f"Copying directory from {src_dir} to {dest_dir}")
        try:
            shutil.copytree(src_dir, dest_dir)
            self.logger.info(f"Directory copied to: {dest_dir}")
        except Exception as e:
            self.logger.error(f"Failed to copy directory: {e}")
