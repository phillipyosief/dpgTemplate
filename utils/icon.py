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
        self.platform = platform.system().lower()

    def get_icon_path(self, size):
        if self.platform == 'windows':
            return self.icons['WINDOWS'].get(f'{size}x{size}')
        elif self.platform == 'linux':
            return self.icons['LINUX'].get(f'{size}x{size}')
        elif self.platform == 'darwin':  # macOS
            return self.icons['MACOS'].get(f'{size}x{size}')
        return None

    def set_icon(self, size):
        icon_path = self.get_icon_path(size)
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