# SIMPLE CALCULATOR - TASK 2 

print("---Simple Calculator---")

#adds two numbers
def add(x, y):
    return x + y

#subtracts two numbers
def subtract(x, y):
    return x - y

#multiplies two numbers
def multiply(x, y):
    return x * y

#divides two numbers
def divide(x, y):
    return x / y

#modulus of two numbers
def mod(x,y):
    return x % y


print("Select operation.")
print("1.Add(+)")
print("2.Subtract(-)")
print("3.Multiply(*)")
print("4.Divide(/)")
print("5.Modulus(%)")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a, "-", b, "=", subtract(a, b))

        elif choice == '3':
            print(a, "*", b, "=", multiply(a, b))

        elif choice == '4':
            print(a, "/", b, "=", divide(a, b))

        elif choice == '5':
            print(a, "%", b, "=", mod(a, b))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
