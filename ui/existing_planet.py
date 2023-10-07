from textual.widgets import Header, Footer, Select, Button, Label
from textual.screen import Screen
from ui.exist_planet_disc import ExistPlanetDisc
import pandas as pd

chosenPlanet = -1

data = pd.read_csv("existing_planets.csv", delimiter=';')
PLANETS = data.planet_name
PLANETS = [(planet, i) for i, planet in enumerate(PLANETS)]


class ExistingPlanet(Screen):
    def compose(self):
        yield Header()
        yield Label("Select planet to expedition:")
        yield Select(PLANETS, id="select_planet")
        yield Button("Choose", id="choose", variant="default")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "choose":
            chosenPlanet = self.query_one("#select_planet").value
            self.app.push_screen(ExistPlanetDisc())
        elif btn_id == "back":
            self.dismiss()
