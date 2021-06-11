import textParser
import json
from art import *
import time
import os
import pyttsx3
import past

class StoryTraverser:
    def __init__(self, gameName, fileRead):
        self.gameName = gameName
        self.fileRead = fileRead
        self.past = []

        self.actionPast = {
            "Flee": past.BoneHeadedWolf(
                "Bone Headed Wolf", 
                0,
                "a wolf that has a horn like structure which covers its face like a mask."
                ),
            "Go": past.Bunnimander(
                "Bunnimander", 
                1,
                "a creature that is a breed which is a mix between bunny and salamander."
                ),
            "Fight": past.Mamull(
                "Bone Headed Wold", 
                2,
                "a creature that is a breed between the Wooly Mammoth and a bull."
                ),
            "Skird": past.Skird(
                "Skird", 
                0,
                "a bird like creature which can hunt large predators."
                ),
            "Wood": past.Wood(
                "Wood", 
                0,
                "a resource that is used for construction and heat."
                ),
        }

    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    def traverseRecur(self, dictRead):
        os.system("cls")
    
        if dictRead["prompt"] == "Animal Check":
            print(dictRead["true"])
            self.speak(dictRead["true"])
            return(1)

        print(dictRead["prompt"])
        self.speak(dictRead["prompt"])

        while True:
            actionChoice = input("\nWhat is your action: ")
            if "past" in actionChoice.lower():
                actionChoice = actionChoice.split(" ")
                if len(actionChoice) == 1:
                    if len(self.past) == 0:
                        print("\nNothing currently in past.")
                    else:
                        for countI, i in enumerate(self.past):
                            print("{}: {}".format(countI, i.name))
                        
                        print("If you want information on any of the things in your inventory. Type in 'past [position inventory]'. If it is an animal, you can do past [position inventory] interact.")
                elif len(actionChoice) == 2:
                    try:
                        print(self.past[int(actionChoice[1])].useInfo())
                    except Exception as e:
                        print(e)
                        print("Invalid command. Try again.")
                elif len(actionChoice) == 3:
                    try:
                        self.past[int(actionChoice[1])].interact()
                    except AttributeError:
                        print("This object cannot interact. Try again.")
                else:
                    #print(actionChoice)
                    print("Invalid command. Try again.")

            else:
                break
            
        if len(actionChoice.split(" ")) == 1:
            actionChoice = actionChoice + " vaccine"
        elif len(actionChoice.split(" ")) > 2:
            actionChoice = " ".join(actionChoice.split(" ")[:2])

        actionChoice = textParser.TextParser(actionChoice)

        dictKeys = list(dictRead.keys())
        dictKeys.pop(dictKeys.index("prompt"))

        pairing = [dictKeys[0], 0]

        for i in dictKeys:
            count = 0
            for l in i.split(" "):
                for z in actionChoice:
                    if l.lower() == z.lower():
                        count += 1
            
            if pairing[1] < count:
                pairing = [i, count]

        for i in list(self.actionPast.keys()):
            if i == pairing[0]:
                self.past.append(self.actionPast[i])

        if type(dictRead[pairing[0]]) == str:
            print(dictRead[pairing[0]])
            self.speak(dictRead[pairing[0]])

        else:
            self.traverseRecur(dictRead[pairing[0]])
              

    def startTraverse(self):
        os.system("cls")
        print(text2art(self.gameName))
        print("\n\n" + "-"*20 + "\n\n")
        print("""
Directions: This is a text-based game so make sure that you follow all of the rules in
order for this game to work. In order to play, you will have to answer prompts
like Zork. Like Zork, the possiblilites will be hidden so make sure to read the prompts
correctly in order to answer. If you answer is not clear, a random choice will be taken.
In order for you to see the history of what you have done and see the animals and objects
you have seen, use the 'past' command at any time to access this info. Have fun. Some parts
of the game may be unfinished so be wary.
        """)
        self.speak("""
Directions: This is a text-based game so make sure that you follow all of the rules in
order for this game to work. In order to play, you will have to answer prompts
like Zork. Like Zork, the possiblilites will be hidden so make sure to read the prompts
correctly in order to answer. If you answer is not clear, a random choice will be taken.
In order for you to see the history of what you have done and see the animals and objects
you have seen, use the 'past' command at any time to access this info. Have fun. Some parts
of the game may be unfinished so be wary.
        """)

        ready = input("Press enter when ready: ")


        with open(self.fileRead, "r") as actionList:
            data = json.loads(actionList.read())
            self.traverseRecur(data)