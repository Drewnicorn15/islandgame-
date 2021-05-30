import json

def TextParser(prompt):
    prompt1, prompt2 = prompt.split(" ")

    with open("jsonFiles/connectedVerbs.json", "r") as verbList:
        data = json.loads(verbList.read())
        
        for i in data:
            for l in data[i]:
                if str(l).lower() == prompt1.lower():
                    prompt1 = i

    with open("jsonFiles/connectedActions.json", "r") as actionList:
        data = json.loads(actionList.read())
        
        for i in data:
            for l in data[i]:
                if str(l).lower() == prompt2.lower():
                    prompt2 = i

    return(prompt1, prompt2)

