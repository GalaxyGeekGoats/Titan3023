from textual.widgets import Header, Footer, Label, Button, DataTable, Select, Input
from textual.screen import Screen
from rich.text import Text
from gameplay.building_reader import building_reader
from gameplay.variables import StateSaver
from textual.validation import Number
from ui.label_change import LabelChange

# do not remove
import gameplay.grid

ROWS = [
    ("NAME", "COST", "INPUT", "OUTPUT",)

]
for i in range(6):
    ROWS.append(
        (str(building_reader.build_building(i).name),
         str(building_reader.build_building(i).build_cost_value) + " x " + str(
             building_reader.build_building(i).build_cost),
         str(building_reader.build_building(i).input_value) + " x " + str(
             building_reader.build_building(i).building_input),
         str(building_reader.build_building(i).output_value) + " x " + str(
             building_reader.build_building(i).building_output)))

def generate_to_build():
    to_build = []
    for z in range(6):
        if building_reader.build_building(z).build_cost == "Iron" and int(building_reader.build_building(z).build_cost_value) <= int(StateSaver.resources["iron"]):
            to_build.append((str(building_reader.build_building(z).name), z))
        elif building_reader.build_building(z).build_cost == "Silicon" and int(building_reader.build_building(z).build_cost_value) <= int(StateSaver.resources["silicon"]):
            to_build.append((str(building_reader.build_building(z).name), z))
    return to_build

def get_stats():
    return "Day: " + str(StateSaver.resources["day"]) + "   Iron: " + str(StateSaver.resources.get("iron")) + "   Uran: " + str(StateSaver.resources["uran"]) + "   Silicon: " + str(StateSaver.resources["silicon"]) + "   Electricity: " + str(StateSaver.resources["electricity"])

class Build_ui(Screen):
    def compose(self):
        grid_label = LabelChange(id="grid")
        grid_label.data = str(StateSaver.grid)

        yield Header()
        yield Label(get_stats(), id="head")
        yield DataTable()
        yield Select(generate_to_build(), id="select_build")
        yield Button("Build", id="build", variant="default")
        yield Button("Back", id="back", variant="default")
        yield Input(
            id="x",
            placeholder="Enter a digit...",
            validators=[
                Number(minimum=0, maximum=5),
            ]
        )
        yield Input(
            id="y",
            placeholder="Enter a digit...",
            validators=[
                Number(minimum=0, maximum=5),
            ]
        )
        yield grid_label
        yield Footer()

    def on_mount(self):
        self.query_one("#grid").styles.text_align = "right"
        self.query_one("#grid").styles.width = "50%"
        #self.query_one("#grid").styles.margin = (0,0,300,300)
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        for row in ROWS[1:]:
            styled_row = [
                Text(str(cell), style="italic #03AC13", justify="right") for cell in row
            ]
            table.add_row(*styled_row)

    def on_button_pressed(self, event):
        btn_id = event.button.id
        if btn_id == "build":
            selected_type = self.query_one("#select_build").value
            try:
                x = int(self.query_one("#x").value)
                y = int(self.query_one("#y").value)
                if StateSaver.grid.build(selected_type, x, y):
                    self.query_one("#grid").data = str(StateSaver.grid)
                    self.query_one("#select_build").value = None
                    self.query_one("#select_build").set_options(generate_to_build())
                self.refresh()
            except ValueError:
                pass
        elif btn_id == "back":
            self.dismiss()
        self.query_one("#head").value = get_stats()
