import tkinter as tk
import keyboard

from utils.windows.window_overlay import WindowOverlay
from utils.windows.window_text_area_selector import WindowTextAreaSelector


class MainApp:
    def __init__(self, config):

        self.area_selector = None

        self.root = tk.Tk()
        self.root.geometry(f'{config["SCREEN"]["WIDTH"]}x{config["SCREEN"]["HEIGHT"]}+0+0')
        self.root.withdraw()

        self.area_selector = WindowTextAreaSelector(self.root, config)
        self.overlay_window = WindowOverlay(self.root)
        self.area_selector.overlay_window_class = self.overlay_window

        keyboard.add_hotkey(config["SCREENSHOOT"]["CREATE"], self.select_area)
        keyboard.add_hotkey(config["SCREENSHOOT"]["CLOSE"], self.close_overlay)


    def select_area(self):
        self.area_selector.setup_window()

    def close_overlay(self):
        self.overlay_window.close()

    def run(self):
        self.root.mainloop()