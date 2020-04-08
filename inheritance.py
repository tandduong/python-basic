class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    #pass #use this method if there is an empty class
    def bark(self):
        print("bark")


class Cat(Mammal):
    #pass  # use this method if there is an empty class
    def meow(self):
        print("Meow")


dog = Dog()
dog.bark()
dog.walk()

cat = Cat()
cat.meow()
cat.walk()