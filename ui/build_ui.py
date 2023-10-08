from textual.widgets import Header, Footer, Label, Button, Input, DataTable, Select
from textual.screen import Screen
from rich.text import Text
from gameplay.building_reader import building_reader
from gameplay.variables import StateSaver

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


TOBUILD =[]
i = 0
while i < 6:
    if building_reader.build_building(i).build_cost == "Iron" and int(building_reader.build_building(i).build_cost_value) <= int(StateSaver.resources.get("iron")):
        TOBUILD.append(str(building_reader.build_building(i).name))
    elif building_reader.build_building(i).build_cost == "Silicon" and int(building_reader.build_building(i).build_cost_value) <= int(StateSaver.resources.get("silicon")):
        TOBUILD.append(str(building_reader.build_building(i).name))
    elif building_reader.build_building(i).build_cost == "Energy" and int(building_reader.build_building(i).build_cost_value) <= int(StateSaver.resources.get("electricity")):
        TOBUILD.append(str(building_reader.build_building(i).name))
    i+=1

TOBUILD = list(map(lambda x: (x, x), TOBUILD))


class Build_ui(Screen):
    def compose(self):
        yield Header()
        yield Label("Day: " + str(StateSaver.resources["day"]) + "   Iron: " + str(
            StateSaver.resources.get("iron")) + "   Uran: " + str(StateSaver.resources["uran"]) + "   Silicon: " + str(
            StateSaver.resources["silicon"]) + "   Electricity: " + str(StateSaver.resources["electricity"]), id="head")
        yield DataTable()
        yield Select(TOBUILD, id="select_build")
        yield Button("Build", id="build", variant="default")
        yield Button("Back", id="back", variant="default")
        yield Footer()

    def on_mount(self):
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
            pass
        elif btn_id == "back":
            self.dismiss()
