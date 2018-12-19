class User:

    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender
    
    # this is like the toString() method of C#
    def __repr__(self):
        return self.name + " " + self.gender + " " + self.email

joey = User("Joey", "412371201@163.com", "Male")
print(joey)
aria = User("Aria", "aria@pretty.com", "Female")
print(str(aria))
