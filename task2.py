def what_a_number():
    inp = input('Введите число: ')
    try:
        num = float(inp)
    except ValueError:
        print('Вы ввели не число')
    else:
        if num.is_integer():
            print('Вы ввели целое число')
        else:
            print('Вы ввели дробное число')
            inp = inp.split('.')
            if inp[0] == inp[1]:
                return True
            else:
                return False


if __name__ == '__main__':
    print(what_a_number())
