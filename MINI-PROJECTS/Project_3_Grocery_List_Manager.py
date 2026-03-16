def view_items(grocery_list):
    if len(grocery_list)==0:
        print("\n❌ Your grocery list is empty!")
    else:
        print("\n📋 Your Grocery List:")
        print("-" * 20)
        for index , item in enumerate(grocery_list):
            print(f"{index+1} : {item}")

def add_item(grocery_list):
    new_item = input("\nEnter item to add : ").lower()
    
    if new_item in grocery_list:
        print(f"⚠️  '{new_item}' is already in your list!")
    else:
        grocery_list.append(new_item)
        print(f"✅ '{new_item}' added to your list!")

def remove_item(grocery_list):

    if len(grocery_list) == 0:
        print("\n❌ List is empty! Nothing to remove.")
    else:
        print("\nCurrent items:")
        print("-" * 20)
        for index , item in enumerate(grocery_list):
            print(f"{index+1} : {item}")

    item_to_remove = input("\nEnter item name to remove: ").lower()

    if item_to_remove not in grocery_list:
        print(f"❌ '{item_to_remove}' not found in list!")
    else:
        grocery_list.remove(item_to_remove)
        print(f"✅ '{item_to_remove}' removed from list!")

def chack_item(grocery_list):
    item_to_check = input("\nEnter item to search: ")

    if item_to_check in grocery_list:
        position = grocery_list.index(item_to_check)
        print(f"✅ '{item_to_check}' is in your list at position {position + 1}")
    else:
        print(f"❌ '{item_to_check}' is not in your list")

def clear_list(grocery_list):
    if len(grocery_list) ==0 :
        print("\n❌ Your grocery list is alrady empty!")
    else:
        confirm = input("\n⚠️  Are you sure you want to clear the entire list? (yes/no): ")
        if confirm.lower() == "yes":
            grocery_list.clear() 
            print("✅ List cleared!")
        else:
            print("❌ Clear cancelled")

def sort_list(grocery_list):
    if len(grocery_list) ==0 :
        print("\n❌ Your grocery list is empty!")
    else:
        grocery_list.sort()
        print("\n✅ List sorted alphabetically!")
        print("\nSorted list:")
        print("-"*20)
        for item in grocery_list:
            print(f"  • {item}")


def grocery_list_manager(grocery_list):
    keep_running = True 

    while keep_running:
        print("\n"+"-"*40)
        print("🛒 GROCERY LIST MANAGER")
        print("="*40)
        print(f"\nCurrent items in list: {len(grocery_list)}")
        print("\n1. View all items")
        print("2. Add new item")
        print("3. Remove item")
        print("4. Check if item exists")
        print("5. Clear entire list")
        print("6. Sort list alphabetically")
        print("7. Exit")

        choice = int(input("\nEnter your choice (1-7) : "))

        if choice == 1:
            view_items(grocery_list)
        elif choice == 2:
            add_item(grocery_list)
        elif choice == 3:
            remove_item(grocery_list)
        elif choice == 4:
            chack_item(grocery_list)
        elif choice == 5:
            clear_list(grocery_list)
        elif choice == 6:
            sort_list(grocery_list)
        elif choice == 7:
            print("\n👋 Thank you for using Grocery List Manager!")
            print(f"Final list has {len(grocery_list)} items")
            keep_running = False
        else:
            print("\n❌ Invalid choice! Please enter 1-7")


grocery_list = ["milk","bread","eggs","biscut","water"]
grocery_list_manager(grocery_list)