import json

data_to_save = {
    "uranium",
    "iron",
    "silicon",
    "energy",
    "heat"
}

file_path = "variables.json"

with open(file_path, "w") as json_file:
    json.dump(data_to_save, json_file)

with open(file_path, "r") as json_file:
    loaded_data = json.load(json_file)

"uranium" = loaded_data["uranium"]
"iron" = loaded_data["iron"]
"silicon" = loaded_data["silicon"]
"energy" = loaded_data["energy"]
"heat" = loaded_data["heat"]
