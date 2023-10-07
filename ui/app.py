from textual.app import App
from ui.settings import SettingsScreen
from ui.menu import Menu
from ui.quit_screen import QuitScreen

class Titan3023(App):
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [("s", "push_screen('settings')", "Settings"), 
                ("q", "push_screen('quit_screen')", "Quit")]
    SCREENS = {"menu": Menu, "settings": SettingsScreen, "quit_screen": QuitScreen}
    CSS_PATH = "./style.tcss"

    def on_mount(self):
        self.push_screen("menu")
