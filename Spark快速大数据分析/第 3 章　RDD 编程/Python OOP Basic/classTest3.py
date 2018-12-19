class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def getFullName(self):
        print(self.first + " " + self.last)
    
    def getInitials(self):
        print(self.first[0]+"."+self.last[0])

    def likes(self, thingy):
        print(self.first + " " + self.last + " likes " + thingy)
    
    def isSenior(self):
        if self.age >= 45:
            print(self.first + " is Senior")
        else:
            print(self.first + " is Junior")
    
    def happyBirthday(self):
        print("Happy Birthday " + self.first)
        self.age = self.age + 1
        print("Now you are  " + str(self.age))
    
    def say_hi(self):
        print("Hello World.")

user1 = User("joey", "jiao", 70)
user2 = User("aria", "yang", 20)
user1.getFullName()
user2.getFullName()
user1.getInitials()
user2.getInitials()
user1.likes("Movies")
user2.likes("Food")
user1.isSenior()
user2.isSenior()
user2.happyBirthday()
user2.say_hi()