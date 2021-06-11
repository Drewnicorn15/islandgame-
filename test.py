import json

with open("jsonFiles/storyPath.json", "r") as actionList:
    data = json.loads(actionList.read())
    
    print(type(data["Flee"]))