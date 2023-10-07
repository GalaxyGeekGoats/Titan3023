from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Select, Static, Button, Label, Checkbox
from textual.containers import ScrollableContainer
from textual.screen import Screen, ModalScreen
from textual.reactive import reactive
from textual.binding import Binding

LANGUAGES = ["english", "polski", "deutsch"]
LANGUAGES = list(map(lambda x: (x, x), LANGUAGES))


class SettingsScreen(Screen):
    def compose(self):
        yield Select(LANGUAGES, id="select_lang")
        yield Button("Change language", id="lang_change", variant="default")
        yield Checkbox("Is darkmode enabled?", True, id="darkmode")
        yield Button("Save", id="save_btn", variant="success")

    def on_checkbox_changed(self, event):
        if event.checkbox.id == "darkmode":
            self.parent.dark = not self.parent.dark

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "lang_change":
            pass
            # if self.query_one("#select_lang").value  == "polski"
        elif btn_id == "save_btn":
            self.app.pop_screen()

class Credits(Screen):
    def compose(self):
        yield Header()
        yield Label("Authors:")
        yield Label("Adam, Robert, Witold")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.dismiss()

class Menu(Static):
    def compose(self):
        yield Button("Load", id="load", variant="primary")
        yield Button("New Game", id="new_game", variant="success")
        yield Button("Database", id="database", variant="warning")
        yield Button("Credits", id="credits", variant="default")
   
    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "credits":
            self.app.push_screen(Credits())

class Titan3023(App):
    BINDINGS = [("s", "push_screen('settings')", "Settings")]
    SCREENS = {"settings": SettingsScreen}
    CSS_PATH = "./style.tcss"

    def compose(self):
        yield Header()
        yield ScrollableContainer(Menu())
        yield Footer()

if __name__ == "__main__":
    app = Titan3023()
    app.run()
