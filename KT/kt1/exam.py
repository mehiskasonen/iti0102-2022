"""KT1."""
import math

def capitalize_string(s: str) -> str:
    """
    Return capitalized string.

    The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if len(s) == 0:
        return s
    else:
        return s[:1].upper() + s[1:]


def has_seven(nums):
    """
    Whether the list has three 7s and no repeated consecutive elements.

    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    count = 0
    result = any(nums[i] == nums[i + 1] for i in range(len(nums) - 1))
    for nr in nums:
        if nr == 7:
            count += 1

    if count == 3 and result is False:
        return True
    else:
        return False


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], []]
    """

    # print((initial_list[-factor:]))
    # print(initial_list[:-factor])
    new_list = []
    """rolled_list = []"""
    counter = 0

    if factor == 0:
        new_list.append(initial_list)
        new_list = new_list * amount
        return new_list

    if amount == 0:
        return new_list

    if factor > 0:
        new_list.append(initial_list)
        counter += 1
        #return new_list
        #mult_list = new_list * amount
        while counter < amount:
            new_list.append(initial_list[-factor:] + initial_list[:-factor])
            factor = factor + factor
            print(factor)
            counter += 1
    return new_list


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    new = []
    first = 0
    second = 1
    call_log_dict = {}
    comma_split_call_log = call_log.split(",")
    sum_log = []
    for element in comma_split_call_log:
        print(element)
        colon_split_call_log = element.split(':')
        sum_log.append(colon_split_call_log)

    print(sum_log)




"""
    for element in sum_log:
        print(element)

        key = element[first]
        value = element[second]

        if key in call_log_dict.keys() and value in call_log_dict.values():
            continue
        if key in call_log_dict.keys() and value not in call_log_dict.values():
            call_log_dict[key].append(value)
        else:
            call_log_dict[key] = [value]

        first += 1
        second += 1

    print(call_log_dict)
    """


if __name__ == '__main__':
    # print(capitalize_string("abc"))  #  => "Abc"
    # print(capitalize_string("ABc"))  #  => "ABc"
    # print(capitalize_string(""))  #  => ""

    # print(has_seven([1, 2, 3]))  #  => False
    # print(has_seven([7, 1, 7, 7]))  #  => False
    # print(has_seven([7, 1, 7, 1, 7]))  #  => True
    # print(has_seven([7, 1, 7, 1, 1, 7]))  #  => False

    # print(list_move(["a", "b", "c"], 3, 0))  #  => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    # print(list_move(["a", "b", "c"], 3, 1))  #  => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    # print(list_move([1, 2, 3], 3, 2))  # => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    # print(list_move([1, 2, 3], 4, 1))  # => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    # print(list_move([], 3, 4))  # => [[], [], []]
    # print(list_move([['a']], 0, 2))
    # print(list_move(['P', 'e', 'l', 'm', 'e', 'e', 'n', 'i', 'd'], 2, 3))

    # print(parse_call_log(""))  # => {}
    # print(parse_call_log("ago:kati,mati:malle"))  # => {"ago": ["kati"], "mati": ["malle"]}
    print(parse_call_log("ago:kati,ago:mati,ago:kati"))  # => {"ago": ["kati", "mati"]}
    print(parse_call_log("ago:kati:mati"))  # => {"ago": ["kati"], "kati": ["mati"]}
    # print(parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati"))  # =>
    #{'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}