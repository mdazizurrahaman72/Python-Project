def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multipl(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Errpr: Cannot divide by zero!"
    return a/b

def modulus(a,b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b

def power(a,b):
    return a**b

def display_menu():
    print("\n"+"-"*40)
    print("📱 BASIC CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. History")
    print("8. Exit")
    print("-"*40)
 
def get_number():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1,num2

def basic_calculator():
    print("Welcome to Basic Calculator!")
    history = []

    while True:
        display_menu()
        choice = int(input("Choose operation (1-7): "))

        if choice in [1,2,3,4,5,6]:
            num1,num2 = get_number()

            if num1 is None or num2 is None:
                continue

            if choice == 1:
                result = add(num1,num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == 2:
                result = subtract(num1,num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == 3:
                result = multipl(num1,num2)
                operation = f"{num1} X {num2} = {result}"
            elif choice == 4:
                result = divide(num1,num2)
                operation = f"{num1} / {num2} = {result}"
            elif choice == 5:
                result = divide(num1,num2)
                operation = f"{num1} % {num2} = {result}"
            elif choice == 6:
                result = divide(num1,num2)
                operation = f"{num1} ^ {num2} = {result}"
            
            print(f"\nResult: {operation}")
            history.append(operation)
        elif choice == 7:
            if len(history) == 0:
                print(" No calculations yet!")
            else:
                print("\n📊 Calculation History:")
                for cal in history:
                    print(f" {cal}")
        elif choice == 8:
            print("\nThank you for using Calculator! 👋")
            break
        else:
            print("❌ Invalid choice! Please select 1-8")

basic_calculator()