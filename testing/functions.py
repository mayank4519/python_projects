from typing import Union

def divide(dividend: Union[int, float], divisor: Union[int, float]):
    return  dividend / divisor

def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError("At least one argument required!")
    total = 1
    for arg in args:
        total *= arg
    return total
