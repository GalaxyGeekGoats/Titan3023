from textual.widgets import Header, Footer, Label
from textual.screen import Screen
from ui.start import Start


class CustomPlanetDisc(Screen):
    def compose(self):
        yield Header()
        yield Label("You woke up. Did you sleep well. Overnight your machines: ")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "start":
            self.app.switch_screen(Start())
