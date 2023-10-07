import pandas as pd
from building_class import Building

class BuildingReader:
    def __init__(self):
        self.__data =pd.read_csv("buildings.csv", delimeter=';')
        self.building_name = [(building, i) for i, building in enumerate(self.__data.building_name)]

    def read_building(self, row):
        plan = Building(*self.__data.iloc[row])
        return plan

building_reader = BuildingReader()
