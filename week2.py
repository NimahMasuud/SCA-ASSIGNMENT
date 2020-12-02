# create the class
class Myclass:

    def MyFunc(self):
        return "Hey my name is Nimah!"

# create an object from the class
a = Myclass()

#object
print(a.MyFunc())

class Person:
    def __init__(self, id, username):
        self.id = id
        self.username = username


    def speak(self):
        print(self.id)
        print(self.username)

p1 = Person(12, "Nimah")
p1.speak()

