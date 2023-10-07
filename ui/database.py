from textual.screen import Screen
from textual.reactive import reactive
from textual.widgets import Button, Select
from textual.widget import Widget
from read_existing_planet import readPlanet
import pandas as pd

data = pd.read_csv("existing_planets.csv", delimiter=';')
PLANETS = data.planet_name
PLANETS = [(planet, i) for i, planet in enumerate(PLANETS)]

class PlanetWidget(Widget):
    data = reactive("")

    def render(self):
        return self.data

class DatabaseScreen(Screen):
    def compose(self):
        yield Select(PLANETS, id="chosen_planet")
        yield Button("Confirm", id="confirm_btn", variant="success")
        yield PlanetWidget()
        yield Button("Back", id="back_btn", variant="default")

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "confirm_btn":
            self.query_one(PlanetWidget).data = readPlanet(self.query_one("#chosen_planet").value).info()
        elif btn_id == "back_btn":
            self.app.pop_screen()
