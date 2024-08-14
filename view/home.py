import dearpygui.dearpygui as dpg
import logging

from utils.logger import configure_logger

configure_logger()

logger = logging.getLogger(__name__)


class Home:
    def __init__(self):
        logger.info("Initializing Home")
        logger.debug("Creating Home window")
        with dpg.window(label="Home") as self.window:
            logger.debug("Adding text to Home window")
            dpg.add_text("Welcome to the Home window!")

