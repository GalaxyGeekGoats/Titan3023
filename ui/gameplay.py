from textual.widgets import Header, Footer, Label, Button
from textual.screen import Screen
from gameplay.variables import StateSaver
from ui.build_ui import Build_ui
from ui.label_change import LabelChange

class Gameplay(Screen):
    def compose(self):
        stats = LabelChange(id="head")
        stats.styles.height = 1
        stats.data = StateSaver.get_stats()

        yield Header()
        yield stats
        yield Button("Build", id="build")
        yield Button("Remove", id="remove")
        yield Button("Shop", id="shop")
        yield Button("Next day", id="day")
        yield Footer()

    def _on_mount(self):
        self.query_one("#head").styles.align_vertical = "top"
        self.query_one("#head").data = StateSaver.get_stats()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "build":
            self.app.push_screen(Build_ui())
        elif btn_id == "remove":
            pass
        elif btn_id == "shop":
            pass
        elif btn_id == "day":
            pass
