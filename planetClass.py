import openai

class planet:
    def __init__(self, name, min_temp, max_temp, avg_temp, light_intensity, uranTF, ironTF, siliconTF, color):
        self.name = name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.avg_temp = avg_temp
        self.light_intensity = light_intensity
        self.uranTF = uranTF
        self.ironTF = ironTF
        self.siliconTF = siliconTF
        self.color = color

    def info(self):
        return (f"name: {str(self.name)}\nmin_temp: {str(self.min_temp)}\nmax_temp: {str(self.max_temp)}\navg_temp: {str(self.avg_temp)}\nlight_intensity: {str(self.light_intensity)}\nuranTF: {str(self.uranTF)}\nironTF: {str(self.ironTF)}\nciliconTF: {str(self.siliconTF)}\ncolor: {str(self.color)}")

    def opis(self):
        openai.api_key = "[klucz]"
        response = openai.Completion.create(
           model="gpt-3.5-turbo-instruct",
           prompt = "Opisz planete która jest: "+self.info(),
           max_tokens = 500,
           temperature = 1
        )
        print(response['choices'][0]['text'])

    def custom_name(self, name):
        self.name=name