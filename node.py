import textParser
#for the init method infoonpath is expacted to be list or tuple in order of: 
#Actions & data for action [action,]
#interacble objects
class node:
    def __init__(self,infoonpath):
        self.thingsinspace = infoonpath[1]
        self.actions = infoonpath[0]
    def actionhappened(self,input):
        realinput = textParser.TextParser(input)
        for i in self.actions():
            if realinput == i[1]:
                return i[0]
    def removeitem(self,item):
        self.thingsinspace.remove(item)
    def additem(self,item):
        self.thingsinspace.append(item)