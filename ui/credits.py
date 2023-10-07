from textual.widgets import Header, Footer, Button, Label
from textual.screen import Screen


class Credits(Screen):
    def compose(self):
        yield Header()
        yield Label("Created by the Galaxy Geek Goats team during the 2023 NASA Space Apps Hackathon Stalowa Wola")
        yield Label("Adam Wasiak - Backend and Frontend Developer in Python, Application Build")
        yield Label("Robert Gruszczyński - Backend Developer in Python, Game Systems")
        yield Label("Witold Żotkiewicz - Game Design and Database Management")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.dismiss()
