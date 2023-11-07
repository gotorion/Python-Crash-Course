class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"name: {self.name}, type: {self.type}")

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self):
        self.number_served = self.number_served + 1

my_restaurant = Restaurant('bal', 'Chinese Food')
print(my_restaurant.number_served)
my_restaurant.set_number_served(40)
print(my_restaurant.number_served)
my_restaurant.increment_number_served()
print(my_restaurant.number_served)
