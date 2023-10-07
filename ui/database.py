from textual.screen import Screen
from textual.widgets import Button, Select
from read_existing_planet import existing_planet_reader
from ui.label_change import LabelChange


class DatabaseScreen(Screen):
    def compose(self):
        yield Button("Back", id="back_btn", variant="default")
        yield Select(existing_planet_reader.planet_names, id="chosen_planet")
        yield Button("Confirm", id="confirm_btn", variant="success")
        yield LabelChange()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "confirm_btn":
            self.query_one(LabelChange).data = str(existing_planet_reader.read_planet(self.query_one("#chosen_planet").value))
        elif btn_id == "back_btn":
            self.app.pop_screen()
