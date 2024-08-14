import dearpygui.dearpygui as dpg
import platform
import logging
import ctypes

import config

from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class FontManager:
    def __init__(self):
        self.default_font_path = self.get_default_font_path()
        self.default_font = None
        self.second_font = None
        self.system_font_scale = self.get_system_font_scale()

    @staticmethod
    def get_default_font_path():
        logger.debug("Getting default font path")
        system = platform.system()
        if system == "Darwin":  # macOS
            return "/System/Library/Fonts/SFNS.ttf"
        elif system == "Windows":
            return "C:\\Windows\\Fonts\\Arial.ttf"
        else:  # Linux
            return "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    @staticmethod
    def get_system_font_scale():
        logger.debug("Getting system font scale")
        system = platform.system()
        if config.FONT_CONFIG['FONT_SCALE'] is None:
            if system == "Darwin":  # macOS
                # macOS does not provide a direct way to get the system font size, using default scale
                return 2
            elif system == "Windows":
                # Get the system DPI setting
                user32 = ctypes.windll.user32
                dpi = user32.GetDpiForSystem()
                return dpi / 96.0  # 96 DPI is the default scale
            else:  # Linux
                # Linux does not provide a direct way to get the system font size, using default scale
                return 2
        else:
            return config.FONT_CONFIG['FONT_SCALE']

    def setup_fonts(self):
        logger.debug(f"Setting up fonts {self.get_default_font_path()}")
        base_font_size = 16
        second_font_size = 10
        scaled_default_font_size = int(base_font_size * self.system_font_scale)
        scaled_second_font_size = int(second_font_size * self.system_font_scale)

        with dpg.font_registry():
            self.default_font = dpg.add_font(self.default_font_path, scaled_default_font_size)
            self.second_font = dpg.add_font(self.default_font_path, scaled_second_font_size)
        logger.debug("Binding default font")
        dpg.bind_font(self.default_font)
        logger.debug(f"Setting global font scale {1 / self.system_font_scale}")
        dpg.set_global_font_scale(1 / 2)
