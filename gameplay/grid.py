from gameplay.building_reader import building_reader
from gameplay.variables import StateSaver
import random

class Grid:
    SIZE = 5
    # require planet for load too
    def __init__(self):
        self.content = [[None] * Grid.SIZE for _ in range(Grid.SIZE)]

    def validate(x, y):
        return x >= 0 and x < Grid.SIZE and y >= 0 and y < Grid.SIZE

    def begin_new_day(self):
        for row in self.content:
            for cell in row:
                if cell:
                    if cell.building_input != "None":
                        StateSaver.resources[cell.bulding_input.lower()] -= cell.input_value
                    if cell.name == "Extractor":
                        resources = []
                        if StateSaver.planet.uranTF:
                            resources.append("uran")
                        
                        if StateSaver.planet.siliconTF:
                            resources.append("silicon")

                        if StateSaver.planet.ironTF:
                            resources.append("iron")
                        
                        if len(resources) > 0:
                            StateSaver.resources[random.choice(resources)] += cell.output_value
                    elif cell.building_output != "None":
                        StateSaver.resources[cell.bulding_output.lower()] += cell.output_value
    
    def __str__(self):
       return "\n".join(["\t".join(["_" if not cell else cell.emote for cell in row]) for row in self.content]) 

    def remove(self, x, y) -> bool:
        if not Grid.validate(x, y) or not self.content[x][y]: return False
        build = self.content[x][y]
        self.content[x][y] = None
        StateSaver.resources[build.build_cost.lower()] += build.build_cost_value
        return True

    def build(self, type, x, y) -> bool:
        if not Grid.validate(x, y) or self.content[x][y]: return False
        build = building_reader.build_building(type)
        if type == "Hub":
            temp_unit = "Radiator" if StateSaver.planet.avg_temp > 273 else "Heater"
            good_placement = self._check_proximity(temp_unit, x, y)
            if not good_placement:
                return False
        StateSaver.resources[build.build_cost.lower()] -= build.build_cost_value
        self.content[x][y] = build
        return True

    def _check_proximity(self, name, x, y):
        coords = [[1,0], [0,1], [-1,0], [0,-1]]
        for i,j in coords:
            newx = x+i
            newy = y+j
            if Grid.validate(newx, newy):
                if self.content[newx][newy].name == name: return True
        return False

StateSaver.grid = Grid()
