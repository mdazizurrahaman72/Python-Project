scores = (85,90,78,92,88)
keep_running =True

def show_scores():
    print("\nStudent Scores:", scores)

def menu():
    print("\nStudent Score Tracker")
    print("-"*40)
    print("1. Show all scores")
    print("2. Show highest score")
    print("3. Show lowest score")
    print("4. Show average score")
    print("5. Exit")


while keep_running:
    menu()
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        show_scores()
    elif choice == 2:
        print("\nHighest Score:", max(scores))
    elif choice == 3:
        print("\nLowest score:",min(scores))
    elif choice == 4:
        avg = sum(scores)/len(scores)
        print("\nAverage score:",avg)
    elif choice == 5:
        print("\nExiting program...")
        keep_running = False
    else:
        print("\nInvalid choice!")