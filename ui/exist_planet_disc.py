from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label
from read_existing_planet import existing_planet_reader
import ui.existing_planet
from gameplay.variables import StateSaver
from ui.start import Start


class ExistPlanetDisc(Screen):
    def compose(self):
        yield Header()
        yield Label(StateSaver.planet.desc)
        yield Button("Choose", id="choose", variant="default")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "choose":
            self.app.switch_screen(Start())
        elif btn_id == "back":
            self.dismiss()