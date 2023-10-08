import pandas as pd
from gameplay.building_class import Building


class BuildingReader:
    def __init__(self):
        self.__data = pd.read_csv("gameplay/buildings.csv", delimiter=';')
        self.building_name = [(building, i) for i, building in enumerate(self.__data.building_name)]

    def build_building(self, name):
        return Building(*self.__data.iloc[name])


building_reader = BuildingReader()
