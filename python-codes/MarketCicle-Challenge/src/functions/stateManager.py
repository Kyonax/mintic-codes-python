def stateManagerRead (json,path):     
    with open(path) as f:
        jsonFile = json.load(f)
    return jsonFile

def stateManagerWrite (json,jsonFile,path):
    with open(path,'w') as outFile:
        json.dump(jsonFile,outFile)

def stateManagerConsole (json,jsonFile,path):
    return json.dumps(jsonFile, indent=4, sort_keys=True)