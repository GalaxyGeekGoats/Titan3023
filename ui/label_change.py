from textual.widget import Widget
from textual.reactive import reactive


class LabelChange(Widget):
    data = reactive("")

    def render(self):
        return self.data
