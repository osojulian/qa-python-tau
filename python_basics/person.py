import random


class Person:
    #First Method allow us to create objects of the Person class with specific attributes
    def __init__(self, name, age, health, status):
        """Initialize a Person object with name, age, health, and status."""
        self.name = name
        self.age = age
        self.health = health
        self.status = status

    def introduce(self):
        """All people introduce themselves with their name and age"""
        print(f"Hello, my name is {self.name} and I am {self.age} years old ")

    def emote(self):
        emotion = random.randrange(1, 3)

        if emotion == 1:
            print(f"{self.name} is happy today")
        elif emotion == 2:
            print(f"{self.name} is sad right now")

    def status_change(self):
        if self.health == 100:
            print(f"{self.name} is totally healthy")
        elif self.health >=77:
            print(f"{self.name} is feeling a bit under the weather")
        elif self.health >= 50:
            print(f"{self.name} feels unwell")
        elif self.health <=50:
            print(f"{self.name} goes to the doctor")
        else:
            print(f"{self.name} is in critical condition and needs immediate medical attention")

Maria = Person('Maria', 32, 90, status=True)
Rey = Person('Rey', 28, 70, status=False)
Leo = Person('Leo', 45, 44, status=True)


print(f'{Maria.name} is my friend? {Maria.status}')
print(f'{Rey.name} is my friend? {Rey.status}')


Maria.introduce()
Rey.introduce()
Leo.introduce()


Maria.status_change()
Rey.status_change()
Leo.status_change()


class Enemy(Person):
    def __init__(self, weapon, name, age, health, status):
        super().__init__(name, age, health, status)
        self.weapon = weapon


    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print(f'{other.name} you are tired and weak')

    def steal(self, other):
        print(f'ha ha ha, {other.name} I have your stuff')
        if other.status == True:
            other.status = False

Alex = Enemy('rock', 'Alex', 30, 100, status=False)

Alex.hurt(Maria)
Alex.insult(Leo)
Alex.steal(Rey)

#Rey.steal(Alex)  # This line will raise an AttributeError since 'steal' is not defined for Person class