def greet_user(username):
    """show greeter with name"""
    print(f"Hello, {username.title()}")

def greet_default(username = 'john'):
    """with default value"""
    print(f"Hello, {username.title()}")

greet_default('luke')
greet_default()