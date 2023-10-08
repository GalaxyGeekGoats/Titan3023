import json, time, os
from gameplay.grid import Grid
from planet_class import Planet
from gameplay.variables import StateSaver

import numpy as np


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


class FileSaver:
    @staticmethod
    def export_save():
        if not StateSaver.planet or not StateSaver.grid:
            return
        if not os.path.exists("./saves"):
            os.makedirs("./saves")
        name = "./saves/save_" + str(int(time.time())) + ".json"
        with open(name, "w") as f:
            json.dump({
                "resources": StateSaver.resources,
                "planet": StateSaver.planet.__dict__,
                "grid": {
                    "content": str(StateSaver.grid)
                }
            }, f, cls=NpEncoder)

    @staticmethod
    def load_save(file):
        with open(file, "r") as f:
            data = json.load(f)
        StateSaver.resources = data['resources']
        StateSaver.grid = Grid.load(**data['grid'])
        StateSaver.planet = Planet(**data['planet'])
