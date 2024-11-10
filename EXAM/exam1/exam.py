"""Exam1 (2023-01-04)."""
import math
import string
from typing import Optional


def count_digits(text: str) -> int:
    """
    Return the count of digits in a string.

    count_digits("123") => 3
    count_digits("a") => 0
    count_digits("") => 0
    count_digits("0a9r44") => 4
    """
    count = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in text:
        if char in digits:
            count += 1
    return count


def pairwise_min(numbers: list[int]) -> list[int]:
    """
    Return a list where for every element pair in the input list the minimum of those is used.

    If there are odd number of elements, ignore the last lonely element.

    pairwise_min([1, 2, 3, 4]) => [1, 3]
    pairwise_min([]) => []
    pairwise_min([1, 9, 2]) => [1]
    pairwise_min([9, 9, 2, 2]) => [9, 2]
    """
    return_list = []
    compare = []
    for nr in numbers:
        compare.append(nr)
        if len(compare) == 2:
            return_list.append(min(compare))
            compare = []
    return return_list


def same_length(texts: list[str]) -> list[str]:
    """
    Normalize the lengths of the elements and return a list of those normalized elements in reverse order.

    You have to find the longest element in the list.
    Append "_" to every shorter element so that all the lengths are equal.
    Return a list of those equal-length elements in reverse alphabetical order.

    same_length(["a", "ab", "abc"]) => ["abc", "ab_", "a__"]
    same_length([]) => []
    same_length(["_", "ab_", "a"]) => ["ab_", "a__", "___"]
    """
    return_list = []
    if len(texts) == 0:
        return []
    longest = max(texts, key=lambda x: len(x))
    # print(longest)
    for element in texts:
        if element != longest:
            diff = len(longest) - len(element)
            element += "_" * diff
            return_list.append(element)
        else:
            return_list.append(element)
    return sorted(return_list, reverse=True)


def max_average(data: list, n: int) -> float:
    """
    Find maximum average with window width of n.

    max_average([1, 2, 3], 2) = (2 + 3) / 2
      possible variants with window 2: [1, 2], [2, 3]
    max_average([1, 7, 4, 5, 6], 3) = (7 + 4 + 5) / 3 = 5.333333
      possible variants with window 3: [1, 7, 4], [7, 4, 5], [4, 5, 6]

    :param data - data with at least n + 1 elements.
    :param n - Window width. Amount of consecutive numbers to take into calculation. n > 0.

    :return Maximum average achievable with current parameters.
    """
    result = 0
    maximum = -999999999999
    find_max = []

    for nr in range(len(data)):
        find_max.append(data[nr:nr + n])

    for i in find_max:
        if len(i) == n:
            if sum(i) > maximum:
                maximum = sum(i)
                result = float(sum(i) / len(i))

    return result


