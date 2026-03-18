contacts = {}

contacts["Azizur"] = "01862958963"
contacts["Rahim"] = "017-1234567"
contacts["Kamal"] = "019-8888999"

print("📱 Welcome to Simple Contact Book!")
print("-"*40)

keep_running = True

while keep_running:
    print("\nWhat do you want to do?")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("\n--- All Contacts ---")

        for name in contacts:
            print(f"{name} = {contacts[name]}")

    elif choice == 2:
        print("\n--- Add New Contact ---")
        name = input("Enter name: ")
        phone_num = input("Enter Phone number: ")

        if name in contacts.keys():
            print("❌ The name is in your contacts")
        else:
            contacts[name] = phone_num
            print("The contruct is added")

    elif choice == 3:
        print("\n--- Search Contact ---")
        search_name = input("Enter name to search: ")

        phone = contacts.get(search_name,"Note found")
        print(phone)

        # if search_name in contacts.keys():
        #     print(f"{search_name} = {contacts[search_name]}")
        # else:
        #     print("❌ The name is not found in contacts")

    elif choice == 4:
        print("\n--- Delete Contact ---")
        name = input("Enter name to delete: ")

        if name in contacts.keys():
            contacts.pop(name)
            print(f"{name} is romoved")
        else:
            print("Not found")

    elif choice == 5:
        print("\n👋 Goodbye!")
        keep_running = False

    else:
        print("❌ Invalid choice! Please enter 1-5")

print("\nProgram ended.")   