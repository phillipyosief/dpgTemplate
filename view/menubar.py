import tkinter as tk
from tkinter import messagebox
import dearpygui.dearpygui as dpg
import platform

class MenuManager:
    def __init__(self):
        self.system = platform.system()
        if self.system == "Darwin":  # macOS
            self.window = tk.Tk()
            self.window.title("Main")
            self.menubar = tk.Menu(self.window)
            self.window.config(menu=self.menubar)
        else:
            self.window = None
            dpg.create_context()
            self.menubar = dpg.add_menu_bar()

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

    def show(self):
        if self.system == "Darwin":
            self.window.mainloop()
        else:
            dpg.create_viewport(title='Custom Title', width=800, height=600)
            dpg.setup_dearpygui()
            dpg.show_viewport()
            dpg.start_dearpygui()
            dpg.destroy_context()

def do_about_dialog():
    if menu_manager.system == "Darwin":
        tk_version = menu_manager.window.tk.call('info', 'patchlevel')
        messagebox.showinfo(message=app_name + "\nThe answer to all your problems.\n\nTK version: " + tk_version)
    else:
        print("About dialog")

def do_preferences():
    if menu_manager.system == "Darwin":
        messagebox.showinfo(message="Preferences window")
    else:
        print("Preferences window")

def do_button():
    print("You pushed my button")

if __name__ == "__main__":
    app_name = "Chocolate Rain"
    menu_manager = MenuManager()

    app_menu = menu_manager.add_menu('Apple')
    menu_manager.add_menu_entry(app_menu, 'About ' + app_name, do_about_dialog)
    menu_manager.add_menu_entry(app_menu, 'Preferences...', do_preferences)

    if menu_manager.system != "Darwin":
        with dpg.window(label="Main Window"):
            dpg.add_button(label="Push", callback=do_button)

    menu_manager.show()