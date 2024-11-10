"""Exam 6 (2023-01-17)."""


def double_letters(text: str) -> str:
    """
    Double every letter in text.

    Latin letters (a-z and A-Z) have to be doubled for the output.
    All other symbols should remain the same.

    double_letters("abc") => "aabbcc"
    double_letters("hello world") => "hheelllloo wwoorrlldd"
    double_letters("Hi!?") => "HHii!?"
    """
    pass


def count_digits_chars_symbols(string: str) -> str:
    """
    Count digits, characters and other symbols.

    Count all the letters, numbers and special symbols from the given string.
    If the input is an empty string, return "".

    There is no difference whether the count is 1 or more, we use plural nouns ("1 symbols", "1 digits", "1 chars").
    Depending on the input, the output has to be in The format:

    count_digits_chars_symbols("aa") => The input has 2 chars
    count_digits_chars_symbols("33") => The input has 2 digits
    count_digits_chars_symbols("¤") => The input has 1 symbols
    count_digits_chars_symbols("sbf56") => The input has 3 chars, 2 digits
    count_digits_chars_symbols("db/") => The input has 2 chars, 1 symbols
    count_digits_chars_symbols("545#¤%") => The input has 3 digits and 3 symbols
    count_digits_chars_symbols("545dd#¤%") => The input has 2 chars, 3 digits and 3 symbols
    """
    pass


def mix_string(s1: str, s2: str) -> str:
    """
    Given two strings s1 and s2, create a mixed string by alternating between str1 and str2 chars.

    mix_string("AAA", "bbb") -> "AbAbAb"
    mix_string("AA", "") -> "AA"
    mix_string("mxdsrn", "ie tig") -> "mixed string"
    """
    pass


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


def reverse_substring(s: str, substring: str) -> str:
    """
    Reverse every substring in the string.

    Reverse every occurrence of substring and return the modified string.

    The function has to be recursive.
    No loops allowed!
    Also, "x in y" not allowed.

    reverse_subword("abcde", "bc") => "acbde"
    reverse_subword("abcabc", "bc") => "acbacb"
    reverse_subword("abcabc", "ac") => "abcabc"

    :param s: original string
    :param substring: len(substring) > 0
    :return:
    """
    if len(s) < len(substring):
        return s
    if s.startswith(substring):
        return substring[::-1] + reverse_substring(s[len(substring):], substring)
    else:
        return s[0] + reverse_substring(s[1:], substring)


def valid_parentheses(sequence: str) -> bool:
    """
    Determine if the input string has valid parentheses.

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine whether the string is valid.

    The input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Example 1:
    Input: sequence = "()"
    Output: true

    Example 2:
    Input: sequence = "()[]{}"
    Output: true

    Example 3:
    Input: sequence = "(]"
    Output: false

    Example 4:
    Input: sequence = "([)]"
    Output: false

    Example 5:
    Input: sequence = "{[]}"
    Output: true

    :return boolean whether sequence is valid or not
    """
    stack = []
    for c in sequence:
        if c in '([{':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if c == ')' and stack[-1] in '[{':
                return False
            if c == ']' and stack[-1] in '({':
                return False
            if c == '}' and stack[-1] in '[(':
                return False
            stack.pop()
    return len(stack) == 0


class Patient:
    """Patient."""

    def __init__(self, name: str, illness: str, age: int):
        """
        Patient class constructor.

        :param name: patient's name
        :param illness: patient's illness
        :param age: patient's age
        """
        self.name = name
        self.illness = illness
        self.age = age


