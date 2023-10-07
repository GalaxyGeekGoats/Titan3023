from textual.widgets import Button, Header, Footer
from ui.credits import Credits
from ui.new_game import NewGame
from textual.screen import Screen
from textual.containers import Container, Vertical
from ui.database import DatabaseScreen


class Menu(Screen):
    def compose(self):
        yield Header()
        yield Button("Load", id="load", variant="primary")
        yield Button("New Game", id="new_game", variant="success")
        yield Button("Database", id="database", variant="warning")
        yield Button("Credits", id="credits", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "credits":
            self.app.push_screen(Credits())
        elif btn_id == "new_game":
            self.app.push_screen(NewGame())
        elif btn_id == "database":
            self.app.push_screen(DatabaseScreen())
