import dearpygui.dearpygui as dpg

from view.home import Home


class App:
    def __init__(self):
        self.home = Home()


if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport(title='Dear PyGui',
                        small_icon='',
                        large_icon='',
                        width=1280,
                        height=800,
                        x_pos=100,
                        y_pos=100,
                        min_width=250,
                        max_width=10000,
                        min_height=250,
                        max_height=10000,
                        resizable=True,
                        vsync=True,
                        always_on_top=False,
                        decorated=True,
                        clear_color=(0, 0, 0, 255),
                        disable_close=False)

    app = App()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(app.home.window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()
