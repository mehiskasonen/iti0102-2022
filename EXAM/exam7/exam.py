"""Exam 7 (2022-01-19)."""
import math


def segment_number(first_number, last_number):
    """
    Segment number.

    Return list of numbers where only numbers between first_number
    and last_number (both inclusive) which divide by 5 but do not divide by 3
    are used.

    #1
    segment_number(1, 11) == [5, 10]
    segment_number(1, 4) == []
    segment_number(-20, 20) == [-20, -10, -5, 5, 10, 20]

    :param first_number: the lowest possible candidate
    :param last_number: the highest possible candidate
    :return: list of numbers
    """
    nr_list = []
    for nr in range(first_number, last_number + 1):
        if nr % 5 == 0 and nr % 3 != 0:
            nr_list.append(nr)
    return nr_list


def add_or_subtract(numbers):
    """
    Add or subtract.

    Return the sum of all numbers in a list.

    The sum is calculated according to following rules:
        -always start by adding all the numbers together.
        -if you find a 0, start subtracting all following numbers until you find another 0, then start adding again.
        -there might be more than two 0 in a list - change +/- with every 0 you find.

    For example:
        [1, 2, 0, 3, 0, 4] -> 1 + 2 - 3 + 4 = 4
        [0, 2, 1, 0, 1, 0, 2] -> -2 - 1 + 1 - 2 = -4
        [1, 2] -> 1 + 2 = 3
        [4, 0, 2, 3] = 4 - 2 - 3 = -1

    #2

    :param numbers: the list of number given.
    :return: the sum of all numbers.
    """
    change = 1
    result_sum = 0
    for nr in numbers:
        if nr == 0:
            change = change * -1
        if change > 0:
            result_sum += nr
        if change < 0:
            result_sum -= nr
    return result_sum


def should_get_up_early(is_weekday, really_tired, first_class_is_programming):
    """
    Return whether you should get up early.

    Decide if you should get up early enough for first class.

    You should only even consider getting up early if it is a weekday, on weekends you should never get up early.
    If it is a weekday you should typically get up early, unless you are really tired.
    But if it is a weekday and you are really tired but the first class is a programming class you should still get up
    early ignoring you being tired.

    #3
    TFT - True	testiga tagastas None. Otsin viga koodis.
    TFF - False	testiga tagastas True. Otsin viga koodis.


    :param is_weekday: is it a weekday or not, boolean
    :param really_tired: are you really tired, boolean
    :param first_class_is_programming: is the first class a programming class, boolean
    :return: True if you should get up early, otherwise False
    """
    if is_weekday is False:
        return False
    if is_weekday is True and really_tired is True and first_class_is_programming is True:
        return True
    if is_weekday is True and really_tired is False and first_class_is_programming is False:
        return True
    if is_weekday is True and really_tired is True and first_class_is_programming is False:
        return False
    if is_weekday is True and really_tired is False and first_class_is_programming is True:
        return True
    else:
        return False


def pear_fear(pears, people):
    """
    Pear fear.

    Every 3rd person fears pears, so they won't get any.
    How many pears will each get?
    Everyone who is not afraid of pears gets equal number of pears.
    Only whole pears will be used, so some pears may remain.

    #4
    pear_fear(10, 3) == 5
    pear_fear(10, 5) == 2
    pear_fear(0, 3) == 0
    pear_fear(17, 2) == 8
    pear_fear(21, 10) == 3

    :param pears:
    :param people:
    :return:
    """
    if pears == 0:
        return 0
    not_afraid = people - (math.floor((1 / 3) * people))
    result = math.floor(pears / not_afraid)
    return result


def string_between_string(word1, word2):
    """
    Insert reversed word2 to the center of word1.

    word1 length is always even.

    #5 "smrt", "a"

    :param word1: Initial word. String.
    :param word2: Word to reverse and insert. String.
    :return: New word as string.
    """
    w1_len = len(word1) // 2
    return word1[:w1_len] + word2[::-1] + word1[w1_len:]


