unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_user = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_user.append(current_user)

print("\nThe following users have been confirmed: ")
for user in confirmed_user:
    print(user.title())
