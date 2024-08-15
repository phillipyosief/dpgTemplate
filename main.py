import logging
import platform
import dearpygui.dearpygui as dpg

import config
from user_data.directories import DirectoryManager
from utils.fonts import FontManager
from utils.icon import Icon
from utils.installer import Installer
from utils.logger import configure_logger
from view.home import Home
from utils.image import ImageHandler

configure_logger()

# Create a logger instance
logger = logging.getLogger(__name__)

# check if macOS
if platform.system() == "Darwin" and config.MENUBAR_CONFIG['NATIVE_MACOS_MENUBAR'] == True:
    logger.info("Using macOS native menubar")
    from view.menubar.macos import MenuBar
else:
    logger.info("Using default menubar")
    from view.menubar.default import MenuBar


class App:
    def __init__(self):
        logger.info("Initializing App")
        self.home = Home()

        font_manager = FontManager()
        font_manager.setup_fonts()

        directory_manager = DirectoryManager()
        directory_manager.create_app_dirs()

        installer = Installer()
        installer.install_resources()

        image_handler = ImageHandler()
        image_handler.load_all_images()




def run_dearpygui():
    dpg.create_context()
    dpg.create_viewport(
        title=config.WINDOW_CONFIG['WINDOW_TITLE'],
        width=config.WINDOW_CONFIG['WINDOW_WIDTH'],
        height=config.WINDOW_CONFIG['WINDOW_HEIGHT'],
        x_pos=config.WINDOW_CONFIG['WINDOW_X_POS'],
        y_pos=config.WINDOW_CONFIG['WINDOW_Y_POS'],
        vsync=config.WINDOW_CONFIG['WINDOW_VSYNC'],
        always_on_top=config.WINDOW_CONFIG['WINDOW_ALWAYS_ON_TOP'],
        decorated=config.WINDOW_CONFIG['WINDOW_DECORATED'],
        clear_color=config.WINDOW_CONFIG['WINDOW_CLEAR_COLOR'],
        resizable=config.WINDOW_CONFIG['WINDOW_RESIZABLE'],
        min_width=config.WINDOW_CONFIG['WINDOW_MIN_WIDTH'],
        max_width=config.WINDOW_CONFIG['WINDOW_MAX_WIDTH'],
        min_height=config.WINDOW_CONFIG['WINDOW_MIN_HEIGHT'],
        max_height=config.WINDOW_CONFIG['WINDOW_MAX_HEIGHT'],
        disable_close=config.WINDOW_CONFIG['WINDOW_DISABLE_CLOSE']
    )

    app = App()

    icon_manager = Icon()
    icon_manager.set_all_icons()

    dpg.setup_dearpygui()
    dpg.show_viewport()

    dpg.set_primary_window(app.home.window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    run_dearpygui()
