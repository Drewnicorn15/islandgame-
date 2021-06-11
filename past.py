class item():
    def __init__(self, name, position, use):
        self.name = name
        self.position = position
        self.use = use

    def useInfo(self):
        return("{}. Currently in position {} in your hotbar. {} is {}".format(self.name, self.position, self.name, self.use))


class Mamull(item):
    def __init__(self, name, position, use):
        self.name = name
        self.position = position
        self.use = use
        self.username = ""
        super().__init__(name, position, use)

    def interact(self):
        print("Roar!!! I am the Mamull.")
        if self.username == "":
            self.username = input(" What is your name: ")

        print("Hello {}, let me tell you something about me.".format(self.username))
        print("I have hooks on the soles of my feet and the edges in order to walk in the snow.")
        print("I live in large volcano caves")
        print("Finally, I have extra fat storage to keep warm during the winter.")
        print("Those are some details about me")

class BoneHeadedWolf(item):
    def __init__(self, name, position, use):
        self.name = name
        self.position = position
        self.use = use
        self.username = ""
        super().__init__(name, position, use)

    def interact(self):
        print("Awoooo! I am the Bone Headed Wolf")
        if self.username == "":
            self.username = input(" What is your name: ")

        print("Hello {}, let me tell you something about me.".format(self.username))
        print("I have the ability to sense heat to find prey that burrow.")
        print("I have occasional nomad tendencies if food source moves")
        print("Finally, my scientific name is Canis Ossum")
        print("Those are some details about me")

class Skird(item):
    def __init__(self, name, position, use):
        self.name = name
        self.position = position
        self.use = use
        self.username = ""
        super().__init__(name, position, use)

    def interact(self):
        print("Tweet! I am the Skird")
        if self.username == "":
            self.username = input(" What is your name: ")

        print("Hello {}, let me tell you something about me.".format(self.username))
        print("My scientific name is Haliaeetus Tribuo.")
        print("My feathers are oiled so that when they dive for food, they do not get wet.")
        print("I stay away from volcanos and caves except when in danger.")
        print("Those are some details about me")

class Bunnimander(item):
    def __init__(self, name, position, use):
        self.name = name
        self.position = position
        self.use = use
        self.username = ""
        super().__init__(name, position, use)

    def interact(self):
        print("Cluck! I am the Bunnimander")
        if self.username == "":
            self.username = input(" What is your name: ")

        print("Hello {}, let me tell you something about me.".format(self.username))
        print("I am a mix between Bunnies and Salamanders.")
        print("My fur is multi-shaded meaning it has lots of shades of white and grey so that I can camouflage in any habitat.")
        print("Finally, my paws are grippy so I can climb like salamanders")
        print("Those are some details about me")

class Wood(item):
    def __init__(self, name, position, use):
        self.name = name
        self.position = position
        self.use = use
        self.username = ""
        super().__init__(name, position, use)