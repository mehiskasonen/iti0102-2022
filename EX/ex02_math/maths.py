"""Math."""


def average(a, b, c, d) -> float:
    multi = (a * 1) + (b * 2) + (c * 3) + (d * 4)
    arith_average = multi / 4
    return arith_average


def school_pressure(ects: int, weeks: int) -> float:
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours.

    If it's not possible in time then return -1.

    Examples:
    school_pressure(30, 12) == 65
    school_pressure(1, 1) == 26
    school_pressure(1, 0) == -1
    """
    if weeks <= 0:
        return -1
    effort = (ects * 26) / weeks
    if effort <= 168:
        return effort
    else:
        return -1


def add_fractions(a: int, b: int, c: int, d: int) -> str:
    """
    Implement a function that takes 4 parameters.

    Parameters a and b denote the first fraction like a/b.
    Parameters c and d denote the second fraction like c/d.

    Find and return a fraction in string format that is the sum of a/b and c/d.

    NB! the fraction does not have to be in the simplest form.
    NB! the answer should not contain any commas.

    Examples:
    add_fractions(1, 3, 1, 3) # 1/3 + 1/3 => there are many correct answers like "2/3" and "6/9"
    add_fractions(2, 5, 1, 5) # 2/5 + 1/5 => there are many correct answers like "3/5" and "15/25"
    """
    numerator = a + c
    common_denominator = b
    denominator = b * d
    if b == d:
        return str(f"{numerator}/{common_denominator}")
    if b != d:
        numerator = a * (denominator // b) + c * (denominator // d)
    return str(f"{numerator}/{denominator}")


if __name__ == '__main__':
    print(average(1, 2, 3, 4.5))
    print(school_pressure(1, 2))
    print(school_pressure(8, 1))
    print(school_pressure(9, 2))
    print(school_pressure(1, 1))  # => 26
    print(school_pressure(1, 0))  # => -1
    print(school_pressure(5, 220))
    print(add_fractions(1, 2, 1, 2))  # => 1/2 + 1/2 => Võimalikud vastused "1/1", "4/4", "2/2", jne
    print(add_fractions(3, 1, 1, 1))  # => 3/1 + 1/1 => Võimalikud vastused "4/1", "16/4", "8/2", jne
    print(add_fractions(1, 6, 3, 5))  # => 1/6 + 3/5 => Võimalikud vastused "23/30", "46/60", jne
