## this file will hold the class for the user
## each user will have a:
##                      username
##                      password
##                      favorite stock list

class user:
    fav_list = []
    def __init__(self):
        self.password = 0
        self.username = 0
        self.fav_list = []
        print("User started")

    def username():
        print("Enter your username:")
        username = input()
        print("Username set")

    def password():
        print("Enter password:")
        password = input()
        print("Password set")

    def fav_stocks():
        print("Enter stock to add to favorites list:")
        user.fav_list.append(input())
        print("Stock "+ fav_list[-1]+" was added to you list!")

pedro = user
pedro.password()


