from textual.widgets import Header, Footer, Select, Static, Button, Label, Checkbox
from textual.screen import Screen, ModalScreen

class Credits(Screen):
    def compose(self):
        yield Header()
        yield Label("Authors:")
        yield Label("Adam, Robert, Witold")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.dismiss()


