# -*- coding: utf-8 -*-
"""ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.

    :param text: string
    :return: string
    """
    result = ""
    for element in text:
        if element.isdigit():
            result += element
        else:
            result += ""
    if len(result) > 11:
        return "Too many numbers!"
    elif len(result) < 11:
        return "Not enough numbers!"
    else:
        return result


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    last_result = find_id_code(text)
    first_result = 0
    weights = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    if last_result == "Too many numbers!" or last_result == "Not enough numbers!":
        return "Incorrect ID code!"
    else:
        for digit in range(len(weights)):
            weights_digit = weights[digit]
            code_digit = int(last_result[digit])
            first_result += weights_digit * code_digit
        first_control_number = first_result % 11

        if first_control_number < 10 and first_control_number == int(last_result[10]):
            return last_result
        if first_control_number < 10 and first_control_number != int(last_result[10]):
            return "Incorrect ID code!"
        elif first_control_number >= 10:
            return "Needs the second algorithm!"


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number:
    :return:
    """
    if 0 < gender_number <= 6:
        return True
    else:
        return False


def get_gender(gender_number: int) -> str:
    """
    Give a gender based on gender number in ID code.

    :param gender_number:
    :return:
    """
    gender = {"male": [1, 3, 5], "female": [2, 4, 6]}
    for key, value in gender.items():
        if gender_number in value:
            return key


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if year_number == 00:
        return True
    if 0 < year_number <= 99:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if 1 <= month_number <= 12:
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if 1 <= birth_number <= 999:
        return True
    return False


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    pre_check = is_valid_birth_number(birth_number)
    if pre_check is False:
        return "Wrong input!"

    birth_place_dict = {
        tuple(range(1, 11)): "Kuressaare",
        tuple(range(11, 21)): "Tartu",
        tuple(range(21, 221)): "Tallinn",
        tuple(range(221, 271)): "Kohtla-Järve",
        tuple(range(271, 371)): "Tartu",
        tuple(range(371, 421)): "Narva",
        tuple(range(421, 471)): "Pärnu",
        tuple(range(471, 711)): "Tallinn",
        tuple(range(711, 1000)): "undefined"
    }
    for key, value in birth_place_dict.items():
        for digit in key:
            if birth_number == digit:
                return value


def is_leap_year(year_number: int) -> bool:
    """
    Check if year is leap year.

    :param year_number:
    :return:
    """
    if (year_number % 4) == 0:
        if (year_number % 100) == 0:
            if (year_number % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    full_year_result = ""
    if 1 <= gender_number <= 6 and 0 <= year_number <= 99:
        if 1 <= gender_number <= 2:
            full_year_result += str("18") + str(year_number).zfill(2)
            return int(full_year_result)
        elif 3 <= gender_number <= 4:
            full_year_result += str("19") + str(year_number).zfill(2)
            return int(full_year_result)
        elif 5 <= gender_number <= 6:
            full_year_result += str("20") + str(year_number).zfill(2)
            return int(full_year_result)
        else:
            return int("Wrong input!")


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    mid_result = the_first_control_number_algorithm(id_code)
    if mid_result == "Incorrect ID code!":
        return False

    first_result = 0
    second_result = 0
    weights = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    weights2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)

    for digit in range(len(weights)):
        weights_digit = weights[digit]
        code_digit = int(id_code[digit])
        first_result += weights_digit * code_digit
    first_control_number = first_result % 11
    if first_control_number >= 10:
        for digit2 in range(len(weights2)):
            weights_digit_2 = weights2[digit2]
            code_digit2 = int(id_code[digit2])
            second_result += weights_digit_2 * code_digit2
            second_control_number = second_result % 11
            while str(second_control_number) == 10 and str(second_control_number) == id_code[10]:
                return True
    if str(first_control_number) == id_code[10]:
        return True
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    calendar = {"January": [1, 31], "February": [2, 28], "March": [3, 31], "April": [4, 30], "May": [5, 31],
                "June": [6, 30], "July": [7, 31], "August": [8, 31], "September": [9, 30], "October": [10, 31],
                "November": [11, 30], "December": [12, 31]
                }

    if month_number == 2 and day_number == 29:
        full_year = get_full_year(gender_number, year_number)
        leap_year = is_leap_year(full_year)
        if leap_year:
            calendar["February"] = [2, 29]

    for key, value in calendar.items():
        if month_number == value[0]:
            if day_number <= value[1]:
                return True
            else:
                return False


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    if len(find_id_code(id_code)) != 11:
        return False
    gender_number = int(id_code[0])
    year_number = int(id_code[1:3])
    month_number = int(id_code[3:5])
    day_number = int(id_code[5:7])
    birth_number = int(id_code[7:10])
    if is_valid_gender_number(gender_number) and is_valid_year_number(year_number) and \
            is_valid_month_number(month_number) and is_valid_birth_number(birth_number) and \
            is_valid_day_number(gender_number, year_number, month_number,
                                day_number) and is_valid_control_number(id_code):

        return True
    else:
        return False


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    year_number = int(id_code[1:3])
    birth_number = int(id_code[7:10])
    gender_number = int(id_code[0])
    # full_year = get_full_year(gender_number, year_number)
    if is_id_valid(id_code):
        return ("This is a " + str(get_gender(gender_number)) + " born on " + (id_code[5:7]) + "."
                + (id_code[3:5]) + "." + str(get_full_year(gender_number, year_number)) + " in "
                + str(get_birth_place(birth_number))) + "."
    else:
        return "Given invalid ID code!"


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("123456789123456789"))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("ID code is: 49403136526"))  # -> "49403136526"
    print(the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"
    print(the_first_control_number_algorithm("50412057633"))  # -> "50412057633"
    print(the_first_control_number_algorithm("Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> "Needs
    # the second algorithm!"
    print(the_first_control_number_algorithm("51809170123"))  # -> 51809170123 - Needs the second algo.
    print(the_first_control_number_algorithm("60109200186"))  # -> 60109200186

    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true
    print(is_valid_year_number(00))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6
    print(is_valid_control_number("38910164717"))  # -> True
    print(is_valid_control_number("51809170123"))  # -> True
    print(is_valid_control_number("60109200186"))  # -> ...

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    print(is_id_valid("38910164717"))  # -> True
    print(is_id_valid("51809170123"))  # -> ...
    print(is_id_valid("60109200186"))  # -> ...

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
