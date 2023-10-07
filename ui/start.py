from textual.widgets import Header, Footer, Label, Input, Button, DataTable
from textual.screen import Screen
from textual.validation import Function, Number, ValidationResult, Validator
from textual.reactive import reactive
from ui.label_change import LabelChange
from building_reader import building_reader
from rich.text import Text

ROWS = [
    ("NAME", "COST", "INPUT", "OUTPUT", ),
    (building_reader.read_building(0).name, str(building_reader.read_building(0).build_cost_value) + " x " + building_reader.read_building(0).build_cost, str(building_reader.read_building(0).input_value) + " x " + building_reader.read_building(0).building_input, str(building_reader.read_building(0).output_value) + " x " + building_reader.read_building(0).building_output),
    (building_reader.read_building(1).name,
     str(building_reader.read_building(1).build_cost_value) + " x " + str(building_reader.read_building(1).build_cost),
     str(building_reader.read_building(1).input_value) + " x " + str(building_reader.read_building(1).building_input),
     str(building_reader.read_building(1).output_value) + " x " + str(building_reader.read_building(1).building_output)),
    (building_reader.read_building(2).name,
     str(building_reader.read_building(2).build_cost_value) + " x " + str(building_reader.read_building(2).build_cost),
     str(building_reader.read_building(2).input_value) + " x " + str(building_reader.read_building(2).building_input),
     str(building_reader.read_building(2).output_value) + " x " + str(building_reader.read_building(2).building_output)),
    (building_reader.read_building(3).name,
     str(building_reader.read_building(3).build_cost_value) + " x " + str(building_reader.read_building(3).build_cost),
     str(building_reader.read_building(3).input_value) + " x " + str(building_reader.read_building(3).building_input),
     str(building_reader.read_building(3).output_value) + " x " + str(building_reader.read_building(3).building_output)),
    (building_reader.read_building(4).name,
     str(building_reader.read_building(4).build_cost_value) + " x " + str(building_reader.read_building(4).build_cost),
     str(building_reader.read_building(4).input_value) + " x " + str(building_reader.read_building(4).building_input),
     str(building_reader.read_building(4).output_value) + " x " + str(building_reader.read_building(4).building_output)),
    (building_reader.read_building(5).name,
     str(building_reader.read_building(5).build_cost_value) + " x " + str(building_reader.read_building(5).build_cost),
     str(building_reader.read_building(5).input_value) + " x " + str(building_reader.read_building(5).building_input),
     str(building_reader.read_building(5).output_value) + " x " + str(building_reader.read_building(5).building_output))

]

class Start(Screen):
    def compose(self):
        yield Header(id="Header")
        yield DataTable()
        yield Label("The rocket's payload is 21 units. Choose wisely so that you don't miss anything on your trip. You will be able to extract raw materials on the planet, but at the beginning you must choose how much of what you take.", id="desc")
        yield Label("Silicon:", id="silicon_text")
        yield Input(
            id="silicon_amount",
            placeholder="Enter a number...",
            validators=[
                Number(minimum=0, maximum=21),
            ],
        )
        yield Label("Iron:", id="iron_text")
        yield Input(
            id="iron_amount",
            placeholder="Enter a number...",
            validators=[
                Number(minimum=0, maximum=21),
            ],
        )
        yield Label("Uranium:", id="uranium_text")
        yield Input(
            id="uranium_amount",
            placeholder="Enter a number...",
            validators=[
                Number(minimum=0, maximum=21),
            ],
        )
        yield Button("Submit", id="submit_btn")
        yield LabelChange(id="return")
        yield Button("Next", id="next")
        yield Footer()

    def on_button_pressed(self, event):

        btn_id = event.button.id
        if btn_id == "submit_btn":
            try:
                silicon = int(self.query_one("#silicon_amount").value)
                iron = int(self.query_one("#iron_amount").value)
                uranium = int(self.query_one("#uranium_amount").value)
                if silicon + iron + uranium > 21 or silicon + iron + uranium < 0:
                    self.query_one("#return").data = "Rocket won't launch. Weight of materials is more than 21 or less than 0"
                else:
                    self.query_one("#return").data = "Good luck"

            except:
                self.query_one("#return").data = "Give a number!!!"
        elif btn_id == "next":
            pass

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        for row in ROWS[1:]:
            # Adding styled and justified `Text` objects instead of plain strings.
            styled_row = [
                Text(str(cell), style="italic #03AC13", justify="right") for cell in row
            ]
            table.add_row(*styled_row)