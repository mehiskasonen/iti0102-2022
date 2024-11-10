"""Hobbies."""


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


if __name__ == '__main__':
    data = """Jack:crafting\nPeter:hiking\nPeter:boardgames\nPeter:movies\nPeter:computers\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(data)
    print(dic)
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

    # sort_result = sort_names_and_hobbies(data)
    # if the condition after assert is False, error will be thrown
    # assert isinstance(sort_result, tuple)
    # assert len(sort_result) == 10
    # assert sort_result[0][0] == 'Alfred'
    # assert len(sort_result[0][1]) == 7
    # assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    # print(find_two_people_with_most_common_hobbies(data))
    # print("sorting works!")

    # print(sort_names_and_hobbies(sample_data))"""
