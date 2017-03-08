import json

def readOutputPath(self):
    with open("config.json", encoding="utf-8-sig") as json_data_file:
        path=json.load(json_data_file)
        return path["paths"][0]["output"]