from textual.app import App
from ui.settings import SettingsScreen
from ui.menu import Menu


lang = "polski"


class Titan3023(App):
    BINDINGS = [("s", "push_screen('settings')", "Settings")]
    SCREENS = {"menu": Menu, "settings": SettingsScreen}
    CSS_PATH = "./style.tcss"


    def on_mount(self):
        self.push_screen("menu")
