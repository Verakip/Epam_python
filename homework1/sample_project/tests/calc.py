def check_power_of_2(a: int) -> bool:
    if type(a) is not int:
        return False
        raise TypeError("Ввод должен быть целым числом")
        
    elif a < 0:
        return False
        raise TypeError("Число не должно быть отрицательным")
        
    else:
        sq_a = int(a**0.5)
        new_a = sq_a ** 2
        return a == new_a





