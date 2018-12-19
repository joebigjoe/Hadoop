class User:

    # class variable
    # it is like a static 
    active_users = 0

    # class method
    @classmethod
    def display_active_user(cls):
        print(cls)
        print(cls.active_users)
    
    @classmethod
    def user_from_string(cls, userString):
        first, last, age = userString.split(',')
        return cls(first, last, age)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def logout(self):
        User.active_users -= 1
        print(self.first + " has logged out.")
    
    def getFullName(self):
        print(self.first + " " + self.last)
    
    def getInitials(self):
        print(self.first[0]+"."+self.last[0])


user1 = User("Joey", "Jiao", 30)
user2 = User("Aria", "Yang", 20)
User.display_active_user()
user2.logout()
User.display_active_user()

user3 = User.user_from_string("Quentin,Tarantino,60")
user3.getFullName()
user4 = User.user_from_string("Massie,Guo,30")
user4.getInitials()
User.display_active_user()
