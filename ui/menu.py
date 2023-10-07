from textual.widgets import Static, Button
from ui.credits import Credits


class Menu(Static):
    def compose(self):
        yield Button("Load", id="load", variant="primary")
        yield Button("New Game", id="new_game", variant="success")
        yield Button("Database", id="database", variant="warning")
        yield Button("Credits", id="credits", variant="default")
   
    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "credits":
            self.app.push_screen(Credits())
