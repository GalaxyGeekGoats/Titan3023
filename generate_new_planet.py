import random
import planetClass

colors = ("red", "blue", "green")
letters = ("x", "y", "z", "a", "u", "w")
def randomNumber(min, max) -> int:
    return random.randint(min, max)


min_temp = randomNumber(0, 300)
max_temp = randomNumber(200, 800)

def generate(   ):
    plan = planetClass.planet(
        letters[randomNumber(0, len(letters)-1)] + "-" + str(randomNumber(100, 999)),
        min_temp,
        max_temp,
        (min_temp+max_temp) / 2,
        randomNumber(1, 15000) / 1000,
        randomNumber(0, 1),
        randomNumber(0, 1),
        randomNumber(0, 1),
        colors[randomNumber(0, len(colors) - 1)]
    )

    plan.opis()