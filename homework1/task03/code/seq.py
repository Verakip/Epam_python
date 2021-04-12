
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    mi = 10000000
    ma = -10000000
    with open(file_name) as fi:
        for line in fi:
            if int(line) < mi:
                mi = int(line)
            elif int(line) > ma:
                ma = int(line)
    return(mi, ma)
