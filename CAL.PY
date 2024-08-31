# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Main program loop
def main():
    while True:
        # Display the available operations
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Prompt the user to choose an operation
        choice = input("Choose an operation (1/2/3/4/5): ")
        
        if choice == "5":
            print("Goodbye!")
            break
        
        if choice in ["1", "2", "3", "4"]:
            # Prompt the user to enter two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the chosen operation
            if choice == "1":
                result = add(num1, num2)
                print(f"The result of adding {num1} and {num2} is: {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"The result of subtracting {num2} from {num1} is: {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"The result of multiplying {num1} and {num2} is: {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"The result of dividing {num1} by {num2} is: {result}")
        else:
            print("Invalid input. Please choose a valid operation.")

if __name__ == "__main__":
    main()
