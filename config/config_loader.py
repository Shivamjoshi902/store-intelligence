import json

def load_config():

    with open("config/store_config.json", "r") as file:
        return json.load(file)