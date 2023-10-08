class StateSaver:
    resources = {
        "iron": 0,
        "uran": 0,
        "silicon": 0,
        "electricity": 0,
        "day": 0
    }

    planet = None

    grid = None

    @staticmethod
    def get_stats():
        return "Day: " + str(StateSaver.resources["day"]) + "   Iron: " + str(
            StateSaver.resources.get("iron")) + "   Uran: " + str(StateSaver.resources["uran"]) + "   Silicon: " + str(
            StateSaver.resources["silicon"]) + "   Electricity: " + str(StateSaver.resources["electricity"])

