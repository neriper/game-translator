import tkinter as tk


class WindowOverlay:
    def __init__(self, master):
        self.canvas = None
        self.master = master
        self.window = None
        self.is_selection_active = False

    def close(self):
        self.window.destroy()

    def create_overlay(self, text, x, y, width, height):
        # Создаем окно с переводом
        self.window = tk.Toplevel(self.master)
        self.window.overrideredirect(True)  # Убираем декорации окна
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.attributes("-topmost", True)  # Поверх всех окон
        # root.attributes("-transparentcolor", "white")  # Делаем белый цвет прозрачным
        self.window.config(bg="white")  # Устанавливаем белый фон

        # Создаем холст для рисования
        canvas = tk.Canvas(self.window, bg="white", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Добавляем текст
        print(text)
        canvas.create_text(
            width // 2,
            height // 2,
            text=text,
            fill="black",
            font=("Arial", 14),
            width=width - 5,
            justify=tk.CENTER
        )

        # Кнопка для выхода (опционально)
        btn_quit = tk.Button(
            self.window,
            text="X",
            command=self.window.destroy,
            bd=0,
            bg="red",
            fg="white"
        )
        btn_quit.place(relx=1.0, x=-2, y=2, anchor=tk.NE)