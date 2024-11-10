"""Solutions for students_study, lottery and fruit_order."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if 18 <= time <= 24 and coffee_needed is False:
        return True
    if 18 <= time <= 24 and coffee_needed is True:
        return True
    if 5 <= time <= 17 and coffee_needed is True:
        return True
    if 5 <= time <= 17 and coffee_needed is False:
        return False
    if 1 <= time <= 4:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """Return Lottery victory result 10, 5, 1, or 0 according to input values."""
    if a == 5 and b == 5 and c == 5:
        return 10
    if a == b == c and a != 5:
        return 5
    if a != b and a != c:
        return 1
    if c != b and a == b or a == c:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """Return number of small fruit baskets if it's possible to finish the order, otherwise return -1."""
    if small_baskets < 0:
        return False
    if big_baskets < 0:
        return False
    if ordered_amount < 0:
        return False
    big_basket_kg = big_baskets * 5

    if small_baskets + big_basket_kg == ordered_amount:
        return small_baskets
    if small_baskets + big_basket_kg < ordered_amount:
        return -1

    while big_baskets * 5 > ordered_amount:
        big_baskets -= 1

    while small_baskets + (big_baskets * 5) != ordered_amount:
        small_baskets -= 1
    return small_baskets


if __name__ == '__main__':
    print(students_study(24, True))
    print(students_study(23, True))
    print(students_study(22, True))
    print(students_study(21, True))
    print(students_study(20, True))
    print(students_study(19, True))
    print(students_study(18, True))
    print(students_study(17, True))
    print(students_study(16, True))
    print(students_study(15, True))
    print(students_study(14, True))
    print(students_study(13, True))
    print(students_study(12, True))
    print(students_study(11, True))
    print(students_study(10, True))
    print(students_study(9, True))
    print(students_study(8, True))
    print(students_study(7, True))
    print(students_study(6, True))
    print(students_study(5, True))
    print(students_study(4, True))
    print(students_study(3, True))
    print(students_study(2, True))
    print(students_study(1, True))
    print(students_study(19, False))
    print(students_study(11, True))
    print(students_study(11, False))
    print(students_study(10, True))
    print(students_study(10, False))
    print(students_study(9, True))
    print(students_study(9, False))
    print(students_study(8, True))
    print(students_study(8, False))
    print(students_study(7, True))
    print(students_study(7, False))
    print(students_study(6, True))
    print(students_study(6, False))
    print(students_study(5, True))
    print(students_study(5, False))
    print(students_study(1, True))
    print(students_study(25, True))
    print(lottery(5, 5, 5))   # -> 10
    print(lottery(2, 2, 1))   # -> 0
    print(lottery(2, 3, 1))   # -> 1
    print(fruit_order(4, 1, 9))   # -> 4
    print(fruit_order(3, 1, 10))   # -> -1
    print(fruit_order(2, 0, 1))
