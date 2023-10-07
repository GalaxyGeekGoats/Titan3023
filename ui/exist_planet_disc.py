from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label


class ExistPlanetDisc(Screen):
    def compose(self):
        yield Header()
        yield Label(self.app.screen_stack[-2])
        yield Button("Choose", id="choose", variant="default")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    #def on_button_pressed(self, event):
    #    btn_id = event.button.id
    #    if btn_id == "choose":
    #    elif btn_id == "back":
    #        self.dismiss()