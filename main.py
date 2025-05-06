from configparser import ConfigParser

from utils.windows.window_main_app import MainApp


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")

    app = MainApp(config=config)
    app.run()
