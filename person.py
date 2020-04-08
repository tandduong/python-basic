class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name}")


person = Person("Tan")
person.talk()