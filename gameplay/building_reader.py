import pandas as pd
from gameplay.building_class import Building


class BuildingReader:
    def __init__(self):
        self.__data = pd.read_csv("gameplay/buildings.csv", delimiter=';')
        self.building_names = {building: i for i, building in enumerate(self.__data.building_name)}
        self.building_emotes = {emote: i for i, emote in enumerate(self.__data['emote'].tolist())}

    def build_building(self, row):
        return Building(*self.__data.iloc[row])


building_reader = BuildingReader()
