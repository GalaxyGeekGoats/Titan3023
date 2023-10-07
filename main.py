from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Select, Static, Button, Label
from textual.containers import ScrollableContainer

LANGUAGES = ["english", "polski", "deutsch"]
LANGUAGES = list(map(lambda x: (x, x), LANGUAGES))


class Credits(Static):
    def compose(self):
        yield Label("Authors:")
        yield Label("Adam, Robert, Witold")
        yield Button("Back", id="back", variant="default")

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.parent.mount(Menu())
            self.remove()

class Settings(Static):
    select = Select(LANGUAGES)

    def compose(self):
        yield select
        yield Button("Change language", id="lang_change", variant="default")

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "lang_change":
            if select.value == "polski": self.remove()




class Menu(Static):
    def compose(self):
        yield Button("Load", id="load", variant="primary")
        yield Button("New Game", id="new_game", variant="success")
        yield Button("Database", id="database", variant="warning")
        yield Button("Credits", id="credits", variant="default")
        yield Button("Settings", id="settings", variant="default")
   
    def __switch_widget(self, widget_class):
            self.parent.mount(widget_class())
            self.remove()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id in ELEMENTS:
            self.__switch_widget(ELEMENTS[event.button.id])

class Titan3023(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "./style.tcss"

    def compose(self):
        yield Header()
        yield ScrollableContainer(Menu())
        yield Footer()

    def action_toggle_dark(self):
        self.dark = not self.dark


ELEMENTS = {"credits": Credits, "settings": Settings}
if __name__ == "__main__":
    app = Titan3023()
    app.run()
