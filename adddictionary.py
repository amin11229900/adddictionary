users = []

# Load existing users from file
try:
    with open("users.txt", "r") as f:
        for line in f:
            username, password = line.strip().split(", ")
            users.append({"username": username.split(": ")[1], "password": password.split(": ")[1]})
except FileNotFoundError:
    pass

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username already exists
    for user in users:
        if user["username"] == username:
            print("Username already exists! Please choose a different username.")
            break
    else:
        # Check if the exact same username and password combination already exists
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Username and password combination already exists! Please choose a different combination.")
                break
        else:
            user = {"username": username, "password": password}
            users.append(user)
            print("User added successfully!")
            print("Current users:")
            for user in users:
                print(f"Username: {user['username']}, Password: {user['password']}")

    cont = input("Do you want to add another user? (y/n): ")
    if cont.lower()!= 'y':
        break

print("Final users list:")
for user in users:
    print(f"Username: {user['username']}, Password: {user['password']}")

# Save users to a file
with open("users.txt", "w") as f:
    for user in users:
        f.write(f"Username: {user['username']}, Password: {user['password']}\n")

print("Users saved to users.txt file!")