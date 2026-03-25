import math  # For advanced math functions

# ------------------- BASIC SCIENTIFIC FUNCTIONS -------------------

def square_root(n):
    if n < 0:
        return "Error: Cannot find square root of negative number"
    return math.sqrt(n)

def factorial(n):
    if n < 0:
        return "Error: Factorial of negative number doesn't exist"
    if n != int(n):
        return "Error: Factorial only works with whole numbers"
    if n > 1000:
        return "Error: Number too large"
    return math.factorial(int(n))

def logarithm():
    try:
        n = float(input("Enter number: "))
        base = input("Enter base (10 / e / custom): ")

        if n <= 0:
            return "Error: Logarithm only works for positive numbers"

        if base == '10':
            return math.log10(n)
        elif base == 'e':
            return math.log(n)
        else:
            base = float(base)
            return math.log(n, base)
    except:
        return "Error: Invalid input"

def sine(angle_degrees):
    return math.sin(math.radians(angle_degrees))

def cosine(angle_degrees):
    return math.cos(math.radians(angle_degrees))

def tangent(angle_degrees):
    if angle_degrees % 180 == 90:
        return "Error: Tangent undefined at 90 + k*180 degrees"
    return math.tan(math.radians(angle_degrees))

def power(base, exponent):
    return math.pow(base, exponent)

def exponential(x):
    return math.exp(x)

# ------------------- PERCENTAGE FUNCTIONS -------------------

def percentage(value, percent):
    return (value * percent) / 100

def percentage_change(old_value, new_value):
    if old_value == 0:
        return "Error: Cannot calculate percentage change from 0"
    return ((new_value - old_value) / old_value) * 100

# ------------------- MAIN CALCULATOR -------------------

def scientific_calculator():
    print("\n🔬 SCIENTIFIC CALCULATOR")
    print("=" * 50)

    operations = {
        '1': ('Square Root', square_root, 1),
        '2': ('Factorial', factorial, 1),
        '3': ('Logarithm', logarithm, 0),
        '4': ('Sine', sine, 1),
        '5': ('Cosine', cosine, 1),
        '6': ('Tangent', tangent, 1),
        '7': ('Power (x^y)', power, 2),
        '8': ('Exponential (e^x)', exponential, 1),
        '9': ('Percentage', percentage, 2),
        '10': ('Percentage Change', percentage_change, 2),
    }

    while True:
        print("\nOperations:")
        for key, (name, _, _) in operations.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("\nChoose operation: ")

        if choice == '0':
            print("Exiting Scientific Calculator...")
            break

        if choice in operations:
            name, func, param_count = operations[choice]

            try:
                if param_count == 0:
                    result = func()

                elif param_count == 1:
                    num = float(input(f"Enter number for {name}: "))
                    result = func(num)

                elif param_count == 2:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    result = func(num1, num2)

                if isinstance(result, float):
                    print(f"✅ Result: {round(result, 6)}")
                else:
                    print(f"✅ Result: {result}")

            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")

        else:
            print("❌ Invalid choice!")

# ------------------- RUN PROGRAM -------------------

if __name__ == "__main__":
    scientific_calculator()