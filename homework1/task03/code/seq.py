
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        mi = int(fi.readline())
        ma = int(fi.readline())
        for line in fi:
            if int(line) <= mi:
                mi = int(line)
            elif int(line) >= ma:
                ma = int(line)
    return(mi, ma)
