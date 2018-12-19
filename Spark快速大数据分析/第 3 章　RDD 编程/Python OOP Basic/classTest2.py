#_name
#__name
##__name__

# __init__ is the self defined methods by python, normally it has special purpose
# __init__ is to initialize the instance of a class
# __main__ is to show the start poin of a program.
# nomally it is for override

class Person:
    def __init__(self):
        self._name = "Joey" # this is just a conversion for private member, just a convension
        self.name = "Aria" # normal
        self.__name = "Jria" # name mangling, for when differet class has same name, so we can indentify nane add a class name as a namespace
        self.__lol = "HAHAHAHAHA"

person1 = Person()
print(person1.name)
print(person1._name)
#print(dir(person1))
print(person1._Person__name)
print(person1._Person__lol)