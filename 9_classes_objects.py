# classes and objects demo

class robot:
    def __init__(self, name, color, weight):
        # constructor
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(name, color, weight):
        print("My name is " +  name + ", I'm in color " + color + ", and I am " + weight  + "Kgs")

r1 = robot.introduce_self("Jerry", "Green", str(40))

class person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = bool

    def introduce(name, personality):
        print("Hi, my name is " + name + ", I am " + personality)

    def sit_down():
        is_sitting = True
        print("I am now seated") 
    
    def stand_up():
        is_sitting = False
        print("I am now standing")

p1 = person.introduce("Hayley", "talkative")
p2 = person.stand_up()
