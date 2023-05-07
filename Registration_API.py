class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def register(self):
        print("Registered {0.first_name} {0.last_name} with email {0.email}".format(self))

user = User("John", "Doe", "johndoe@example.com", "password123")
User.register(user)
