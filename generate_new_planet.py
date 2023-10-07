import random
from planet_class import Planet

colors = ("red", "blue", "green")
letters = ("x", "y", "z", "a", "u", "w")


def random_number(min, max) -> int:
    return random.randint(min, max)


min_temp = random_number(0, 300)
max_temp = random_number(200, 800)


def generate():
    plan = Planet(
        letters[random_number(0, len(letters) - 1)] + "-" + str(random_number(100, 999)),
        min_temp,
        max_temp,
        (min_temp + max_temp) / 2,
        random_number(1, 15000) / 1000,
        random_number(0, 1),
        random_number(0, 1),
        random_number(0, 1),
        colors[random_number(0, len(colors) - 1)]
    )

    return plan.desc()
