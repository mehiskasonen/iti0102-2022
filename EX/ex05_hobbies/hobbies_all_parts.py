"""Hobbies."""
import itertools


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    hobbies_dict = {}
    split_data = list(subString.split(":") for subString in data.split("\n"))
    # print(split_data)
    for element in split_data:
        key = element[0]
        value = element[1]

        if key in hobbies_dict.keys() and value in hobbies_dict.values():
            continue
        if key in hobbies_dict.keys() and value not in hobbies_dict.values():
            hobbies_dict[key].append(value)
        else:
            hobbies_dict[key] = [value]

    for name, value in hobbies_dict.items():
        a = set(value)
        b = list(sorted(a))
        hobbies_dict[name] = b

    return hobbies_dict


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "...f", "...a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    result_dict = {}
    for name, hobby in dic.items():
        hob = sorted(hobby)
        result_dict[name] = hob

    return result_dict


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    result_dict = {}
    split_data = list(subString.split(":") for subString in data.split("\n"))
    for element in split_data:
        key = element[1]
        value = element[0]

        if key in result_dict.keys() and value in result_dict.values():
            continue
        if key in result_dict.keys() and value not in result_dict.values():
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]

    for name, value in result_dict.items():
        a = set(value)
        b = list(sorted(a))
        result_dict[name] = b

    return result_dict


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    dic = create_dictionary(data)
    sorted_dic = sort_dictionary(dic)

    people_most_hobbies = {key: (len(value)) for (key, value) in sorted_dic.items()}
    max_value = max(people_most_hobbies.values())
    people_with_most_hobbies = [k for k, v in people_most_hobbies.items() if v == max_value]

    return sorted(people_with_most_hobbies)


def find_people_with_least_hobbies(data: str) -> list:
    """
    Find the people who have least hobbies.

    :param data: given string from database
    :return: list of people with least hobbies. Sorted alphabetically.
    """
    people_with_least_hobbies = []
    dic = create_dictionary(data)
    sorted_hobbies = sort_dictionary(dic)
    people_with_least_hobbies.append(min(sorted_hobbies, key=lambda hobbies: len(set(sorted_hobbies[hobbies]))))
    return people_with_least_hobbies