def get_padded_string(string1, string2):
    """
    Pad the longer of two strings with the shorter one on both sides.

    If both strings are the same length, consider string1 as the longer one.
    For example when string1 is "pizza" and string2 is "bbq", this should return "bbqpizzabbq".

    #6

    :param string1: String one
    :param string2:  String two
    :return: Padded string
    """
    if len(string1) == len(string2) or string1 > string2:
        return string2 + string1 + string2
    if len(string1) < len(string2):
        return string1 + string2 + string1


def remove_duplicate(number_list):
    """
    Remove duplicates.

    Go though given list and remove all
    occurrences of two or more of the same
    numbers appearing after one another.
    Remove all but one of the duplicates.

    #7 remove_duplicate([1, 1, 1, 1, 1, 2, 1, 1, 3]) == [1, 2, 1, 3]

    :param number_list: input list
    :return: new list
    """
    result_list = []
    for nr in number_list:
        if len(result_list) == 0:
            result_list.append(nr)
        if len(result_list) > 0:
            if result_list[-1] == nr:
                continue
            else:
                result_list.append(nr)
    return result_list


def who_called(calls, name):
    """
    Who called.

    You are given a dictionary of calls and a name.
    Determine who called that name.
    The key of the dictionary is the caller, the value is to whom the caller called.
    If nobody called the person, return -1.
    Key=caller, value=called_person

    #8 ({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Alex") == "James"
       ({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Olaf") == -1

    :param calls: dictionary of all the calls
    :param name: name of the receiver
    :return: name of the caller
    """
    for k, v in calls.items():
        if v == name:
            return k
    return -1


def remove_lowest_digit(number):
    """
    Remove the lowest digit.

    Given a non-negative integer, remove the first occurrence
    of the lowest digit and return a new number.

    #9

    123 => 23
    223 => 23
    232 => 32
    1 => 0
    :param number: non-negative integer
    :return: non-negative integer
    """
    num = str(number)
    if len(num) == 1:
        return 0
    smallest = min(num)

    for nr in range(len(num)):
        print(nr)
    for nr in range(len(num)):
        if int(num[nr]) == int(smallest):
            index = nr
            if index == 0:
                return int(num[1:])
            else:
                return int(num[:index] + num[index + 1:])


def show_highest_grade(grade1, grade2):
    """
    Show highest grade.

    Print "Highest grade: GRADE"
    where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"

    #10

    :param grade1:
    :param grade2:
    :return:
    """
    if grade1 > grade2:
        print(f"Highest grade: {grade1}")
    else:
        print(f"Highest grade: {grade2}")


def transactions(transaction_string):
    """
    Calculate the result of transactions.

    Given a string of transactions between bank accounts
    return the amount of money on accounts A, B anc C.

    The transaction is in the following format:
    X,Y,Z
    where
    X is the account (A, B or C) the money is transferred from
    Y is the account (A, B or C) the money is transferred to
    Z is the amount transferred.

    For example:
    "A,B,100"
    The amount in account A is lowered by 100,
    the amount in account B is raised by 100.

    The transaction can take place if the starting
    account has enough money.
    Initially, every account has 100 units of money.

    Account C is credit account, meaning from
    that account the transactions can be executed even
    if there is no money left, the balance goes below 0.

    "C,A,101"
    as the first transaction yields in
    [201, 100, -1]

    "A,B,100" => [0, 200, 100]
    "A,B,10 B,C,10" => [90, 100, 110]

    "A,B,200 C,A,200" => [300, 100, -100]
    (the first transaction is cancelled)

    If the first account is 0 (zero), then
    the money is just transferred to the second account
    (like payment into the account).

    "0,A,100" => [200, 100, 100]
    "0,A,110 A,B,120" => [90, 220, 100]

    The input is always correct:
     - space separated transactions
     - transaction is in the format X,Y,Z
     - X is either '0', 'A', 'B' or 'C'
     - Y is either 'A', 'B' or 'C'
     - Z is non-negative integer

     #11

    :param transaction_string: string with transactions
    :return: list of ints (length 3)
    """
    accounts = {'A': 100, 'B': 100, 'C': 100}
    all_transactions = transaction_string.split(" ")
    result_list = []

    for trans in all_transactions:

        if trans[0] == '0':
            accounts[trans[2]] = accounts[trans[2]] + int(trans[4:])
            continue
        if trans[0] == 'A' or trans[0] == 'B':
            if accounts[trans[0]] < int(trans[4:]):
                continue
            else:
                accounts[trans[2]] = accounts[trans[2]] + int(trans[4:])
                accounts[trans[0]] = accounts[trans[0]] - int(trans[4:])
        else:
            accounts[trans[2]] = accounts[trans[2]] + int(trans[4:])
            accounts[trans[0]] = accounts[trans[0]] - int(trans[4:])

    for value in accounts.values():
        result_list.append(value)
    return result_list


