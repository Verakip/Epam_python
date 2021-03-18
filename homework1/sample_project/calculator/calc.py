def check_power_of_2(a: int) -> bool:
    if type(a) in [float, str]:
        print('Введите целое число')
        return False
    elif a < 0:
        print('Введите положительное число')
        return False
    else:
        sq_a = int(a**0.5)
        new_a = sq_a ** 2
        return a == new_a

    #not (bool(a & (a - 1)))



