from textual.widgets import Header, Footer, Button, Label
from textual.screen import Screen

import ui.custom_planet
from ui.start import Start


class CustomPlanetDisc(Screen):
    def compose(self):
        yield Header()
        yield Label("You woke up. Did you sleep well. Overnight your machines: ") #do dodania co zostało dodane
        #dodać losowanie random eventów
        yield Footer()

    def on_button_pressed(self, event):

        btn_id = event.button.id
        if btn_id == "start":
            self.app.switch_screen(Start())