def find_most_popular_hobbies(data: str) -> list:
    """
    Find the most popular hobbies.

    :param data: given string from database
    :return: list of most popular hobbies. Sorted alphabetically.
    """
    result = []
    popular_hobbies = []
    data = create_dictionary_with_hobbies(data)  # popular_hobbies returns {'hobby1': [name1, name2, name3]}
    for hobby, name in data.items():
        result.append(len(name))
        max_res = max(result)
        if len(name) == max_res:
            popular_hobbies.append(hobby)
    return popular_hobbies


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    a = create_dictionary_with_hobbies(data)
    least_popular_numbers = {key: (len(value)) for (key, value) in a.items()}
    min_value = min(least_popular_numbers.values())
    least_popular_hobbies = [k for k, v in least_popular_numbers.items() if v == min_value]

    return sorted(least_popular_hobbies)


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    dic = create_dictionary(data)
    sorted_dic_hobbies = sort_dictionary(dic)

    d = {i: sorted_dic_hobbies[i] for i in sorted(list(sorted_dic_hobbies.keys()), reverse=False)}

    nested_tuple = [(k, tuple(v)) for k, v in d.items()]
    return tuple(nested_tuple)


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    """
    Find all the different people with certain hobbies.

    It is recommended to use set here.
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    dic = create_dictionary(data)
    sorted_dic_hobbies = sort_dictionary(dic)

    result_set = set()

    for name, hobby in sorted_dic_hobbies.items():
        for element in hobbies:
            if element in hobby:
                result_set.add(name)

    return result_set


def find_two_people_with_most_common_hobbies(data: str) -> tuple or None:
    """
    Find a pair of people who have the highest ratio of common to different hobbies.

    Common hobbies are the ones that both people have.
    Different hobbies are the ones that only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies; ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair is returned.

    The exception is when multiple pairs share all of their hobbies, in which case the pair with
    the most shared hobbies is returned.

    A pair with only common hobbies is better than any other pair with at least 1 different hobby.

    Example:
    John has:
        running
        walking
    Mary has:
        running
        walking
    Nora has:
        running
    Oprah has:
        running
    Albert has:
        tennis
        basketball
        football
    Xena has:
        tennis
        basketball
        football
        dancing

    John and Mary have 2 common, 0 different. Ratio 2/0
    Nora and Mary (also Nora and John, Oprah and John, Oprah and Mary) have 1 common, 1 different. Ratio 1/1
    Nora and Oprah have 1 common, 0 different. Ratio 1/0
    Albert and Xena have 3 common, 1 different. Ratio 3/1

    In that case the best pair is John and Mary. If the number of different hobbies is 0,
    then this is better than any pair with at least 1 different hobby.
    Out of the pairs with 0 different hobbies, the one with the highest number
    of common hobbies is the best.
    If there are multiple pairs with the highes number of common hobbies,
    any pair (and in any order) is accepted.

    If there are less than 2 people in the input, return None.
    """
    dictionary = create_dictionary(data)
    sorted_dic = sort_dictionary(dictionary)
    if len(sorted_dic) < 2:
        return None

    set_dic = {k: set(v) for k, v in sorted_dic.items()}
    # {'John': {'walking', 'running'}, 'Mary': {'dancing', 'running'}, 'Nora': {'singing', 'running', 'dancing'}}
    people = [t for t in itertools.combinations(sorted_dic.keys(), 2)]
    # [('John', 'Mary'), ('John', 'Nora'), ('Mary', 'Nora')]
    hh = {(p1, p2): (len(set_dic[p1] & set_dic[p2]), len(set_dic[p1] ^ set_dic[p2])) for p1, p2 in people}
    # {('John', 'Mary'): (1, 2), ('John', 'Nora'): (1, 3), ('Mary', 'Nora'): (2, 1)}

    def most_shared(key):
        try:
            ratio = hh[key][0] / hh[key][1]
        except ZeroDivisionError:
            ratio = float('inf')
        return ratio, hh[key][0]

    res = max(hh, key=most_shared)
    if len(res) < 2:
        return None
    return res


if __name__ == '__main__':
    data = """Jack:crafting\nPeter:hiking\nPeter:boardgames\nPeter:movies\nPeter:computers\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(data)
    # print(dic)
    # print(sort_dictionary(dic))
    # print(create_dictionary_with_hobbies(data))
    # print(sort_dictionary({'b': ['d', 'a'], 'a': ['c', 'f']}))  # {"b":["a", "d"], "a":["c", "f"]}
    # print(sort_dictionary({"": ["f", "d", "a"]}))  # => {"": ["a", "d", "f"]}
    # print(sort_dictionary({"b": ["e", "...f", "...b", "...a", "a"], "a": ["c", "f"]}))
    # => {"b":["a", "d"], "a":["c", "f"]}
    # print(sort_dictionary({'a': ['a', 'b', 'c', 'd', 'e', 'f', ...], 'b': ['a', 'b', ...', 'f', ...],
    # # 'd': ['a', 'b', 'c', 'd', 'e', 'f', ...], ...}) # {'a': ['a', 'a', 'a', 'b', 'b', 'c', ...],
    # # 'b': ['a', 'a', ...', 'b', ...], 'd': ['a', 'a', 'a', 'b', 'b', 'b', ...], ...}))
    # print(sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}))
    # {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    # print("shopping" in dic["Wendy"])  # -> True
    # print("fitness" in dic["Sophie"])  # -> False
    # print("gaming" in dic["Peter"])  # -> True
    # print(find_people_with_most_hobbies(data))  # -> ['Jack']
    # print(len(dic["Jack"]))  # ->  12
    # print(len(dic["Carmen"]))  # -> 10
    # print(find_people_with_least_hobbies(data))  # -> ['Molly']
    # print(len(dic["Molly"]))  # -> 5
    # print(len(dic["Sophie"]))  # -> 7
    # print(find_most_popular_hobbies(sample_data))  # -> ['football', 'gaming', 'sport']
    # print(find_least_popular_hobbies(data))  # -> ['dance', 'flowers', 'puzzles', 'tennis']
    # print(sort_dictionary(dic))
    # print(find_people_with_hobbies(data, ["running", "dancing", "fitness"]))

    sort_result = sort_names_and_hobbies(data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    print(find_two_people_with_most_common_hobbies(data))
    print("sorting works!")

    # print(sort_names_and_hobbies(sample_data))"""
