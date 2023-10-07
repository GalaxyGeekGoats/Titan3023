from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Select, Static, Button, Label, Checkbox
from textual.containers import ScrollableContainer
from textual.screen import Screen, ModalScreen
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

