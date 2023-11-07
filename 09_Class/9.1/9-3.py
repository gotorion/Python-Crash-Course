class User:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f' age = {self.age}')

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")


me = User('john', 'li', '23')

me.describe_user()

me.greet_user()
