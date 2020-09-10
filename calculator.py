while True:
    print('To calculating press any key, to stop enter "stop"')
    answer = input()
    if answer == 'stop':
        break
    else:
        print('Enter number1, option ("+", "-", "*" or "/") and number2')
        number1 = float(input())
        option = input()
        number2 = float(input())
        if option == '+':
            print(number1 + number2)
        elif option == '-':
            print(number1 - number2)
        elif option == '*':
            print(number1 + number2)
        elif option == '/' and number2 != 0:
            print(number1 / number2)
        elif option == '/' and number2 == 0:
            print('Devision by zero!')
        else:
            print('Input error')
