import random
from planet_class import Planet
from gameplay.variables import StateSaver

colors = ("red", "blue", "green")
letters = ("x", "y", "z", "a", "u", "w")


def random_number(min, max) -> int:
    return random.randint(min, max)


min_temp = random_number(0, 300)
max_temp = random_number(200, 800)


def generate_and_save(name=letters[random_number(0, len(letters) - 1)] + "-" + str(random_number(100, 999))):
    plan = Planet(
        name,
        min_temp,
        max_temp,
        (min_temp + max_temp) / 2,
        random_number(1, 15000) / 1000,
        random_number(0, 1),
        random_number(0, 1),
        random_number(0, 1),
        colors[random_number(0, len(colors) - 1)]
    )
    plan.generate_desc()
    StateSaver.planet = plan
    return plan
