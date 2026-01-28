def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def main() :
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")
    choice = input("Choose an operation (1/2/3): ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The result is: {subtract(num1, num2)}") 
    elif choice == '3':
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid choice. Please select a valid operation.")
    
if __name__ == "__main__":
    main()