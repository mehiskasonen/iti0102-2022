"""Exam1 (2021-03-01)."""


def split_string_into_ints(numbers: str) -> list:
    """
    Return list of integers from comma-separated string of integers.

    split_string_into_ints("1,2") => [1, 2]
    split_string_into_ints("") => []
    split_string_into_ints("0") => [0]
    split_string_into_ints("-1,-2,3") => [-1, -2, 3]
    """
    if numbers == "":
        return []
    else:
        numbers = numbers.split(",")
        numbers = [int(i) for i in numbers]
        return numbers


def sum_of_multiples(limit: int, multiplier: int) -> int:
    """
    Given a limit, find the sum of all the multiples of multiplier up to but not including that number.

    Limit and multiplier are both natural numbers.
    If limit is smaller or equal than multiplier the function should return 0.

    sum_of_multiples(20, 5) -> 30
    sum_of_multiples(10, 1) -> 45
    sum_of_multiples(5, 5) -> 0
    """
    n = 0
    for i in range(multiplier, limit, multiplier):
        n += i
    return n


def mix_string(s1: str, s2: str) -> str:
    """
    Given two strings s1 and s2, create a mixed string by alternating between str1 and str2 chars.

    mix_string("AAA", "bbb") -> "AbAbAb"
    mix_string("AA", "") -> "AA"
    mix_string("mxdsrn", "ie tig") -> "mixed string"
    """
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) > len(s2):
        for _ in range(len(s1) - len(s2)):
            s2.append("")
    if len(s2) > len(s1):
        for _ in range(len(s2) - len(s1)):
            s1.append("")
    return "".join("".join(i) for i in zip(s1, s2))


def bingo(matrix: list, numbers: list) -> tuple:
    """
    Whether the matrix has winning combinations with the given numbers.

    Check if player got any winning combinations:
    1. Corners - all 4 corners contain winning numbers
    2. Diagonals - all diagonals contain winning numbers
    3. Full game - all numbers in the matrix/ticket are in the winning numbers
    Example matrix:
    [
        [ 5,  7, 11, 15, 21],
        [22, 25, 26, 27,  9],
        [34,  2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37,  3,  6, 32],
    ]

    :param matrix: 5 x 5 bingo ticket of numbers
    :param numbers: list of winning numbers (size always at least 4)
    :return: tuple of booleans (corners, diagonals, full_game)
    """
    pass


def mirror_ends(s: str) -> str:
    """
    Return the first non-matching symbol pair from both ends.

    The function has to be recursive. No loops allowed!

    Starting from the beginning and end, find the first symbol pair which does not match.
    If the input string is a palindrome (the same in reverse) then return "" (empty string).

    mirror_ends("abc") => "ac"
    mirror_ends("aba") => ""
    mirror_ends("abca") => "bc"
    mirror_ends("abAAca") => "bc"
    mirror_ends("") => ""
    """
    pass


def prime_factorization(number: int) -> int:
    """
    Given a natural number greater than 1, return it's prime factorization.

    Return the prime factorization of number.

    Return dict, where the key is a prime factor and the value is count of this factor.

    12 = 2 * 2 * 3 => {2: 2, 3:1}
    1960 = 2 * 2 * 2 * 5 * 7 * 7 => {2: 3, 5: 1, 7: 2}
    79 = 71 * 1 => {79: 1}

    Prime number is a number which is divisible only by 1 and the number itself.
    For example 2, 3, 5, 7, 11, 13, 17, 19, 23 are prime numbers.

    Examples:
    2 => { 2: 1 }
    12 => { 2: 2, 3: 1 }
    1960 => { 2: 3, 5: 1, 7: 2 }
    1024 => { 2: 10 }
    79 => { 79: 1 }
    121 => { 11: 2 }

    :param number: a number greater than 1
    :return: dict of prime factors and their counts.
    """
    pass


class Candy:
    """Candy."""

    def __init__(self, name: str, filling: str):
        """
        Candy class constructor.

        :param name: candy name
        :param filling: candy filling
        """
        self.name = name
        self.filling = filling


