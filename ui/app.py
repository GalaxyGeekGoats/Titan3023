from textual.app import App
from textual.widgets import Header, Footer
from textual.containers import ScrollableContainer
from ui.settings import SettingsScreen
from ui.menu import Menu


class Titan3023(App):
    BINDINGS = [("s", "push_screen('settings')", "Settings")]
    SCREENS = {"settings": SettingsScreen}
    CSS_PATH = "./style.tcss"

    def compose(self):
        yield Header()
        yield ScrollableContainer(Menu())
        yield Footer()
