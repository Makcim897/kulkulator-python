def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "ПЛЮНЬ БЯКУ!!!"
def square( user_choice, num3, num4):
    if user_choice == '1':
        return num3*num4/2
    elif user_choice == '2':
         return num3*num4
    elif user_choice == '3':
         return num3*num4