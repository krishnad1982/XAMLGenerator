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
            "importtype":properties["settings"][0]["importtype"],
            "skinversion":properties["settings"][0]["skinversion"],
            "versiontextblock":properties["settings"][0]["versiontextblock"]
            }
        return properties

def saveConfigDetails(self,output,csvpath,importtype,groupbox,gridname,versiontextblock,skinversion):
    data = {}
    data['paths'] = []
    data['settings'] = []
    data['paths'].append({  
    'output': output,
    'csvpath': csvpath
    })
    data['settings'].append({  
    'importtype': importtype,
    'groupbox': groupbox,
    'gridname': gridname,
    'versiontextblock':versiontextblock,
    'skinversion':skinversion
    })
    with open("config.json",mode="w") as write_json:
        json.dump(data, write_json)

