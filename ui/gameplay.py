from textual.widgets import Header, Footer, Label, Button
from textual.screen import Screen
from gameplay.variables import StateSaver
from ui.build_ui import Build_ui


class Gameplay(Screen):
    def compose(self):
        yield Header()
        yield Label("Day: " + str(StateSaver.resources["day"]) + "   Iron: " + str(
            StateSaver.resources["iron"]) + "   Uran: " + str(StateSaver.resources["uran"]) + "   Silicon: " + str(
            StateSaver.resources["silicon"]) + "   Electricity: " + str(StateSaver.resources["electricity"]), id="head")
        yield Button("Build", id="build")
        yield Button("Remove", id="remove")
        yield Button("Shop", id="shop")
        yield Button("Next day", id="day")
        yield Footer()

    def _on_mount(self):
        self.app.query_one("#head").styles.align_vertical = "top"

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "build":
            self.app.switch_screen(Build_ui())
        elif btn_id == "remove":
            pass
        elif btn_id == "shop":
            pass
        elif btn_id == "day":
            pass
