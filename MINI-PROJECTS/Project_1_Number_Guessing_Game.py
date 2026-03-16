import random

secret = random.randint(1,100)
max_attempts = 7
attempts = 0
key = True
print(f"You Can attempts {max_attempts} times")

while key:
    choice = int(input("Enter a Guessing number in (1-100) : "))

    if choice == secret:
        print("Correct! 🎉")
        break
    elif choice<secret:
        print("Too low!")
        attempts+=1
        print(f"You Can attempts {max_attempts-attempts} times")
    elif choice>secret:
        print("Too high!")
        attempts+=1
        print(f"You Can attempts {max_attempts-attempts} times")

    if attempts == max_attempts and choice != secret:
         print("Sorry, you lost. The number was:", secret)
         key = False