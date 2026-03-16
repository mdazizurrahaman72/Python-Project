Username = "Azizur"
Password = 1234

key = True
max_attempts = 3

print(f"Attempts left = {max_attempts}")

while key:
    name = input("Enter Username : ").capitalize()
    pwd = int(input("Enter Password (4 digit) : "))
        
    if name == Username and Password == pwd:
        print("✅ Login successful! Welcome,", Username)
        break
    else:
        max_attempts -= 1
        print(f"❌ Incorrect username or password. Attempts left: {max_attempts}")

    if max_attempts == 0:
        print("🚫 Account locked due to too many failed attempts.")
        key = False