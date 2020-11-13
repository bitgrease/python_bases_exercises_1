class Farm:

    pigs = []
    cows = []
    chickens = []
    horses = []

    def __init__(self, name):
        self.name = name

    def error_message(self, animal):
        print(f"That's a {type(animal)}! I can't add that here!")

    def add_horse(self, horse):
        if type(horse) is Horse:
            self.horses.append(horse)
        else:
            self.error_message(horse)

    def add_pig(self, pig):
        if type(pig) is "Pig":
            self.pigs.append(pig)
        else:
            self.error_message(pig)


    def add_chicken(self, chicken):
        if type(chicken) is "Chicken":
            self.chickens.append(chicken)
        else:
            self.error_message(chicken)

    def add_cow(self, cow):
        if type(cow) is "Cow":
            self.cows.append(cow)
        else:
            self.error_message(cow)


# TODO : Create Animal class and then create Chicken, Pig, Horse, Cow
# TODO : Add method to show various animals that iterates through the lists.