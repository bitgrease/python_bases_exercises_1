class Dog:
    species = "Canis Familiaris"

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}."


class GoldenRetriever(Dog):

    def speak(self, sound="Bark"):
        return super().speak(sound)

gr = GoldenRetriever(13, "Dave")

print(gr)
print(gr.speak())