def recursive_sum(list_of_numbers):
    """
    Recursive sum.

    Write a function that finds the sum of numbers in the given list recursively.
    Assume that the list always exists and can be empty or contain only numbers.

    #12 recursive_sum([1, 2, 3]) -> 6

    @param list_of_numbers: list of integers.
    @return: sum of numbers in list
    """
    if len(list_of_numbers) == 0:
        return 0
    else:
        return list_of_numbers[0] + recursive_sum(list_of_numbers[1:])


class Stargate:
    """
    Class Stargate.

    Stargate is a device that creates a wormhole between it and another stargate that can be used to travel between two
    stargates almost instantly. Stargate can dial (connect) to another stargate and a stargate can be connected to
    (dialed to) by another stargate. Each stargate can only have one active connection. A stargate can be only connected
    to if it is currently disconnected. When a stargate connects to a stargate it means that the destination stargate is
    also connected to the stargate that initiated the connection (the one who dialed). When one of the stargates that is
    connected disconnects, the other disconnects also. To dial out (initiate the connection it needs to have a Dial Home
    Device (DHD). Think of the DHD of like a controller. If it doesn't have one, it can oly be dialed to by another
    stargate (it can't dial out) and it can't initiate a disconnect (remains connected until the other stargate
    initiates the disconnect).
    """

    def __init__(self, planet_name, has_dial_home_device):
        """
        Construct a new stargate.

        :param planet_name: The name of the planet the stargate is on. String
        :param has_dial_home_device: Does the stargate have a Dial Home Device. Boolean
        """
        self.has_dial_home_device = has_dial_home_device
        self.planet_name = planet_name
        self.connection = False
        self.active_connections = {}

    def __repr__(self):
        """Return string representation on Stargate object."""
        return f"Stargate on {self.planet_name}, has DHD {self.has_dial_home_device}"

    def get_planet_name(self):
        """
        Get planet name.

        :return: The name of the planet the stargate is on. String
        """
        return self.planet_name

    def is_connected(self):
        """
        Whether is connected.

        :return: Is the stargate currently connected or not. Boolean
        """
        return self.connection

    def get_connected_stargate(self):
        """
        Get connected stargate.

        :return: The stargate this stargate is connected to. None if not connected. Stargate or None
        """
        if not self.connection:
            return None
        else:
            for k in self.active_connections.keys():
                if k == self.planet_name:
                    return Stargate

    def get_connected_planet_name(self):
        """
        Get connected planet name.

        :return: The name of the planet that the stargate that this stargate is connected to is on. None if not connected. String or None
        """
        if not self.connection:
            return None
        else:
            for k, v in self.active_connections.items():
                if k == self.planet_name:
                    return v

    def dial(self, destination):
        """
        Dial.

        Dial out to another stargate. This can only succeed if these criteria are met:
        * this stargate is not connected
        * this stargate has a Dial Home Device
        * the destination is an instance of the Stargate class
        * the destination stargate is currently not connected
        * this stargate is not trying to connect to itself

        :param destination: The stargate that this stargate should connect to. Stargate
        :return: Did the two stargates connect successfully. Boolean
        """
        can_dial = True
        if self.connection:
            return False
        if not self.has_dial_home_device:
            return False
        if not isinstance(destination, Stargate):
            return False
        if destination.connection:
            return False
        if self.planet_name == destination.planet_name:
            return False

        self.connection = True
        destination.connection = True

        if self.planet_name not in self.active_connections.items():
            self.active_connections[self.planet_name] = destination.planet_name

        return can_dial

    def disconnect(self):
        """
        Disconnect.

        Disconnect this stargate and the stargate that this stargate is connected to if this stargate is currently
        connected.
        """
        if self.connection:
            for k, v in self.active_connections.items():
                if self.planet_name == k:
                    k.connection = False
                    k.planet_name = ""
                if self.planet_name == v:
                    v.connection = False
                    v.planet_name = ""
        # print(self.active_connections)


