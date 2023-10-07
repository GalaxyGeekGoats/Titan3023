from textual.widgets import Button, Header, Footer
from ui.credits import Credits
from ui.NewGame import NewGame
from textual.screen import Screen

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
        if btn_id == "new_game":
            self.app.switch_screen(NewGame())
