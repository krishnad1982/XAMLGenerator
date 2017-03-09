import json

# output and csv file paths
def readOutputPath(self):
    with open("config.json", encoding="utf-8-sig") as json_data_file:
        path=json.load(json_data_file)
        paths={"output":path["paths"][0]["output"],"csvpath":path["paths"][0]["csvpath"]}
        return paths
