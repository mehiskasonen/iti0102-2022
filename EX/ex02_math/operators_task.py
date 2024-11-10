"""Operators."""


def add(x, y) -> int:
    """Add x to y."""
    return x + y


def sub(x, y) -> int:
    """Subtract y from x"""
    return x - y


def multiply(x, y) -> int:
    """Multiply x by y."""
    return x * y


def div(x, y) -> float:
    """Divide x by y."""
    return x / y


def modulus(x, y) -> int:
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y


def floor_div(x, y) -> int:
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return x // y


def exponent(x, y) -> int:
    """Calculate x where y is an exponent."""
    return x ** y


def first_greater_or_equal(x, y) -> bool:
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        return True
    else:
        return False


def second_less_or_equal(x, y) -> bool:
    """If y is less or equal then return True. If not then return False."""
    if y <= x:
        return True
    else:
        return False


def x_is_y(x, y) -> bool:
    """If x same as y then return True. If not then return False."""
    if x is y:
        return True
    else:
        return False


def x_is_not_y(x, y) -> bool:
    """If x is not same as y then return True. If not then return False."""
    if x is not y:
        return True
    else:
        return False


def if_else(a, b, c, d) -> float:
    """Create a program that has 4 numeric parameters. Multiply parameters 1-2 (multiply a by b)..."""
    mult = a * b
    div = c / d
    if mult > div:
        return mult
    if div > mult:
        return div
    else:
        return 0


def surface(a: int, b: int):
    """Add the missing parameters to calculate the surface. Calculate and return the value of surface."""
    return a * b


def volume(a: int(1), b: int(1), c: int(1)):
    """Add the missing parameters to calculate the volume. Calculate and return the value of volume."""
    return a * b * c


def clock(days: int, hours: int, minutes: int, seconds: int):
    """Convert days, hours, minutes and seconds into total amount of minutes."""
    minutes_in_time = (days * 1440) + (hours * 60) + minutes + (seconds / 60)
    return minutes_in_time


def calculate(operation: int, operand_a: int, operand_b: int):
    """Add an operation to be performed on two operands."""
    if operation == 0:
        return operand_a + operand_b
    if operation == 1:
        return operand_a - operand_b
    if operation == 2:
        return operand_a * operand_b
    elif operation == 3:
        return operand_a / operand_b


if __name__ == '__main__':
    print(add(1, -2))  # -1
    print(sub(5, 5))  # 0
    print(multiply(5, 5))  # 25
    print(div(15, 5))  # 3
    print(modulus(9, 3))  # 0
    print(floor_div(3, 2))  # 1
    print(exponent(5, 5))  # 3125
    print(first_greater_or_equal(1, 2))  # False
    print(second_less_or_equal(5, 5))  # True
    print(x_is_y(1, 2))  # False
    print(x_is_not_y(1, 2))  # True
    print(if_else(1, 3, 5, 99))  # 3
    print(if_else(2, 1, 10, 5))  # 0
    print(surface(1, 2))  # 2
    print(volume(5, 5, 5))  # 125
    print(clock(0, 0, 1, 15))  # 1.25
    print(clock(0, 1, 5, 0))  # 65
    print(calculate(1, 5, 2))
