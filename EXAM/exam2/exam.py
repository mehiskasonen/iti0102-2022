"""Exam2 (2023-01-07)."""
from typing import Optional


def find_first_pair(text: str) -> str:
    """
    Find the first (consecutive) pair of the same symbols.

    If there are no such pair, return an empty string ("").

    It doesn't matter if there are more than 2 same consecutive symbols.

    find_first_pair("abbcc") => "bb"
    find_first_pair("abcccc") => "cc"
    find_first_pair("abBcccc") => "cc"
    find_first_pair("helo  world") => "  "
    find_first_pair("2022 was good") => "22"
    find_first_pair("2023 is the best") => ""
    find_first_pair("") => ""
    """
    result = ""
    try:
        for char in range(len(text) + 1):
            if text[char] == text[char + 1]:
                result += text[char] + text[char + 1]
                return result
    except IndexError:
        if len(result) < 1:
            return result
    finally:
        return result


def remove_non_palindrome_numbers(numbers: list) -> list:
    """
    Return list where all the non-palindrome numbers are removed.

    Palindrome number is a number which reads forward and backward the same: 1, 121, 55, 1001.
    If the number is a negative number, the minus does not count. So -1, -121, -99 are also palindromes.
    The result list should contain only palindromes.

    remove_non_palindrome_numbers([1, 2, 3]) => [1, 2, 3]
    remove_non_palindrome_numbers([1, 12, 62, 33]) => [1, 33]
    remove_non_palindrome_numbers([]) => []
    remove_non_palindrome_numbers([12]) => []
    remove_non_palindrome_numbers([-12]) => []
    remove_non_palindrome_numbers([-121]) => [-121]
    remove_non_palindrome_numbers([-121, 0, 12, 21, -12, 999]) => [-121, 0, 999]
    """
    palindromes = []
    for element in numbers:
        nr = str(abs(element))
        if nr[::-1] == nr:
            palindromes.append(element)
    return palindromes


def add_symbols(string: str, symbols: str) -> str:
    """
    Return given string with added symbols where needed.

    If letter in string exists in symbols, double it in result.
    If number in string exists in symbols, triple it in result.

    It does not change the result when any symbol appears more than once in symbols.

    add_symbols("ab12", "b12a") -> "aabb111222"
    add_symbols("xyz", "xxxxxx") -> "xxyz"
    add_symbols("aaaa", "b") -> "aaaa"
    add_symbols("aab", "a") -> "aaaab"
    """
    return_string = ""
    for char in string:
        if char in symbols:
            if char.isdigit():
                return_string += char * 3
            else:
                return_string += char * 2
        else:
            return_string += char
    return return_string


def h_index(articles: list) -> int:
    """
    Given a list where each value represents the times of citations of one article.

    Return a h index of the person.

    H-index is the largest number such that a number of publications
    have at least the same number of citations.

    Examples:
    [4, 2, 4] => 2
    [1, 2, 2] => 2
    [] => 0
    [1, 1, 1, 1] => 1
    [3, 5, 7] => 3
    [2, 5, 7] => 2
    [5, 4, 7, 3, 6] => 4
        [5, 4, 7, 3, 6] => 4
    Leia kõige suurem naturaalarv N nii, et leidub vähemalt N elementi, mille väärtus >= N.

    """
    if len(articles) < 1:
        return 0
    # maximum = 0
    # biggest_n = 0

    for n in range(len(articles) + 1):
        counter = 0
        for nr in articles:
            if nr >= n:
                counter += 1
        if counter < n:
            return n - 1

    """
    for nr in articles:
        biggest_n = nr
        for common in articles:
            if common >= nr:
                biggest_n -= 1
                if biggest_n == 0:
                    if nr > max:
                        max = nr
    return max
    """

def sum_of_digits_recursion(s: str) -> int:
    """
    Return sum of all the digits.

    The input string contains different symbols.
    Sum all the digits.

    The function has to be recursive (no loops allowed).

    sum_of_digits_recursion("123") => 6
    sum_of_digits_recursion("a") => 0
    sum_of_digits_recursion("") => 0
    sum_of_digits_recursion("1-2-3-99") => 24
    """
    if len(s) == 0:
        return 0
    else:
        if s[0].isdigit():
            return int(s[0]) + int(sum_of_digits_recursion(s[1:]))
        else:
            return sum_of_digits_recursion(s[1:])


