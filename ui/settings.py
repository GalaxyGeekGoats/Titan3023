from textual.widgets import Select, Button, Checkbox
from textual.screen import Screen

import ui.app

LANGUAGES = ["english", "polski", "deutsch", "Español", "日本語(Nihongo)", "Latinus"]
LANGUAGES = list(map(lambda x: (x, x), LANGUAGES))


class SettingsScreen(Screen):
    def compose(self):
        yield Select(LANGUAGES, id="select_lang")
        yield Button("Change language", id="lang_change", variant="default")
        yield Checkbox("Is darkmode enabled?", True, id="darkmode")
        yield Button("Save", id="save_btn", variant="success")

    def on_checkbox_changed(self, event):
        if event.checkbox.id == "darkmode":
            self.parent.dark = not self.parent.dark

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "save_btn":
            ui.app.lang = self.query_one("#select_lang").value
            self.app.pop_screen()