class CandyShop:
    """Candy shop."""

    def __init__(self):
        """CandyShop class constructor."""
        pass

    def add_candies(self, candies: list):
        """
        Add list of fresh candies to already existing ones.

        :param candies: list of candies to add
        :return:
        """
        pass

    def get_candies(self) -> list:
        """
        Return list of all candies existing in the shop.

        :return: list of all candies
        """
        pass

    def get_candies_by_filling(self, filling: str) -> list:
        """
        Get list of candies that have the same filling as given in parameter value.

        :return: list
        """
        pass

    def sort_candies_by_filling(self) -> list:
        """
        Method should return list of candies sorted by filling in alphabetical order.

        If filling is the same, then sort
        by name in alphabetical order.

        :return: sorted list of candies
        """
        pass

    def get_most_popular_candy_name_and_filling(self) -> dict:
        """
        Find the most popular candy name and filling.

        Method should return dict with name and filling of the most popular candy in the shop (type of candy which name
        and filling is present the most in the shop). NB! You should consider the most popular combination of name and filling.
        {name: most_pop_candy_name, filling: most_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of most pop candy
        """
        pass

    def get_least_popular_candy_name_and_filling(self) -> dict:
        """
        Find the least popular candy name and filling.

        Method should return dict with name and filling of the least popular candy in the shop (type of candy which name
        and filling is present the least in the shop). NB! You should consider the least popular combination of name and filling.
        {name: least_pop_candy_name, filling: least_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of least pop candy
        """
        pass

    def collect_candies_by_filling(self) -> dict:
        """
        Group candies by filling.

        Method should return dict with candies divided by filling, where dict key is filling and dict value is list
        of candies with this filling.
        {candy_filling: [candy1, candy2]}

        :return: dict of candies divided by filling
        """
        pass


class Grade:
    """Grade."""

    def __init__(self, grade, weight: int, assignment: str, date: str):
        """Constructor."""
        self.assignment = assignment
        self.value = grade
        self.weight = weight
        self.date = date
        self.previous_grades = {}

    def change_grade(self, new_grade: int, date: str):
        """
        Change a previous grade.

        This function should save the previous grade in a dictionary previous_grades, where key is the date and value
        is the value of the grade. Value and date should be updated.
        """
        pass


class Student:
    """Student."""

    def __init__(self, name: str):
        """Constructor."""
        self.name = name
        self.grades = {}

    def grade(self, grade: Grade):
        """
        Add a grade for an assignment that a students has done.

        Grades are kept in a dictionary where assignment name is the key and Grade object is the value (All previous
        grades for the same assignment are kept in the Grade object previous grades dictionary).
        Note that this function is only used when a student does an assignment for the first time.
        """
        pass

    def redo_assignment(self, new_grade: int, assignment: str, date: str):
        """
        Update the grade for given assignment.

        This function is only used when an assignment has been attempted at least once before. Keep in mind that you
        need to also keep the history of grades, not create a new grade!
        """
        pass

    def calculate_weighted_average(self):
        """
        Calculate the weighted average of grades.

        You should take into account the weights. There are three weights: 1, 2 and 3, where 3 means that one grade of
        weight 3 is the same as three grades of weight 1.

        For example:
        if there are grades 4 with weight 3 and 3 with weight 1, then the resulting value will be
                (4 * 3 + 3 * 1) / (3 + 1) = 15 / 4 = 3.75
        which will be rounded to 4.

        Also make sure not to miss out when a grade is noted as "!". If there is no attempt to redo this, then "!"
        should be equivalent to grade "1".
        """
        pass


class Class:
    """Class."""

    def __init__(self, teacher: str, students: list):
        """Constructor."""
        self.teacher = teacher
        self.students = students

    def add_student(self, student: Student):
        """Add student to the class."""
        pass

    def add_students(self, students: list):
        """Add several students to the class."""
        pass

    def remove_student(self, student: Student):
        """Remove student from the class."""
        pass

    def get_grade_sheet(self):
        """
        Return grade sheet as a table.

        Grade sheet includes information of all the students in the class and their final grades.
        All edges should be either "|" or "-".
        First column is student's name and the second column is the final grade (weighted average).
        First, second and third row should look something like this (notice the capital letters):
        ----------------------
        | Name | Final grade |
        ----------------------

        Make sure that all the columns are correctly aligned after the longest element.
        For example, consider following rows:
        | Ago                   |  5  |
        | Some really long name |  3  |

        Rules are following:
        Each row (except for "-----" rows) starts with "|" and a space " " and ends with a space " " and "|".
        Text in "Name" column needs to be aligned to left
        Grades in "Final grade" column need to be centered

        Students in the table should follow the order which they were added to the class.

        The whole table would look something like this:
        ---------------------------------------
        | Name                  | Final grade |
        ---------------------------------------
        | Ago                   |      5      |
        | Johannes              |      4      |
        | Mari                  |      5      |
        | Some really long name |      3      |
        ---------------------------------------

        """
        pass


