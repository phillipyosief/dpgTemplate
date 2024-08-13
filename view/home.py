import dearpygui.dearpygui as dpg


class Home:
    def __init__(self):
        with dpg.window(label="Home") as self.window:
            dpg.add_text("Welcome to the Home window!")
