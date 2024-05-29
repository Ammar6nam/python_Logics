username = input("What is your username? ")
password = input(f"Type the password for user: {username}: ")
valid = {"username": "admin", "password": "admin"}

d1={'username':username,'password':password}
print(d1)


if valid==d1:
    print(f'Welcome, {username}')
else:
    print('Credentials are invalid')