import json

# output and csv file paths
def readConfigProperties(self):
    with open("config.json",mode="r") as json_data_file:
        properties = json.load(json_data_file)
        properties = {
            "output":properties["paths"][0]["output"],
            "csvpath":properties["paths"][0]["csvpath"],
            "groupbox":properties["settings"][0]["groupbox"],
            "gridname":properties["settings"][0]["gridname"],
            "importtype":properties["settings"][0]["importtype"]
            }
        return properties

def saveConfigDetails(self,output,csvpath,importtype):
    data = {}
    data['paths'] = []
    data['settings'] = []
    data['paths'].append({  
    'output': output,
    'csvpath': csvpath
    })
    data['settings'].append({  
    'groupbox': 'AlgoDetails',
    'gridname': 'AlgoGrid',
    'importtype': importtype
    })
    with open("config.json",mode="w") as write_json:
        json.dump(data, write_json)

