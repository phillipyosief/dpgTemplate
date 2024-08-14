# utils/icon.py
import platform
import os
import dearpygui.dearpygui as dpg
import logging

import config

from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)

class Icon:
    def __init__(self):
        self.icons = config.RESOURCES_CONFIG['ICONS']
        self.platform = platform.system()
        logger.debug(f"Icons configuration: {self.icons}")

    def get_icon_path(self, size):
        size_str = str(size)  # Convert size to string
        if self.platform == 'Windows':
            return self.icons['WINDOWS'][size_str + 'x' + size_str]
        elif self.platform == 'Darwin':
            if size == 64:
                return self.icons['MACOS']['128x128']
            return self.icons['MACOS'][size_str + 'x' + size_str]
        else:
            return self.icons['LINUX'][size_str + 'x' + size_str]

    def set_icon(self, size):
        icon_path = self.get_icon_path(size)
        logger.debug(f"Icon path for size {size}: {icon_path}")
        if icon_path and os.path.exists(icon_path):
            if size <= 32:
                dpg.set_viewport_small_icon(icon_path)
            else:
                dpg.set_viewport_large_icon(icon_path)
        else:
            logger.error(f"Icon for {self.platform} not found: {icon_path}")

    def set_all_icons(self):
        for size in [16, 32, 64, 128, 256]:
            self.set_icon(size)