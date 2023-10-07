from textual.screen import Screen
from textual.widgets import Button, Label, Header, Footer


class QuitScreen(Screen):
    def compose(self):
        yield Label("Do you want to quit? Your progress will be saved.")
        yield Button("Quit", id="quit_btn", variant="error")
        yield Button("Cancel", id="cancel_btn", variant="default")

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "quit_btn":
            self.app.exit()
        elif btn_id == "cancel_btn":
            self.app.pop_screen()
