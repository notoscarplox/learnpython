class Dog:
    "Attempt tp model a dog"

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is rolling!")


my_dog = Dog("Chon", 2)
your_dog = Dog("Elpo", 3)

print(f"name: {my_dog.name}")

my_dog.sit()
my_dog.roll_over()