from textual.screen import Screen
from textual.reactive import reactive
from textual.widgets import Button, Select
from textual.widget import Widget
from read_existing_planet import existing_planet_reader
import pandas as pd

class PlanetWidget(Widget):
    data = reactive("")

    def render(self):
        return self.data


class DatabaseScreen(Screen):
    def compose(self):
        yield Select(existing_planet_reader.planet_names, id="chosen_planet")
        yield Button("Confirm", id="confirm_btn", variant="success")
        yield PlanetWidget()
        yield Button("Back", id="back_btn", variant="default")

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "confirm_btn":
            self.query_one(PlanetWidget).data = str(existing_planet_reader.read_planet(self.query_one("#chosen_planet").value))
        elif btn_id == "back_btn":
            self.app.pop_screen()