class Hospital:
    """Hospital."""

    def __init__(self, address: str, illnesses_to_cure: list[str]):
        """Hospital class constructor."""
        pass

    def add_patients(self, patients: list[Patient]):
        """
        Add patients if their illness can be cured in this hospital.

        If the same patient is already in the hospital, do not add.

        :param patients: list of patients to add
        :return:
        """
        pass

    def add_patient(self, patient: Patient):
        """
        Add patient if their illness can be cured in this hospital.

        If the same patient is already in the hospital, do not add.

        :param patient: patient to add
        :return:
        """
        pass

    def add_new_illness_to_cure(self, illness: str):
        """
        Add an illness if it is new to this hospital.

        :param illness: illness to add
        :return:
        """
        pass

    def get_patients(self) -> list[Patient]:
        """
        Return list of all patients in the hospital.

        :return: list of all patients
        """
        pass

    def get_illnesses(self) -> list[str]:
        """
        Return list of all illnesses that can be treated in this hospital.

        :return: list of all illnesses
        """
        pass

    def get_patients_by_illness(self, illness: str) -> list[Patient]:
        """
        Get list of patients that have the same illness as given in parameter value.

        :return: list
        """
        pass

    def sort_patients_by_illness(self) -> list[Patient]:
        """
        Return list of patients sorted by illness in alphabetical order.

        If illness is the same, then sort by age in descending order.

        :return: sorted list of patients
        """
        pass

    def collect_patients_by_illness(self) -> dict[str, list[Patient]]:
        """
        Group patients by illness.

        Method should return dict with patients divided by illness, where dict key is illness and dict value is list
        of patients with this illness.
        {illness: [patient1, patient2]}

        :return: dict of patients divided by illness
        """
        pass


class Grade:
    """Grade."""

    def __init__(self, grade, weight: int, assignment: str, date: str):
        """Initialize grade."""
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
        """Initialize student."""
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
        """Initialize class."""
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
    # assert double_letters("ab") == "aabb"
    # assert double_letters("a! b") == "aa! bb"

    # assert count_digits_chars_symbols("db/") == "The input has 2 chars, 1 symbols"
    # assert count_digits_chars_symbols("545#¤%") == "The input has 3 digits and 3 symbols"

    # assert mix_string("AAA", "bbb") == "AbAbAb"
    # assert mix_string("AA", "") == "AA"
    # assert mix_string("mxdsrn", "ie tig") == "mixed string"

    """
    assert bingo([
        [5, 7, 11, 15, 21],
        [22, 25, 26, 27, 9],
        [34, 2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37, 3, 6, 32],
    ], [5, 21, 90, 32]) == (True, False, False)

    assert bingo([
        [5, 7, 11, 15, 21],
        [22, 25, 26, 27, 9],
        [34, 2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37, 3, 6, 32],
    ], [5, 21, 90, 32, 25, 48, 81, 27, 61, 91]) == (True, True, False)
    """

    assert valid_parentheses("](])[[") is True
    assert valid_parentheses("()") is True
    assert valid_parentheses("[[") is False
    assert valid_parentheses("[(])") is False

    # hospital
    patient1 = Patient("patient1", "covid", 20)
    patient2 = Patient("patient2", "flu", 25)
    patient3 = Patient("patient3", "madness", 35)

    hospital = Hospital("HospiTalTech", ["flu", "madness"])
    hospital.add_patient(patient3)
    assert hospital.get_patients() == [patient3]

    hospital.add_patients([patient1, patient2, patient3])
    assert hospital.get_patients() == [patient3, patient2]

    assert hospital.sort_patients_by_illness() == [patient2, patient3]

    hospital.add_new_illness_to_cure("covid")

    hospital.add_patient(patient1)
    assert hospital.get_patients() == [patient3, patient2, patient1]
    assert hospital.get_patients_by_illness("flu") == [patient2]
    assert hospital.collect_patients_by_illness() == {
        'flu': [patient2],
        'madness': [patient3],
        'covid': [patient1]
    }

    # Teacher, grade, student
    mari = Student("Mari Maa")
    jyri = Student("Jyri Jogi")
    teele = Student("Teele Tee")
    cl = Class("Anna", [mari, jyri, teele])
    mari.grade(Grade(5, 3, "KT", "01/09/2020"))
    gr = Grade("!", 3, "KT", "01/09/2020")
    jyri.grade(gr)
    teele.grade(Grade(4, 3, "KT", "01/09/2020"))

    print(f"Jyri keskmine hinne on {jyri.calculate_weighted_average()}.")  # 1

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
    print(len(cl.students))  # 4