def combine_numbers(numbers: list) -> int:
    """
    Find two elements in the list which give the highest cross sum.

    Cross sum is the sum of all the digits in the number.
    In this exercise you have to apply cross sum calculation until the result is below 10.
    For example: cross sum of 123 => 1 + 2 + 3 => 6
    cross sum on 991 => 9 + 9 + 1 => 19. Because it is not below 10, we calculate 1 + 9 => 10. And again 1 + 0 => 1.

    Here you have to take 2 different elements from the list, put them together
    (writing the first number in front of the second number) and then calculate cross sum.
    And the combined numbers which have the highest cross sum, is the result.

    The order of the combination should be the same as the elements appear in the list.

    combine_numbers([1, 2, 3]) => 23
      we can get the combinations: 12, 13, 23. 23 is the highest
    combine_numbers([1]) => 0
      there are no combinations possible, therefore return 0
    combine_numbers([9, 1]) => 91
      combinations: 91. 9 + 1 => 10, 1 + 0 => 1
    combine_numbers([1, 2, 3, 12, 66]) => 312
      combinations:
      12 => 1 + 2 = 3,
      13 => 1 + 3 = 4,
      112 => 1 + 1 + 2 = 4,
      166 => 1 + 6 + 6 = 13 => 4,
      23 => 5
      212 => 5
      266 => 14 => 5
      312 => 6
      366 => 15 => 6
      1266 => 15 => 6

    the highest cross sum is 6, and we return the first combination (the leftmost) 312.

    Simplification:
    if the function does not calculate second or third round for cross sum, then max points are 60%
    e.g. 991 would give 19
    (in those tests there are no combinations which give cross sum higher than 9)

    print(combine_numbers([1, 2, 3, 12, 66]))
    """
    sum_up = []
    return_combo = 0
    maximum = 0
    sub_sum = 0
    for outer in range(len(numbers)):
        for inner in range(outer, len(numbers) - 1):
            # print(inner + 1)
            # print(len(numbers))
            if inner + 1 < len(numbers) + 1:
                combination = str(numbers[outer]) + str(numbers[inner + 1])
                # print(combination)
                for element in combination:
                    sub_sum += int(element)
                if sub_sum > maximum:
                    # return_combo = 0
                    maximum = sub_sum
                    return_combo = int(combination)
                    sub_sum = 0
                else:
                    sub_sum = 0
                    # sum_up.append(combination)

                # print(sum_up)
    return return_combo


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
        """Initialize candy Shop."""
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
        Return list of candies sorted by filling in alphabetical order.

        If filling is the same, then sort
        by name in alphabetical order.

        :return: sorted list of candies
        """
        pass

    def get_most_popular_candy_name_and_filling(self) -> dict[str, str]:
        """
        Find the most popular candy name and filling.

        Method should return dict with name and filling of the most popular candy in the shop (type of candy which name
        and filling is present the most in the shop). NB! You should consider the most popular combination of name and filling.
        {name: most_pop_candy_name, filling: most_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of most pop candy
        """
        pass

    def get_least_popular_candy_name_and_filling(self) -> dict[str, str]:
        """
        Find the least popular candy name and filling.

        Method should return dict with name and filling of the least popular candy in the shop (type of candy which name
        and filling is present the least in the shop). NB! You should consider the least popular combination of name and filling.
        {name: least_pop_candy_name, filling: least_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of least pop candy
        """
        pass

    def collect_candies_by_filling(self) -> dict[str, list[Candy]]:
        """
        Group candies by filling.

        Method should return dict with candies divided by filling, where dict key is filling and dict value is list
        of candies with this filling.
        {candy_filling: [candy1, candy2]}

        :return: dict of candies divided by filling
        """
        pass


class Plant:
    """The plants that the plant store sells and the plant collector can purchase."""

    def __init__(self, species: str, rarity: int, size: int):
        """
        Initialize the plant.

        The price for the plant is taken from the table based on the size and rarity.
        """
        self.species = species
        self.rarity = rarity
        self.size = size
        self.price = 0

    def __repr__(self):
        """Return string representation of the plant, which is the species of the plant."""
        pass

    def update_rarity(self, rarity: int):
        """Update the rarity of the plant."""
        pass


class PlantStore:
    """Plant store where the different plants are sold and the plant collectors can purchase from."""

    def __init__(self, name: str, pricing_coefficient: float):
        """Initialize plant store."""
        self.pricing_coefficient = pricing_coefficient
        self.name = name
        self.stock = {}
        self.members_club = []
        self.members_only_stock = {}

    def update_stock(self, plant: Plant, amount: int):
        """
        Add plants and their amounts to the stock.

        If the plant is already in stock, adds new amount to current amount.
        """
        pass

    def update_members_only_stock(self, plant: Plant, amount: int):
        """
        Add plants and their amounts to the members only stock.

        If the plant is already in stock, adds new amount to current amount.
        """
        pass

    def sell_plant(self, plant: Plant, customer: 'PlantCollector'):
        """
        Sell the plant to the customer, removing one plant of that type from stock.

        It is important to note that plants that are in the members only stock are to be removed
        from that particular stock and are only sold to customers with a
        membership.
        """
        pass

    def get_members_only_stock(self) -> dict[Plant, int]:
        """Return the members only stock."""
        pass

    def get_stock(self) -> dict[Plant, int]:
        """Return the stock available to all customers."""
        pass

    def assign_membership(self, customer: 'PlantCollector'):
        """Add a customer to the members list."""
        pass

    def get_stock_value(self) -> int:
        """
        Calculate the sale value of the whole stock (both regular and members only stock).

        Multiply the prices and amounts of each plant and then also multiply everything
        by the store's pricing coefficient. Note that the members only stock plants
        do not need to be multiplied by the pricing coefficient, their price is already their sale price.
        """
        pass

    def is_in_stock(self, plant_name: str, customer: 'PlantCollector') -> bool:
        """
        Respond to a customer's query about whether a plant by that name (species) is in stock.

        It is important to note that if a plant is in members only stock and the customer is not a member,
        the plant is not 'in stock' for them, even if the store actually has the plant they are asking for.
        Returns the boolean True if the plant is in stock, and False if not.
        """
        pass

    def get_plant_details(self, plant_name: str) -> Plant:
        """
        Return the full plant object by name (species).

        If no such plant exists in the store's stock, returns None.
        """
        pass


class PlantCollector:
    """Plant collector who buys and collects plants."""

    def __init__(self, name: str):
        """Initialize the plant collector."""
        self.name = name
        self.collection = []
        self.wishlist = []
        self.room = {}

    def add_to_collection(self, plant: Plant):
        """Add a plant to the collector's collection if not already there."""
        pass

    def add_to_wishlist(self, plant_name: str):
        """Add a plant's name to the collector's wishlist if not already there."""
        pass

    def remove_from_wishlist(self, plant_name: str):
        """Remove a plant name from the collector's wishlist."""
        pass

    def add_space(self, space_type: int, space_amount: int):
        """
        Add space to the collector's home.

        If there are no spaces of that size, create a new entry in the dict, otherwise
        add to the amount that already exists.
        """
        pass

    def calculate_collection_value(self) -> int:
        """
        Calculate the collector's plant collection value.

        Add the prices of all the plants together.
        """
        pass

    def most_expensive_wishlist_plant(self, store: PlantStore) -> Optional[str]:
        """
        Find the most expensive wishlist plant.

        As different stores have different prices (pricing coefficient can be
        different), a PlantStore object is also given as an argument to the function.
        Return the name of the most expensive
        plant or if none of the plants in the wishlist are in stock at the store, return None.
        """
        pass

    def buy_wishlist_plant(self, store: PlantStore) -> str:
        """
        Buy the plant that's both the most expensive and biggest one on their wishlist that they have space for.

        It's important to note that a store always carries only one size of any given plant,
        so if a plant is sold at the store, it is only available in that one size.
        If a plant is bought, it should be added to the collection, removed from wishlist and the store and also place it
        somewhere in the home of the collector, meaning a corresponding free space slot should be removed.
        If purchasing a plant was successful, this function returns the species of the plant, if not, returns the string
        "No wishlist plants are for sale in this store of fit in your home!"
        """
        pass

    def buy_plant(self, plant_name: str, store: PlantStore) -> str:
        """
        Buy the plant if it is possible.

        Buys the plant with the given name from the store if it is in stock. Add the plant to collection, remove from wishlist,
        remove from the stock of the store and amend the amount of space available in the home.
        If the purchase is successful, returns the species of the plant, if not, returns the string "Cannot buy this plant!"
        """
        pass


if __name__ == '__main__':
    # print(find_first_pair("helloo"))  # == "ll")
    assert find_first_pair("abbcc") == "bb"
    assert find_first_pair("helloo") == "ll"
    assert find_first_pair("1233") == "33"
    assert find_first_pair("12333") == "33"

    # print(remove_non_palindrome_numbers([-1, -6, -12, -101]))  # == [-1, -6, -101])
    # print(remove_non_palindrome_numbers([-1, -6, -12]))  # == [-1, -6])
    # assert remove_non_palindrome_numbers([1, 2, 3]) == [1, 2, 3]
    # assert remove_non_palindrome_numbers([-1, -6, -12]) == [-1, -6]
    # assert remove_non_palindrome_numbers([]) == []
    # assert remove_non_palindrome_numbers([12, 345]) == []

    # print(add_symbols("aab1", "a12"))  # == "aaaab111")
    assert add_symbols("aab", "a") == "aaaab"
    assert add_symbols("aab1", "a12") == "aaaab111"

    print(h_index([5, 4, 7, 3, 6]))  # == 4)
    print(h_index([4]))  # == 4)
    # print(h_index([4, 2, 4]))  # => 2
    # print(h_index([1, 2, 2]))  # => 2
    print(h_index([]))  # => 0
    print(h_index([1]))  # => 1?

    # print(h_index([1, 1, 1, 1]))  # => 1
    # print(h_index([3, 5, 7]))  # => 3
    # print(h_index([2, 5, 7]))  # => 2
    # print(h_index([5, 4, 7, 3, 6]))  # => 4
    assert h_index([4, 2, 4]) == 2
    assert h_index([5, 4, 7, 3, 6]) == 4

    # print(sum_of_digits_recursion("123"))  # == 6)
    assert sum_of_digits_recursion("123") == 6
    assert sum_of_digits_recursion("") == 0

    # print(combine_numbers([1, 2, 3]))  # == 23)
    # print(combine_numbers([1, 2, 3, 12, 66]))  # == 312)
    assert combine_numbers([1, 2, 3]) == 23
    assert combine_numbers([1]) == 0
    assert combine_numbers([1, 2, 3, 12, 66]) == 312

    # Candy shop
    candy_shop = CandyShop()
    candy1 = Candy('candy1', 'chocolate')
    candy2 = Candy('candy2', 'caramel')
    candy3 = Candy('candy3', 'nut')
    candy4 = Candy('candy1', 'chocolate')
    candy5 = Candy('candy2', 'vanilla')
    candy6 = Candy('candy2', 'vanilla')
    candy7 = Candy('candy3', 'nut')
    candy8 = Candy('candy1', 'chocolate')

    candies = [candy1, candy2, candy3, candy4, candy5, candy6, candy7, candy8]

    candy_shop.add_candies(candies)

    assert candy_shop.get_candies_by_filling('chocolate') == [candy1, candy4, candy8]
    assert candy_shop.get_least_popular_candy_name_and_filling() == {"name": "candy2", "filling": "caramel"}
    assert candy_shop.get_most_popular_candy_name_and_filling() == {"name": "candy1", "filling": "chocolate"}
    assert candy_shop.sort_candies_by_filling() == [candy2, candy1, candy4, candy8, candy7, candy3, candy6, candy5]
    assert candy_shop.collect_candies_by_filling() == {"chocolate": [candy1, candy4, candy8],
                                                       "caramel": [candy2],
                                                       "nut": [candy3, candy7],
                                                       "vanilla": [candy5, candy6]}

    # Plantstore
    jungle_garden = PlantStore("Jungle Garden", 1.2)
    assert jungle_garden.name == "Jungle Garden"
    assert jungle_garden.pricing_coefficient == 1.2
    assert jungle_garden.stock == {}
    assert jungle_garden.members_club == []
    assert jungle_garden.members_only_stock == {}

    lancifolia = Plant("Calathea Lancifolia", 0, 2)
    monstera_deliciosa = Plant("Monstera Deliciosa", 0, 0)
    micans = Plant("Philodendron Micans", 1, 1)
    jungle_garden.update_stock(lancifolia, 9)
    jungle_garden.update_stock(monstera_deliciosa, 3)
    jungle_garden.update_stock(micans, 8)

    expected_stock = {
        micans: 8,
        lancifolia: 9,
        monstera_deliciosa: 3
    }
    assert jungle_garden.get_stock() == expected_stock
    assert jungle_garden.get_stock_value() == 774.0

