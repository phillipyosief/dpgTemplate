import dearpygui.dearpygui as dpg
import logging
from config import RESOURCES_CONFIG
from utils.logger import configure_logger

configure_logger()

class ImageHandler:
    def __init__(self):
        self.textures = {}
        self.logger = logging.getLogger(__name__)

    def load_all_images(self):
        for tag, file_path in RESOURCES_CONFIG['IMAGES'].items():
            try:
                result = dpg.load_image(file_path)
                if result is None:
                    raise ValueError(f"Failed to load image from file path: {file_path}")
                width, height, channels, data = result
                with dpg.texture_registry():
                    self.textures[tag] = dpg.add_static_texture(width, height, data, tag=tag)
                self.logger.info(f"Loaded image '{tag}' from '{file_path}'")
            except Exception as e:
                self.logger.error(f"Failed to load image '{tag}' from '{file_path}': {e}")

    def display_image(self, tag, width, height, **kwargs):
        if tag in self.textures:
            dpg.add_image(self.textures[tag], width=width, height=height, **kwargs)
            self.logger.info(f"Displayed image '{tag}' with size ({width}x{height}) and additional arguments: {kwargs}")
        else:
            self.logger.error(f"Image with tag '{tag}' not found. Please load the image first.")

    def remove_image(self, tag):
        if tag in self.textures:
            dpg.delete_item(self.textures[tag])
            del self.textures[tag]
            self.logger.info(f"Removed image '{tag}'")
        else:
            self.logger.error(f"Image with tag '{tag}' not found.")