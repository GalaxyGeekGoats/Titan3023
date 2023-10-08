import pandas as pd
from planet_class import Planet


class ExistingPlanetReader:
    def __init__(self):
        self.__data = pd.read_csv("existing_planets.csv", delimiter=';')
        self.planet_names = [(planet, i) for i, planet in enumerate(self.__data.planet_name)]

    def read_planet(self, row):
        plan = Planet(*self.__data.iloc[row])
        return plan


existing_planet_reader = ExistingPlanetReader()
