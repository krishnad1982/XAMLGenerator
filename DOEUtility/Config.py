import json

# output and csv file paths
def readConfigProperties(self):
    with open("config.json", encoding="utf-8-sig") as json_data_file:
        properties=json.load(json_data_file)
        properties={
            "output":properties["paths"][0]["output"],
            "csvpath":properties["paths"][0]["csvpath"],
            "gridname":properties["settings"][0]["gridname"]
            }
        return properties
