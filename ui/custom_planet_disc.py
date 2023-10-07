from textual.widgets import Header, Footer, Button, Label
from textual.screen import Screen

import ui.custom_planet
from ui.start import Start
from generate_new_planet import generate


class CustomPlanetDisc(Screen):
    def compose(self):
        name = ui.custom_planet.custom_name
        yield Header()
        if name == "":
            yield Label(generate())
        else:
            yield Label(generate(name))
        yield Button("Start", id="start", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "start":
            self.app.switch_screen(Start())
