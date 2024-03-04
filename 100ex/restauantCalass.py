class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"This is {self.name} is a {self.cuisine} type")


rest = Restaurant("Eli", "italian")

rest.describe()


class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.logins = 0

    def describe(self):
        print(f"This is {self.first_name.capitalize()} {self.last_name.capitalize()} and he is {self.age}")

    def increment_loging_attempts(self):
        self.logins += 1
        return self.logins

    def reset_loging_attempts(self):
        self.logins = 0


user1 = User("oscar", "alvarez", 30)
user1.describe()

print(user1.logins)
user1.increment_loging_attempts()
user1.increment_loging_attempts()
print(user1.logins)
