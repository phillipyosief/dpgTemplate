# view/menubar.py
import tkinter as tk
from tkinter import messagebox
import dearpygui.dearpygui as dpg
import platform
import config
import logging

from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)

class MenuBar:
    def __init__(self):
        logger.info("Initializing MenuBar")
        self.system = platform.system()

        if self.system == "Darwin":
            self.window = tk.Tk()
            self.window.title(config.APP_CONFIG['APP_NAME'])
            self.window.iconbitmap(config.RESOURCES_CONFIG['ICONS']['MACOS']['128x128'])
            self.menubar = tk.Menu(self.window)
            self.window.option_add('*tearOff', False)
            self.window.config(menu=self.menubar)
            self.window.withdraw()  # hide the main window

        else:
            self.window = None
            dpg.create_context()
            self.menubar = dpg.add_menu_bar()

    def run_tkinter(self):
        self.window.mainloop()

    def add_menu(self, label):
        if self.system == "Darwin":
            menu = tk.Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label=label, menu=menu)
            return menu
        else:
            return dpg.add_menu(label=label, parent=self.menubar)

    def add_menu_entry(self, menu, label, command):
        if self.system == "Darwin":
            menu.add_command(label=label, command=command)
        else:
            dpg.add_menu_item(label=label, callback=command, parent=menu)

    def add_cascade(self, menu, label):
        if self.system == "Darwin":
            cascade = tk.Menu(menu, tearoff=0)
            menu.add_cascade(label=label, menu=cascade)
            return cascade
        else:
            return dpg.add_menu(label=label, parent=menu)

    def add_submenu(self, menu, label):
        if self.system == "Darwin":
            submenu = tk.Menu(menu, tearoff=0)
            menu.add_cascade(label=label, menu=submenu)
            return submenu
        else:
            return dpg.add_menu(label=label, parent=menu)

    def hide_menu_entry(self, menu, label):
        if self.system == "Darwin":
            for index in range(menu.index(tk.END) + 1):
                if menu.entrycget(index, "label") == label:
                    menu.entryconfig(index, state=tk.DISABLED)
                    break
        else:
            dpg.hide_item(menu)

    def show_menu_entry(self, menu, label):
        if self.system == "Darwin":
            for index in range(menu.index(tk.END) + 1):
                if menu.entrycget(index, "label") == label:
                    menu.entryconfig(index, state=tk.NORMAL)
                    break
        else:
            dpg.show_item(menu)

    def change_menu_entry_callback(self, menu, label, new_command):
        if self.system == "Darwin":
            for index in range(menu.index(tk.END) + 1):
                if menu.entrycget(index, "label") == label:
                    menu.entryconfig(index, command=new_command)
                    break
        else:
            dpg.set_item_callback(menu, new_command)

    def change_menu_entry_label(self, menu, old_label, new_label):
        if self.system == "Darwin":
            for index in range(menu.index(tk.END) + 1):
                if menu.entrycget(index, "label") == old_label:
                    menu.entryconfig(index, label=new_label)
                    break
        else:
            dpg.set_item_label(menu, new_label)