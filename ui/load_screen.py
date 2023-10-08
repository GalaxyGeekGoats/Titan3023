from textual.widgets import Header, Footer, Select, Button
from textual.screen import Screen
import os
from gameplay.file_saver import FileSaver
from ui.gameplay import Gameplay


class LoadScreen(Screen):
    def compose(self):
        yield Header()
        yield Select([
            (file, "./saves/" + file) for file in os.listdir("./saves")
        ], id="selected_save")
        yield Button("Load", id="load_btn", variant="warning")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        r = self.query_one("#selected_save").value
        if event.button.id == "load_btn" and r:
            FileSaver.load_save(r)
            self.dismiss()
            self.app.switch_screen(Gameplay())
        elif event.button.id == "back":
            self.dismiss()