class Student:
    """Student class."""

    def __init__(self, curriculum):
        """
        Initialize student.

        :param curriculum: the students curriculum.
        """
        self.curriculum = curriculum
        self.grades = {}

    def add_subject_to_curriculum(self, subject, eap):
        """
        Add the given subject to the students curriculum.

        If the subject is already in the curriculum, rewrite the EAPs.

        :param subject: the subject to be added to the curriculum.
        :param eap: how many EAPs the subject is worth.
        """
        student_curriculum = self.get_curriculum()
        if subject in student_curriculum.curriculum.keys():
            del student_curriculum.curriculum[subject]
            new_sub = Subject(subject, eap)
            student_curriculum.curriculum[new_sub] = None
            # setattr(subject, subject.eaps, eap)
        if subject not in student_curriculum.curriculum.keys():
            student_curriculum.curriculum[subject] = None

    def add_grade(self, subject, grade):
        """
        Add grade.

        Add the grade for the subject to students record if the subject is in the students curriculum.
        If the student already has a grade for said subject, rewrite it.
        The grade must be an integer between 0-5 (both included).

        :param subject: the subject for which the students has been given a grade.
        :param grade: the grade the student received. Must be between 0-5 (both included).
        """
        student_curriculum = self.get_curriculum()
        student_curriculum.add_subject_grade(subject, grade)

    def get_subject_grade(self, subject):
        """
        Get subject grade.

        Return the grade the student has received for the given subject.
        If the student has not received a grade for the subject yet return None.
        :param subject: the subject which grade to return.
        :return: the received grade or None.
        """
        student_curriculum = self.get_curriculum()
        for k, v in student_curriculum.curriculum.items():
            if k == subject:
                return v

    def get_average_grade(self):
        """
        Calculate the average of all grades on the students record.

        If a student has failed a subject (the grade is 0), don't count it.
        :return: the average grade with two decimal places.
        """
        grade_total = 0
        count = 0

        student_curriculum = self.get_curriculum()
        for v in student_curriculum.curriculum.values():
            if v is None:
                continue
            if v != 0:
                grade_total += v
                count += 1

        return round(grade_total / count, 2)

    def get_eaps(self):
        """
        Get EAP-s.

        Calculate, how many EAPs does the student currently have for passed subjects.
        A subject is passed when the student has received a grade greater than 0 for it.
        :return: the nr of EAPs.
        """
        total_eaps = 0
        student_curriculum = self.get_curriculum()
        for k, v in student_curriculum.curriculum.items():
            if v is None:
                continue
            if v != 0:
                total_eaps += k.eaps
        return total_eaps

    def get_curriculum(self):
        """
        Get the students curriculum.

        :return: a Curriculum object.
        """
        return self.curriculum


class Subject:
    """Subject class."""

    def __init__(self, name, eaps):
        """
        Initialize subject.

        :param name: name of the subject.
        :param eaps: how many EAPs the subject is worth.
        """
        self.name = name
        self.eaps = eaps

    """
    def __repr__(self):
        Representation of Subject object.
        return f"'{self.name}', '{self.eaps}' EAP"
    """

    def get_eaps(self):
        """
        Return how many EAPs the subject is worth.

        :return: nr of EAPs
        """
        return self.eaps


