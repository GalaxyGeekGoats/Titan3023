import openai, os

import ui.app


class Planet:
    def __init__(self, name, min_temp, max_temp, avg_temp, light_intensity, uranTF, ironTF, siliconTF, color, fun_fact, desc=""):
        self.name = name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.avg_temp = avg_temp
        self.light_intensity = light_intensity
        self.uranTF = uranTF
        self.ironTF = ironTF
        self.siliconTF = siliconTF
        self.color = color
        self.fun_fact = fun_fact
        self.desc = desc

    def __str__(self):
        return (
            f"name: {str(self.name)}\nmin_temp: {str(self.min_temp)}K\nmax_temp: {str(self.max_temp)}K\navg_temp: {str(self.avg_temp)}K\nlight_intensity: {str(self.light_intensity)}\nuranTF: {str(self.uranTF)}\nironTF: {str(self.ironTF)}\nciliconTF: {str(self.siliconTF)}\ncolor: {str(self.color)}\nfun_fact: {str(self.fun_fact)}")

    def generate_desc(self):
        openai.api_key = os.getenv("OPENAI_KEY")
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Opisz planete w języku: "+ ui.app.lang +" która jest: " + str(self),
            max_tokens=550,
            temperature=1
        )
        self.desc = response['choices'][0]['text']

    def custom_name(self, name):
        self.name = name
