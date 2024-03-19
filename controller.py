import view
import model


def run1():
    while True:
        num1, operator, num2 = view.get_user_input1()
        result = model.calculate(num1, num2, operator)
        view.display_result(result)

def run2():
    while True:
        user_choice, num3, num4 = view.get_user_input2()
        result = model.square(user_choice, num3, num4)
        view.display_result(result)