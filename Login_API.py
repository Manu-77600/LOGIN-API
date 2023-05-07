class User:
    user_data = []
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def register(cls, username, password):
        user_data = cls(username, password)
        cls.user_data.append(user_data)
        return user_data
    
    @classmethod
    def login(cls, username, password):
        for user_data in cls.user_data:
            if user_data.username == username and user_data.password == password:
                return True
        return False

user1 = User.register("johndoe", "password123")
user2 = User.register("janedoe", "password456")

print(User.login("johndoe", "password123"))  
print(User.login("janedoe", "wrongpassword"))  
