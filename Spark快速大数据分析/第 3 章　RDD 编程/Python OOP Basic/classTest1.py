class User:
    def __init__(self, name, email):
        #print("Init is called.")
        #self keyword refers to the specific instance of the User class or whatever class we are working with.
        #self is the curent instance of the object, since the Class is User, self id the current instance of User.
        #self must be the first parameter to __init__ and any other methods and properties on class instances.
        
        self.name = name
        self.email = email
    
    def getName(self):
        print(self.name)
    
    def toString(self):
        print(self.name + " " + self.email)

