from textual.widgets import Button, Header, Footer, Input
from textual.screen import Screen

class Menu(Screen):
    def compose(self):
        yield Header()
        yield Button("Load", id="load", variant="primary")
        yield Input("New Game", id="new_game")
        yield Button("Database", id="database", variant="warning")
        yield Button("Credits", id="credits", variant="default")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "credits":
            a = int(self.query_one("#new_game"))
            print(a)