class Curriculum:
    """Curriculum class."""

    def __init__(self):
        """Initialize curriculum."""
        self.curriculum = {}

    def get_subject(self, name):
        """
        Get a subject from the curriculum by name.

        :param name: name of the subject.
        :return: subject object.
        """
        all_subs = self.get_all_subjects()
        for sub in all_subs:
            if sub.name == name:
                return sub

    def add_subject(self, subject):
        """
        Add the subject to curriculum.

        :param subject: the subject to be added.
        """
        if subject not in self.curriculum.keys():
            self.curriculum[subject] = None

    def get_all_subjects(self):
        """
        Get all subjects.

        :return: al list of all the subjects in the curriculum.
        """
        subject_list = []
        for k in self.curriculum.keys():
            subject_list.append(k)
        return subject_list

    def add_subject_grade(self, subject, grade):
        """
        Add subject grade.

        Add the grade for the subject to students record if the subject is in the students curriculum.
        If the student already has a grade for said subject, rewrite it.
        The grade must be an integer between 0-5 (both included).

        :param subject: the subject for which the students has been given a grade.
        :param grade: the grade the student received. Must be between 0-5 (both included).
        """
        if 0 > grade > 5:
            return None
        for k, v in self.curriculum.items():
            if k == subject:
                self.curriculum[k] = grade

    def get_grades(self):
        """
        Return a dictionary where keys are subjects and values are grades.

        The dictionary must include all subjects in teh curriculum, including those the student has not received a grade for yet.
        :return: dictionary.
        """
        return {k: v for (k, v) in self.curriculum.items()}


