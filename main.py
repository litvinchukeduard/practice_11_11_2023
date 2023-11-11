result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            user_input = input("Enter a number: ")
            if user_input == '=':
                print("You need to enter a number first. Please try again.")
                continue
            operand = float(user_input)
            if result is None:
                result = operand
            else:
                if operator == '+':
                    result += operand
                    operator = None
                elif operator == '-':
                    result -= operand
                    operator = None
                elif operator == '*':
                    result *= operand
                    operator = None
                elif operator == '/':
                    result /= operand
                    operator = None            
            wait_for_number = False
        else:
            user_input = input("Enter an operator (+, -, *, /) or = to get the result: ")
            if user_input in ['+', '-', '*', '/']:
                if operator is not None:
                    print(f"You entered two operators in a row. Please try again.")
                    continue
                operator = user_input
                wait_for_number = True
            elif user_input == '=':
                if result is not None:
                    print(result)
                    break
                else:
                    print("You need to enter an operator before =. Please try again.")
                    continue
            else:
                print(f"'{user_input}' is not a valid operator. Please try again.")
    except ValueError:
        print(f"'{user_input}' is not a valid number. Please try again.")