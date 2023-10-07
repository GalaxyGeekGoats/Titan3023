from textual.widgets import Header, Footer, Button
from textual.screen import Screen
from ui.existing_planet import ExistingPlanet
from ui.custom_planet import CustomPlanet


class NewGame(Screen):
    def compose(self):
        yield Header()
        yield Button("Existing planet", id="Exist", variant="primary")
        yield Button("Custom planet", id="custom", variant="success")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "Exist":
            self.app.push_screen(ExistingPlanet())
        elif btn_id == "custom":
            self.app.push_screen(CustomPlanet())
        elif btn_id == "back":
            self.dismiss()
