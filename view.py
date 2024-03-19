def get_user_input1():
    operator = input("Введите операцию (+, -, *, /,**): ")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    return num1, operator, num2

def get_user_input2():
    user_choise = input("Выберите фигуру (triangle-1, square-2, rectangle-3): ")
    num3 = float(input("Введите первое число: "))
    num4 = float(input("Введите второе число: "))
    return user_choise, num3, num4

def display_result(result):
    print(f"Результат: {result}")