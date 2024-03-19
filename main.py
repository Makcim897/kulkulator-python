import controller
while True:
    choice = int(input('Введите 1 для простого калькулятора, введите 2 для калькулятора площадей'))
    if choice == 1:
        calculator = controller.run1()
        calculator.run()
    elif choice == 2:
        calculator_SQ = controller.run2()
        calculator_SQ.run()
