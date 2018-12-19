class User:

    # class variable
    # it is like a static 
    active_users = 0

    # class method
    @classmethod
    def display_active_method(cls):
        print(cls)
        print(cls.active_users)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def logout(self):
        User.active_users -= 1
        print(self.first + " has logged out.")

user1 = User("Joey", "Jiao", 30)
user2 = User("Aria", "Yang", 20)
User.display_active_method()
user2.logout()
User.display_active_method()