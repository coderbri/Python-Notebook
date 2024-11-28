# * Setting the Class Blueprint
# PascalCase is used when naming classes.
class User:
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0          # default value
        self.following = 0          # default value

    # * Defining a Method
    #       the user, and the user being followed
    def follow(self, user):
        user.followers += 1
        self.following += 1
        print(f"You are now following @{user.username}.")


# * Instantiating the Object
# snake_case is used when naming objects.
user_1 = User("001", "janedoe")
user_2 = User("002", "johnsmith")
print(user_1.username)

# * Defining Attributes (w/o a Constructor)
# user_2 = User()
# user_2.id = "002"
# user_2.username = "johnsmith"

# * Using Methods
user_1.follow(user_2)
user_2.follow(user_1)
