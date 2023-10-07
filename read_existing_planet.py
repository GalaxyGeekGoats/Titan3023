import pandas as pd
import planetClass

def readPlanet(row):
    data= pd.read_csv("existing_planets.csv", delimiter=';')
    plan = planetClass.planet(
        data.planet_name[row],
        data.min_temp[row],
        data.max_temp[row],
        data.avg_temp[row],
        data.light_intensity[row],
        data.Uranium[row],
        data.Iron[row],
        data.Silicon[row],
        data.Colour[row]
    )

    plan.opis()