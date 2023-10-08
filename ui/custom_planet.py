from textual.widgets import Header, Footer, Button, Label, Input
from textual.screen import Screen
from ui.custom_planet_disc import CustomPlanetDisc
from generate_new_planet import generate_and_save

custom_name = ""


class CustomPlanet(Screen):
    def compose(self):
        yield Header()
        yield Label("Do you want to add custom name for planet or have a random (leave blank)?")
        yield Input("", id="input")
        yield Button("Go", id="go", variant="default")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        global custom_name
        btn_id = event.button.id
        if btn_id == "go":
            custom_name = self.query_one("#input").value
            generate_and_save()
            self.app.switch_screen(CustomPlanetDisc())
        elif btn_id == "back":
            self.dismiss()
