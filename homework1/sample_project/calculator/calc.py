def check_power_of_2(a: int) -> bool:
    return not (bool(a & (a - 1)))

check_power_of_2(3)

2^3