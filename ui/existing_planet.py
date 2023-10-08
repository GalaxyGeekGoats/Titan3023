from textual.screen import Screen
from textual.widgets import Header, Footer, Select, Button, Label
from gameplay.variables import StateSaver
from read_existing_planet import existing_planet_reader
from ui.exist_planet_disc import ExistPlanetDisc

chosenPlanet = -1


class ExistingPlanet(Screen):
    def compose(self):
        yield Header()
        yield Label("Select planet to expedition:")
        yield Select(existing_planet_reader.planet_names, id="select_planet")
        yield Button("Choose", id="choose", variant="default")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        global chosenPlanet
        btn_id = event.button.id
        if btn_id == "choose":
            chosenPlanet = self.query_one("#select_planet").value
            plan = existing_planet_reader.read_planet(chosenPlanet)
            plan.generate_desc()
            StateSaver.planet = plan
            self.app.push_screen(ExistPlanetDisc())
        elif btn_id == "back":
            self.dismiss()
