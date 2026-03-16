"""Exception handling example for safe division operations."""
##Task1- Safe division function with exception handling for invalid inputs and division by zero
def calculate_division(numerator, denominator):
    """Calculate division with input validation and exception handling.

    Args:
        numerator (int|float): The number to divide.
        denominator (int|float): The number to divide by.

    Returns:
        float|None: Result of numerator / denominator if valid, else None.
    """
    try:
        if not isinstance(denominator, (int, float)):
            raise TypeError("Denominator must be a number.")
        elif denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        return numerator / denominator
    except TypeError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    finally:
        print("Operation completed.")

#Task2 - Bill calculator with exception handling for invalid price entries
prices= [120, 350, 'abc', 500, -200, 800]
def calculate_total(prices):
    """Calculate the total price from a list of prices, handling invalid entries."""
    total = 0
    for price in prices:
        try:
            if not isinstance(price, (int, float)):
                raise ValueError(f"Invalid price: {price}. Skipping.")
            total += price
        except ValueError as e:
            print(e)
    return total
## Task3- custom exception age validator
# file_name=input("Enter the file name to read ages from: ")
def check_age(age):
    """Check if the age is valid (between 0 and 120)."""
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number.")
    elif age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return True

## Task4- File reader with exception handling
def read_user_input_file(file_name):
    """Read user input from a file and handle exceptions."""
    try:
        with open(file_name, 'r') as file:
            data = [next(file) for _ in range(3)]  # Read first 5 lines
            print("File content:")
            print(data)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError as e:
        print(f"IO error occurred: {e}")
    finally:
        print("File reading operation completed.")

##Task5- safe shopping cart total calculator with exception handling for invalid price entries
def calculate_shopping_cart_total(items):
    """Calculate the total cost of items in a shopping cart, handling invalid entries."""
    total = 0
    for item in items:
        try:
            if not isinstance(item, (int, float)):
                raise ValueError(f"Invalid item price: {item}. Skipping.")
            total += item
        except ValueError as e:
            print(e)
    return total

if __name__ == "__main__":
    print("Valid Input:", calculate_division(10, 2))
    print("Zero Denominator:", calculate_division(10, 0))
    print("Invalid Input:", calculate_division(10, 'a'))
    print("\nCalculating Total Price:")
    total_price = calculate_total(prices)
    print(f"Total Price: {total_price}")

    try:
        print("\nChecking Age:")
        check_age(25)  # Valid age
        check_age(-5)  # Invalid age
    except (TypeError, ValueError) as e:
        print(f"Age validation error: {e}") 

    input_file_name=input("\nEnter the file name to read from: ")
    read_user_input_file(input_file_name)

    print("\nCalculating Shopping Cart Total:")
    ## run the loop to get user input prices until user enters 'q'  
    shopping_cart_items = []
    while True:        
        user_input = input("Enter item price (or 'q' to quit): ")
        if user_input == 'q':
            break
        try:
            price = float(user_input)
            shopping_cart_items.append(price)
        except ValueError:
            print("Invalid input. Please enter a valid price or 'q' to quit.")

    total_cart_cost = calculate_shopping_cart_total(shopping_cart_items)
    print(f"Total Shopping Cart Cost: {total_cart_cost}")   