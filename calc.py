'''
Calcultor v. 19.2.1
'''


def calc_me(x, y, oper):
    """
    калькулятор выполняет операции с числами,
    но не проверяет, что получил на вход
    """
    if oper == '*':
        return x * y
    elif oper == '/':
        # если делитель == 0 то возвращаем ошибку
        if y == 0:
            raise ZeroDivisionError("ERROR: division by zero!")
        else:
            return x / y
    elif oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    else:
        raise ValueError("ERROR: Unknown operation")


def input_number():
    num = input("Введите число: ")
    # просто попробуй
    try:
        # преобразовать переменную num в флоат
        num = float(num)
    # если вышла ошибка
    except ValueError:
        # объясняем пользователю ошибку
        print(num+" не число")
        # и снова вызываем функцию ввода числа
        num = input_number()
        # тогда получится бесконечный цикл,
        # и пока пользователь не введет число
        # программа будет его "донимать"
    return num


def input_oper():
    # задаем список допустимых операций
    oper_list = ["*", "/", "+", "-"]
    # введеную информацию записывем в переменную oper
    oper = input("Операция: ")
    # если содержимое переменной не в списке допустимых операций
    if oper not in oper_list:
        # объясняем пользователю ошибку
        print("Недопустимая операция")
        print("Поддерживаемые операции:", ", ".join(oper_list))
        # и снова вызываем функцию ввода оперции
        oper = input_oper()
    return oper


def body():
    # результат работы функции input_number запишется в переменную number1
    number1 = input_number()
    # результат работы функции input_oper запишется в переменную oper
    oper = input_oper()
    # результат работы функции input_number запишется в переменную number2
    number2 = input_number()
    # вызываем функцию calc_me с переменными которые мы ранее получили
    # результат запишем в переменную result
    result = calc_me(number1, number2, oper)
    # выводим результат для пользователя
    print("ИТОГ", result)


if __name__ == '__main__':
    # это специальное служебное условие Питон
    # оно говорит, что если мы вызвали этот файл в консоли
    # то надо выполнить функцию body
    body()