if __name__ == '__main__':
    assert split_string_into_ints("1,2") == [1, 2]
    assert split_string_into_ints("") == []
    assert split_string_into_ints("-1,0") == [-1, 0]

    assert sum_of_multiples(20, 5) == 30
    assert sum_of_multiples(10, 1) == 45
    assert sum_of_multiples(5, 5) == 0

    assert mix_string("AAA", "bbb") == "AbAbAb"
    assert mix_string("AA", "") == "AA"
    assert mix_string("mxdsrn", "ie tig") == "mixed string"

    """assert bingo([
        [5, 7, 11, 15, 21],
        [22, 25, 26, 27, 9],
        [34, 2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37, 3, 6, 32],
    ], [5, 21, 90, 32]) == (True, False, False)"""

    """assert bingo([
        [5, 7, 11, 15, 21],
        [22, 25, 26, 27, 9],
        [34, 2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37, 3, 6, 32],
    ], [5, 21, 90, 32, 25, 48, 81, 27, 61, 91]) == (True, True, False)"""

    # assert mirror_ends("abc") == "ac"
    # assert mirror_ends("abca") == "bc"
    # assert mirror_ends("abcba") == ""

    # assert prime_factorization(1960) == {2: 3, 5: 1, 7: 2}

    """candy_shop = CandyShop()
    candy1 = Candy('candy1', 'chocolate')
    candy2 = Candy('candy2', 'caramel')
    candy3 = Candy('candy3', 'nut')
    candy4 = Candy('candy1', 'chocolate')
    candy5 = Candy('candy2', 'vanilla')
    candy6 = Candy('candy2', 'vanilla')
    candy7 = Candy('candy3', 'nut')
    candy8 = Candy('candy1', 'chocolate')"""

    # candies = [candy1, candy2, candy3, candy4, candy5, candy6, candy7, candy8]

    # candy_shop.add_candies(candies)

    # NB! there are candy variable names in comments, not instance name parameter values!!!

    # print(candy_shop.get_candies_by_filling('chocolate'))  # [candy1, candy4, candy8]
    # print(candy_shop.get_least_popular_candy_name_and_filling())  # {name: candy2, filling: caramel}
    # print(candy_shop.get_most_popular_candy_name_and_filling())  # {name: candy1, filling: chocolate}
    # print(candy_shop.sort_candies_by_filling())  # [candy2, candy1, candy4, candy8, candy7, candy3, candy6, candy5]
    # print(candy_shop.collect_candies_by_filling())  # {chocolate: [candy1, candy4, candy8],
    #                                                  caramel: [candy2],
    #                                                  nut: [candy3, candy7],
    #                                                  vanilla: [candy5, candy6]}

    # Teacher, grade, student
    """mari = Student("Mari Maa")
    jyri = Student("Jyri Jogi")
    teele = Student("Teele Tee")
    cl = Class("Anna", [mari, jyri, teele])
    mari.grade(Grade(5, 3, "KT", "01/09/2020"))
    gr = Grade("!", 3, "KT", "01/09/2020")
    jyri.grade(gr)
    teele.grade(Grade(4, 3, "KT", "01/09/2020"))"""

    """print(f"Jyri keskmine hinne on {jyri.calculate_weighted_average()}.")  # 1

    jyri.redo_assignment(3, "KT", "14/09/2020")
    print(len(gr.previous_grades))  # 1

    print(f"Jyri keskmine hinne on nyyd {jyri.calculate_weighted_average()}.")  # 3
    print()

    mari.grade(Grade(5, 1, "TK", "30/11/2020"))
    jyri.grade(Grade(4, 1, "TK", "30/11/2020"))
    teele.grade(Grade(3, 1, "TK", "30/11/2020"))

    print(f"Teele keskmine hinne on {teele.calculate_weighted_average()}.")  # 4
    print(cl.get_grade_sheet())
    print()

    tuuli = Student("Tuuli Karu")
    cl.add_student(tuuli)
    print(len(cl.students))  # 4"""
    pass
