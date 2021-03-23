while True:
    print('To calculating press any key, to stop enter "stop"')
    answer = input()
    if answer == 'stop':
        break
    else:
        print('Enter number1, action and number2')
        a = float(input())
        s = input()
        b = float(input())
        if s == '+':
            print(a + b)
        elif s == '-':
            print(a - b)
        elif s == '*':
            print(a + b)
        elif s == '/' and b != 0:
            print(a / b)
        elif s == '/' and b == 0:
            print('Devision by zero!')
        else:
            print('Input error')