def fuel_calculator(fuel: int) -> int:
    """
    Find needed amount of fuel for a given mass.

    Amount of fuel needed = mass divided by three, rounded down, subtract two
    + fuel needed for the fuel itself
    + fuel needed for the fuel's fuel + etc.

    Negative fuel rounds to zero.

    The solution has to be recursive! (no loops allowed)

    Examples:
    fuel_calculator(10) -> 1 + 0 = 1
    fuel_calculator(151) -> 48 + 14 + 2 + 0 = 64
    """
    if fuel < 6:
        return 0
    else:
        return (fuel // 3 - 2) + fuel_calculator(fuel // 3 - 2)


def longest_alphabet(text: str) -> str:
    """
    Find the longest substring which contains consecutive letters from alphabet.

    The input contains only lower case ascii letters (a - z).
    If there are several matches with the longest length, return the one which is lower alphabetically.

    longest_alphabet("abc") => "abc"
    longest_alphabet("abcklmn") => "klmn"
    longest_alphabet("klmabcopq") => "abc"
    longest_alphabet("a") => "a"
    longest_alphabet("xyab") => "ab"
    """
    """
    words = []
    result = []
    longest = []
    max_word_length = 0
    """
    best = ""
    if len(text) == 0:
        return ""
    if len(text) == 1:
        return text
    alphabet = string.ascii_letters

    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            word = text[start:end]
            if word in alphabet:
                if len(word) > len(best):
                    best = word
                elif len(word) == len(best):
                    if word < best:
                        best = word
    return best

    """
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            word = text[start:end]
            words.append(word)
    # print(words)

    for word in words:
        if word in alphabet:
            result.append(word)
    # print(result)

    max_len = len(max(result, key=len))
    # print(max_len)

    for i in result:
        if len(i) == max_len:
            longest.append(i)
    # print(longest)
    sorted_longest = sorted(longest)
    """


class Donut:
    """Donut class."""

    def __init__(self, filling: str, icing: str):
        """
        Donut class constructor.

        :param filling: donut filling
        :param icing: donut icing
        """
        self.filling = filling
        self.icing = icing

    def __repr__(self):
        return f"({self.filling}, {self.icing})"


class DonutFactory:
    """DonutFactory class."""

    def __init__(self):
        """DonutFactory class constructor."""
        self.production_line = []
        self.packed_donuts = {}

    def add_donuts(self, donuts: list):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        for item in donuts:
            self.production_line.append(item)

    def get_donuts(self) -> list:
        """
        Return list of all donuts present on the line at the moment.

        :return: list of all donuts
        """
        return self.production_line

    def package_donuts(self):
        """Common method to package donuts."""
        for item in self.production_line:
            key = (item.filling, item.icing)
            value = item
            if key in self.packed_donuts:
                self.packed_donuts[key].append(value)
            else:
                self.packed_donuts[key] = [value]
        return self.packed_donuts

    def empty_production_line(self):
        """Empties the production line."""
        self.production_line = []

    def pack_donuts_by_filling_and_icing(self) -> dict:
        """
        Method should return dict with donuts divided by filling and icing.

        Dict key must be represented as tuple of filling and icing and value as list of donuts with
        given filling and icing.
        {(filling, icing): [donut1, donut2]}

        After packing, the production line for donuts should be empty (everything is packed).

        :return: dict
        """
        self.empty_production_line()

        return self.package_donuts()

    def sort_donuts_by_icing_and_filling(self) -> list:
        """
        Method should return list of donuts sorted by icing in alphabetical order and then by filling in alphabetical order.

        :return: sorted list of donuts
        """
        return list(sorted(self.production_line, key=lambda x: (x.icing, x.filling), reverse=False))

    def get_most_popular_donut(self) -> dict:
        """
        Method should return dict with icing and filling of the most popular donut.

        {'icing': most_pop_donut_icing, 'filling': most_pop_donut_filling}
        If there are several icing-filling combinations with the same amount of donuts,
        use the one which icing is alphabetically lower (a comes before b).

        Hint: you could use the result similar to pack_donuts_by_filling_and_icing method,
        but you cannot empty the production line of donuts.
        So, a common custom method can help here, which returns the dict.
        The most popular combination is the one element of the dict which has the most donuts
        (len on dict value is the highest).

        :return: dict with icing and filling of most pop donut
        """
        result = {'icing': object, 'filling': object}
        all_donuts = self.package_donuts()
        most_popular = []
        maximum = 0

        for key, value in all_donuts.items():
            if len(value) > maximum:
                maximum = len(value)
                most_popular.append(key)
        print(most_popular)
        result['icing'] = most_popular[0][1]
        result['filling'] = most_popular[0][0]

        return result

    def get_donuts_by_flavour(self, flavour: str) -> list:
        """
        Get list of donuts that have the same icing or filling as given in method parameter.

        :return: list of donuts with the given flavour.
        """
        result_list = []
        for item in self.production_line:
            if flavour == str(item.icing) or flavour == str(item.filling):
                result_list.append(item)
        return result_list


class TravelItem:
    """Travel item."""

    def __init__(self, location: str, duration: int):
        """Initialize travel item with location and duration."""
        pass

    def get_location(self) -> str:
        """Return location."""
        pass

    def get_duration(self) -> int:
        """Return duration."""
        pass


class TravelPackage:
    """Travel package combines multiple travel items."""

    def __init__(self, name: str):
        """Initialize the package with the given name."""
        pass

    def create_duplicate(self, new_name: str) -> 'TravelPackage':
        """
        Create a duplicate travel package.

        The new package will be created with the new name.
        Also, all the items should be copied to the new package.
        """
        pass

    def get_total_duration(self) -> int:
        """Return the total duration of travel items in the package."""
        pass

    def get_items(self) -> list[TravelItem]:
        """Return list of TravelItem objects."""
        pass

    def get_name(self) -> str:
        """Return the name of the package."""
        pass


class TravelAgency:
    """Travel agency coordinates travel items and packages."""

    def __init__(self):
        """Initialize the agency."""
        pass

    def add_item_to_package(self, package_name: str, item: TravelItem) -> bool:
        """
        Add an item to the travel package.

        If this item already exists in the package with the given name,
        the method returns False (and the item is not added).

        Otherwise:
        If there is no package with the given name, then the package is created.
        The item is added to the package with the given name.
        The method returns True.
        """
        pass

    def get_packages(self) -> list[TravelPackage]:
        """Return list of packages in the insertion order."""
        pass

    def get_packages_by_location(self, location: str) -> list[TravelPackage]:
        """Return a list of TravelPackage objects where at least one item has the given location."""
        pass

    def search_package(self, locations: list, min_duration: int = None, max_duration: int = None) -> Optional[TravelPackage]:
        """
        Find a package which has all the locations specified in the list.

        If min_duration or max_duration is specified, then filter out packages,
        where total duration is between those values.

        If only min_duration is specified, use only those packages where total duration is greater or equal to that.
        If only max_duration is specified, use only those packages where total duration is less or equal to that.
        If both are specified, use packages where total duration is between those values.
        If none are specified, use all the packages.

        If locations list is empty, then every package matches.

        If multiple packages match, it doesn't matter which one to return.

        Return the found packages. If nothing matches, return None.
        """
        pass

    def get_package_overview_by_locations(self) -> str:
        """
        Create an overview where for every location all the packages are listed.

        The overview contains locations (strings) ordered alphabetically.
        And for every location a list of package names where this location is included, also ordered alphabetically.

        The format:

        location1:
         - package1
         - package2
        location2:
         - package1
         - package3

        The location has no spaces in front of it and is followed by the colon.
        The package has space, minus and space in front of it.
        There is no new line in the end of the string.

        If there are no packages, return empty string.
        """
        pass


if __name__ == '__main__':
    assert count_digits("123") == 3
    assert count_digits("a") == 0

    # print(pairwise_min([1, 2, 4, 3]))

    assert pairwise_min([1, 2, 4, 3]) == [1, 3]
    assert pairwise_min([1, 1, 4, 3, 5]) == [1, 3]

    # print(same_length(["a", "ab", "abc"]))  # => ["abc", "ab_", "a__"]
    # print(same_length([]))  # => []
    # print(same_length(["_", "ab_", "a"]))  # => ["ab_", "a__", "___"]
    # print(same_length(["aaa", "b"]))  # == ["b__", "aaa"]
    assert same_length(["a", "b"]) == ["b", "a"]
    assert same_length(["aaa", "b"]) == ["b__", "aaa"]

    # print(max_average([1, 2, 3, 3], 2))  # 3.0
    # print(max_average([1, 7, 4, 5, 6], 3))  # = (7 + 4 + 5) / 3 = 5.333333
    # print(max_average([-10, -50, -100, -50, -100], 3))  # = (-100 + -50 + -100) / 3 = -83.33

    assert max_average([1, 2, 3, 3], 2) == 3.0  # (3 + 3) / 2
    assert max_average([1, 7, 2, 3, 3], 1) == 7.0
    assert max_average([1, 7, 2, 3, 3], 3) == 4.0  # (7 + 2 + 3) / 3
    assert max_average([8, 2, 9], 2) == 5.5  # (2 + 9) / 2

    # possible variants with window 3: [1, 7, 4], [7, 4, 5], [4, 5, 6]

    # print(fuel_calculator(151))
    # print(fuel_calculator(-1))
    assert fuel_calculator(151) == 64
    assert fuel_calculator(-1) == 0

    # print(longest_alphabet("a"))  # => "a")
    # print(longest_alphabet("klmabcopq"))  # == "abc")
    assert longest_alphabet("abc") == "abc"
    assert longest_alphabet("abcklmn") == "klmn"
    assert longest_alphabet("klmabcopq") == "abc"
    assert longest_alphabet("a") == "a"
    assert longest_alphabet("xyab") == "ab"

    # donut examples

    donut_factory = DonutFactory()
    donut1 = Donut('chocolate', 'sugar')
    donut2 = Donut('caramel', 'chocolate')
    donut3 = Donut('cherry', 'marshmallow')
    donut4 = Donut('chocolate', 'sugar')
    donut5 = Donut('vanilla', 'cream')
    donut6 = Donut('vanilla', 'cream')
    donut7 = Donut('cherry', 'marshmallow')
    donut8 = Donut('chocolate', 'sugar')
    donut9 = Donut('vanilla', 'cream')

    donuts = [donut1, donut2, donut3, donut4, donut5, donut6, donut7, donut8, donut9]

    donut_factory.add_donuts(donuts)

    # print(donut_factory.get_donuts_by_flavour("marshmallow"))  # == [donut3, donut7]
    assert donut_factory.get_donuts_by_flavour("marshmallow") == [donut3, donut7]
    assert donut_factory.get_most_popular_donut() == {'icing': 'sugar', 'filling': 'chocolate'}
    # assert donut_factory.sort_donuts_by_icing_and_filling() == [donut2, donut5, donut6, donut3, donut7, donut1,
                                                                # donut4, donut8]
    assert donut_factory.pack_donuts_by_filling_and_icing() == {
        ('chocolate', 'sugar'): [donut1, donut4, donut8],
        ('vanilla', 'cream'): [donut5, donut6, donut9],
        ('caramel', 'chocolate'): [donut2],
        ('cherry', 'marshmallow'): [donut3, donut7],
        ('vanilla', 'cream'): [donut5, donut6]
    }

    # travel agency
    item_tallinn = TravelItem("Tallinn", 200)
    item_tartu = TravelItem("Tartu", 150)

    agency = TravelAgency()
    assert agency.get_packages() == []

    assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is True
    assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is False

    assert agency.add_item_to_package("Estonian trip", item_tallinn) is True
    assert agency.add_item_to_package("Estonian trip", item_tartu) is True

    assert len(agency.get_packages()) == 2
    assert agency.get_packages()[0].get_name() == "Shorty in Tallinn"
    assert agency.get_packages()[1].get_name() == "Estonian trip"

    assert agency.get_packages()[1].get_total_duration() == 350

    packages = agency.get_packages_by_location("Tallinn")
    assert len(packages) == 2
    assert packages[0].get_name() == "Shorty in Tallinn"
    assert packages[1].get_name() == "Estonian trip"

    assert agency.get_packages_by_location("Narva") == []

    package = agency.search_package(["Tartu"])
    assert package.get_name() == "Estonian trip"
    package = agency.search_package(["Tallinn"])
    assert package.get_name() in ["Estonian trip", "Shorty in Tallinn"]
    package = agency.search_package(["Tallinn"], min_duration=300)
    assert package.get_name() == "Estonian trip"

    assert agency.get_package_overview_by_locations() == "Tallinn:\n - Estonian trip\n - Shorty in Tallinn\nTartu:\n - Estonian trip"

