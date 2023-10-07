from textual.widgets import Header, Footer, Button, Label
from textual.screen import Screen
from ui.start import Start
from generate_new_planet import generate


class CustomPlanetDisc(Screen):
    def compose(self):
        yield Header()
        yield Label(generate())
        yield Button("Start", id="start", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "Start":
            self.app.switch_screens(Start())