if __name__ == '__main__':

    # print(segment_number(-20, 20)) # == [-20, -10, -5, 5, 10, 20])
    assert segment_number(1, 11) == [5, 10]
    assert segment_number(1, 4) == []
    assert segment_number(-20, 20) == [-20, -10, -5, 5, 10, 20]

    # print(add_or_subtract([1, 2, 0, 3]))  # == 0
    # print(add_or_subtract([0, 1, 2]))  # == -3
    # print(add_or_subtract([1, 2, 0, 2, 0, 4]))  # == 5
    assert add_or_subtract([1, 2, 0, 3]) == 0
    assert add_or_subtract([0, 1, 2]) == -3
    assert add_or_subtract([1, 2, 0, 2, 0, 4]) == 5

    # print(should_get_up_early(True, True, True))  # True
    # print(should_get_up_early(True, True, False))  # False
    # print(should_get_up_early(True, False, True))  # True
    # print(should_get_up_early(True, False, False))  # False
    # print(should_get_up_early(False, False, True))  # ?
    # print(should_get_up_early(False, True, False))  # False
    # print(should_get_up_early(False, True, True))  # ?
    # print(should_get_up_early(False, False, False))  # False

    assert should_get_up_early(True, True, True) is True
    assert should_get_up_early(False, True, False) is False

    # print(pear_fear(10, 5))  # == 2)
    assert pear_fear(10, 3) == 5
    assert pear_fear(10, 5) == 2
    # assert pear_fear(0, 3) == 0
    # assert pear_fear(17, 2) == 8
    # assert pear_fear(21, 10) == 3

    # print(string_between_string("smrt", "a"))  # == "smart")
    # print(string_between_string("ho", "lle"))  # == "hello")
    # print(string_between_string('123456', '+'))  # 123+456
    # print(string_between_string('kXMiCXivgiSntPIpdUkC', 'TYUKkt'))  # TYUKktkXMiCXivgiSntPIpdUkCTYUKkt

    assert string_between_string("ho", "lle") == "hello"
    assert string_between_string("", "yas") == "say"
    assert string_between_string("smrt", "a") == "smart"
    assert string_between_string("w  d", " ro ") == "w  or  d"
    assert string_between_string(".,", ",.") == "..,,"

    assert get_padded_string("pizza", "bbq") == "bbqpizzabbq"
    assert get_padded_string("dog", "cat") == "catdogcat"
    assert get_padded_string("geoff", "giraffe") == "geoffgiraffegeoff"

    # print(remove_duplicate([1, 1, 1, 1, 1, 2, 1, 1, 3]))  # == [1, 2, 1, 3])
    # print(remove_duplicate([]))  # []
    # print(remove_duplicate([1, 1, 2, 2, 3, 3]))  # == [1, 2, 3])
    assert remove_duplicate([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert remove_duplicate([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicate([1, 1, 1, 1, 1, 2, 1, 1, 3]) == [1, 2, 1, 3]

    # print(who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Alex"))  # == "James"
    # print(who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Olaf"))  # == -1
    assert who_called({}, "Nathan") == -1
    assert who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Alex") == "James"
    assert who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Olaf") == -1

    # print(remove_lowest_digit(123))  # == 23
    # print(remove_lowest_digit(100))  # == 10)
    # print(remove_lowest_digit(7))  # == 0
    # print(remove_lowest_digit(4321))  # == 432

    # assert remove_lowest_digit(123) == 23
    # assert remove_lowest_digit(100) == 10
    # assert remove_lowest_digit(7) == 0
    # assert remove_lowest_digit(171) == 71

    # print(show_highest_grade(10, 14))
    assert show_highest_grade(10, 14) is None
    # prints:
    # Highest grade: 14

    # print(transactions("A,B,100"))
    # print(transactions("A,B,10 B,C,10 0,A,20"))  # == [110, 100, 110]
    # print(transactions("A,B,100"))  # == [0, 200, 100]
    assert transactions("A,B,100") == [0, 200, 100]
    assert transactions("C,A,200") == [300, 100, -100]

    # assert transactions("") == [100, 100, 100]
    # assert transactions("0,A,1000") == [1100, 100, 100]
    # assert transactions("A,B,10 B,C,10 0,A,20") == [110, 100, 110]

    # print(recursive_sum([1, 2, 3]))  # == 6)
    # print(recursive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # == 55
    assert recursive_sum([]) == 0
    assert recursive_sum([1, 2, 3]) == 6
    assert recursive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55

    # OOP1 - stargate

    sg1 = Stargate("Earth", True)
    sg2 = Stargate("Another planet", False)
    sg3 = Stargate("Abydos", True)
    sg4 = Stargate("Chulak", True)
    # print(sg1.dial(sg2))
    # print(sg1.is_connected())
    # print(sg1.dial(sg2))
    assert sg1.dial(sg2) is True
    assert sg3.dial(sg4) is True
    # print(sg1.get_connected_stargate())
    # print(sg1.get_connected_planet_name())
    # print(sg2.get_connected_planet_name())

    # print(sg1.active_connections)
    # print(sg3.active_connections)
    assert sg1.get_connected_planet_name() == "Another planet"
    sg2.disconnect()
    # sg1 Earth: Another Planet         disconnect: earth disconnect  , another planet disconnect
    # sg2 Another Planet: Earth?        disconnect: another planet disconnect  , earth disconnect
    # print(sg1.get_connected_planet_name())

    # assert sg2.get_connected_planet_name() == "Earth"
    # sg1.disconnect()
    assert sg2.get_connected_planet_name() is None
    assert sg2.dial(sg1) is False

    # OOP2 - student
    student = Student(Curriculum())

    subj1 = Subject("lineaar", 6)
    subj2 = Subject("matanaal", 5)
    subj3 = Subject("java", 4)

    student.get_curriculum().add_subject(subj1)
    student.get_curriculum().add_subject(subj2)
    student.get_curriculum().add_subject(subj3)

    student.add_grade(subj1, 3)
    student.add_grade(subj2, 5)
    assert student.get_subject_grade(subj3) is None
    # print(student.get_curriculum().get_subject('lineaar'))
    # print(student.get_eaps())
    # print(student.get_subject_grade(subj1))
    assert student.get_eaps() == 11
    assert student.get_subject_grade(subj2) == 5
    assert student.get_average_grade() == 4

    student.add_grade(subj2, 3)
    # student.add_grade(subj3, 4)
    # assert student.get_subject_grade(subj3) == 4

    assert student.get_subject_grade(subj2) == 3
    assert student.get_average_grade() == 3

    assert student.get_curriculum().get_subject("java") == subj3
