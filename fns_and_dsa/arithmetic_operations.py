def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.
    Prints and returns the result.
    """

    if operation == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = num1 / num2

    else:
        result = "Error: Invalid operation"

    # Print result for visibility
    print(f"Computed result: {result}")

    return result
