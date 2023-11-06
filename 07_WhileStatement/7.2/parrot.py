prompt = "\nEnter anything and enter 'quit' to kill program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
