from textual.widgets import Header, Footer, Label, Input, Button, DataTable
from textual.screen import Screen
from textual.validation import Number

from gameplay.building_reader import building_reader
from gameplay.variables import resources
from ui.label_change import LabelChange
from rich.text import Text
from ui.gameplay import Gameplay

ROWS = [
    ("NAME", "COST", "INPUT", "OUTPUT",)

]
i = 0
while i < 6:
    ROWS.append(
        (str(building_reader.build_building(i).name),
         str(building_reader.build_building(i).build_cost_value) + " x " + str(
             building_reader.build_building(i).build_cost),
         str(building_reader.build_building(i).input_value) + " x " + str(
             building_reader.build_building(i).building_input),
         str(building_reader.build_building(i).output_value) + " x " + str(
             building_reader.build_building(i).building_output)))
    i += 1


class Start(Screen):
    def compose(self):

        yield Header(id="Header")
        yield DataTable()
        yield Label(
            "The rocket's payload is 21 units. Choose wisely so that you don't miss anything on your trip. You will be able to extract raw materials on the planet, but at the beginning you must choose how much of what you take.",
            id="desc")
        yield Label("Silicon:", id="silicon_text")
        yield Input(
            id="silicon_amount",
            placeholder="Enter a number...",
            validators=[
                Number(minimum=0, maximum=21),
            ]
        )
        yield Label("Iron:", id="iron_text")
        yield Input(
            id="iron_amount",
            placeholder="Enter a number...",
            validators=[
                Number(minimum=0, maximum=21),
            ]
        )
        yield Label("Uranium:", id="uranium_text")
        yield Input(
            id="uranium_amount",
            placeholder="Enter a number...",
            validators=[
                Number(minimum=0, maximum=21),
            ]
        )
        yield Button("Submit", id="submit_btn")
        yield LabelChange(id="return")
        yield Footer()

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "submit_btn":
            try:
                silicon = int(str(self.query_one("#silicon_amount").value))
                iron = int(str(self.query_one("#iron_amount").value))
                uranium = int(str(self.query_one("#uranium_amount").value))
                if silicon + iron + uranium > 21 or silicon + iron + uranium < 0:
                    self.query_one(
                        "#return").data = "Rocket won't launch. Weight of materials is more than 21 or less than 0"
                else:
                    resources.update({"iron": iron})
                    resources["silicon"] = silicon
                    resources["uran"] = uranium
                    self.app.switch_screen(Gameplay())


            except:
                self.query_one("#return").data = "Give a number!!!"

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        for row in ROWS[1:]:
            # Adding styled and justified `Text` objects instead of plain strings.
            styled_row = [
                Text(str(cell), style="italic #03AC13", justify="right") for cell in row
            ]
            table.add_row(*styled_row)
