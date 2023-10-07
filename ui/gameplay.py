from textual.widgets import Header, Footer, Button
from textual.screen import Screen


class Gameplay(Screen):
    def compose(self):
        yield Header("aaa")
        yield Button("Existing planet", id="Exist", variant="primary")
        yield Button("Custom planet", id="custom", variant="success")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        pass
