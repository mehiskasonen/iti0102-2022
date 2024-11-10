"""If you're going to perform inception, you need imagination."""


def x_sum_loop(nums: list, x: int) -> int:
    """
    Given a list of integers and a number called x iteratively return sum of every x'th number in the list.

    In this task "indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output should be -6 (3 + -9).

    X can also be negative, in that case indexing starts from the end of the list, see examples below.

    If x is 0, the sum should be 0 as well.

    print(x_sum_loop([], 3))  # 0
    print(x_sum_loop([2, 5, 6, 0, 15, 5], 3))  # 11
    print(x_sum_loop([0, 5, 6, -5, -9, 3], 1))  # 0
    print(x_sum_loop([43, 90, 115, 500], -2))  # 158
    print(x_sum_loop([1, 2], -9))  # 0
    print(x_sum_loop([2, 3, 6], 5))  # 0
    print(x_sum_loop([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    :param nums: list of integers
    :param x: number indicating every which num to add to sum
    :return: sum of every x'th number in the list
    """
    if x == 0:
        return 0
    if x < 0:
        every_xth_negative = nums[x::x]
        return sum(every_xth_negative)
    if x > 0:
        every_xth_positive = nums[x - 1::x]
        return sum(every_xth_positive)


def x_sum_recursion(nums: list, x: int) -> int:
    """
    Given a list of integers and a number called x recursively return sum of every x'th number in the list.

    In this task "indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output should be -6 (3 + -9).

    X can also be negative, in that case indexing starts from the end of the list, see examples below.

    If x = 0, the sum should be 0 as well.

    print(x_sum_recursion([], 3))  # 0
    print(x_sum_recursion([2, 5, 6, 0, 15, 5], 3))  # 11
    print(x_sum_recursion([0, 5, 6, -5, -9, 3], 1))  # 0
    print(x_sum_recursion([43, 90, 115, 500], -2))  # 158
    print(x_sum_recursion([1, 2], -9))  # 0
    print(x_sum_recursion([2, 3, 6], 5))  # 0
    print(x_sum_recursion([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    :param nums: list of integers
    :param x: number indicating every which num to add to sum
    :return: sum of every x'th number in the list
    """
    if len(nums) < x or x == 0:
        return 0
    if x < 0:
        return x_sum_recursion(nums[::-1], -x)
    else:
        return nums[x - 1] + x_sum_recursion(nums[x:], x)


def sum_squares(nested_list):
    """
    Write a function that sums squares of numbers in list.

    That list may contain additional lists.
    (Hint use the type() or isinstance() function)

    sum_squares([1, 2, 3]) -> 14
    sum_squares([[1, 2], 3]) -> sum_squares([1, 2]) + 9 -> 1 + 4 + 9 -> 14
    sum_squares([[[[[[[[[2]]]]]]]]]) -> 4

    :param nested_list: list of lists of lists of lists of lists ... and ints
    :return: sum of squares
    """
    return summ(_flatten_list(nested_list))


def _flatten_list(nl):
    """Flatten input list."""
    if not bool(nl):
        return nl
    if isinstance(nl[0], list):
        return _flatten_list(nl[0]) + _flatten_list(nl[1:])
    return nl[:1] + _flatten_list(nl[1:])

    # flattened_input = _flatten_list(nested_list)


def summ(flattened_input):
    """Sum up inside of list."""
    if len(flattened_input) == 0:
        return 0
    else:
        return flattened_input[0] ** 2 + summ(flattened_input[1:])


def count_strings(data: list, pos=None, result: dict = None) -> dict:
    """
    Count strings in list.

    You are given a list of strings and lists, which may also contain strings and lists etc. Your job is to
    collect these strings into a dict, where key would be the string and value the amount of occurrences of that string
    in these lists.

    print(count_strings([[], ["J", "*", "W", "f"], ["j", "g", "*"], ["j", "8", "5", "6", "*"], ["*", "*", "A", "8"]]))
    # {'J': 1, '*': 5, 'W': 1, 'f': 1, 'j': 2, 'g': 1, '8': 2, '5': 1, '6': 1, 'A': 1}
    print(count_strings([[], [], [], [], ["h", "h", "m"], [], ["m", "m", "M", "m"]]))  # {'h': 2, 'm': 4, 'M': 1}
    print(count_strings([]))  # {}
    print(count_strings([['a'], 'b', ['a', ['b']]]))  # {'a': 2, 'b': 2}

    :param data: given list of lists
    :param pos: figure out how to use it
    :param result: figure out how to use it
    :return: dict of given symbols and their count
    """
    if result is None:
        result = {}
    if pos is None:
        pos = 0
    if pos < len(data):
        if isinstance(data[pos], str):
            result[data[pos]] = result.get(data[pos], 0) + 1
        elif isinstance(data[pos], list):
            count_strings(data[pos], 0, result)
        count_strings(data, pos + 1, result)
    return result
