from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Select, Static, Button
from textual.screen import Screen
from ui.ExistingPlanet import ExistingPlanet
from ui.CustomPlanet import CustomPlanet


class NewGame(Screen):
    def compose(self):
        yield Header()
        yield Button("Existing planet", id="Exist", variant="primary")
        yield Button("Custom planet", id="custom", variant="success")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "Exist":
            self.app.push_screen(ExistingPlanet())
        if btn_id == "custom":
            self.app.push_screen(CustomPlanet())
