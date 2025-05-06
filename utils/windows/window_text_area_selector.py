
import pytesseract
import tkinter as tk
from tkinter import Canvas
from PIL import Image
from mss import mss

from utils.translate.argostranslate import argos_translate
from utils.translate.google import google_translate



class WindowTextAreaSelector:
    def __init__(self, master, config):
        self.canvas = None
        self.master = master
        self.window = None
        self.overlay_window_class = None
        self.is_selection_active = False
        self.config = config
        self.coords = {}
        self.coords_overlay = {}
        self.screenshoot_name = self.config["SCREENSHOOT"]["NAME"]

    def setup_window(self):
        if self.is_selection_active:
            return

        self.window = tk.Toplevel(self.master)
        self.window.overrideredirect(True)  # Убираем рамки окна
        self.window.geometry(f'{self.config["SCREEN"]["WIDTH"]}x{self.config["SCREEN"]["HEIGHT"]}+0+0')

        print(f"SCREEN: {self.window.winfo_screenwidth()}, {self.window.winfo_screenheight()}")

        self.window.attributes('-alpha', 0.2)
        self.window.attributes('-topmost', True)
        self.window.config(cursor='cross')
        self.canvas = Canvas(self.window, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # setup_bindings
        self.canvas.bind('<ButtonPress-1>', self.on_press)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_release)

        self.is_selection_active = True

    def on_press(self, event):
        self.coords = {
            'start_x': event.x_root,  # Используем данные из события
            'start_y': event.y_root,
            'rect': self.canvas.create_rectangle(0, 0, 0, 0, outline='red', width=2)
        }

    def on_drag(self, event):
        cur_x = event.x_root  # Фиксируем координаты из события
        cur_y = event.y_root
        self.canvas.coords(
            self.coords['rect'],
            self.coords['start_x'],
            self.coords['start_y'],
            cur_x,
            cur_y
        )

    def on_release(self, event):
        self.is_selection_active = False
        end_x = event.x_root  # Берем координаты из события
        end_y = event.y_root
        self.window.destroy()

        # Корректный расчет границ
        x1 = min(self.coords['start_x'], end_x)
        y1 = min(self.coords['start_y'], end_y)
        x2 = max(self.coords['start_x'], end_x)
        y2 = max(self.coords['start_y'], end_y)

        width = x2 - x1
        height = y2 - y1

        if width < 5 or height < 5:
            print("Слишком маленькая область")
            return

        with mss() as sct:
            self.coords_overlay = {'left': x1, 'top': y1, 'width': width, 'height': height}
            sct_img = sct.grab(self.coords_overlay)
            Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX').save(self.screenshoot_name)

        text_from_image = pytesseract.image_to_string(Image.open(self.screenshoot_name))
        text_from_image = text_from_image.replace("\n", " ")
        if text_from_image:
            match self.config["TRANSLATE_SYSTEM"]["SYSTEM"]:
                case "1":
                    text = google_translate(text_from_image)
                case "2":
                    text = argos_translate(text_from_image)
                case _:
                    text = "DONT SET config TRANSLATE_SYSTEM SYSTEM"

            self.overlay_window_class.create_overlay(text, x1, y1, width, height)