class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"name: {self.name}, type: {self.type}")


my_restaurant = Restaurant('balabala',
                           'chinese food')

my_restaurant.describe_restaurant()
