from textual.widgets import Header, Footer
from textual.screen import Screen


class Start(Screen):
    def compose(self):
        yield Header()
        yield Footer()