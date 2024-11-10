"""Hobbies but OOP."""


class Person:
    """
    Class for people.

    Every person has
    a first name,
    last name and
    list of hobbies.
    """

    def __init__(self, first_name: str, last_name: str, hobbies: list):
        """
        Person constructor.

        :param first_name: first name of the person
        :param last_name: last name of the person
        :param hobbies: list of hobbies
        """
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies

    @property
    def full_name(self) -> str:
        """Get person's full name.

        Combination of first and last name.

        :param self: object
        :return string: first + last name of object
        """
        return str(self.first_name) + str(self.last_name)

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people that have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    filtered_people = list(filter(lambda s: hobby in s.hobbies, people_list))
    return filtered_people


def sort_by_most_hobbies(people_list: list) -> list:
    """Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_alphabetically = sorted(people_list, key=lambda p: sorted(p.full_name))
    return sorted(sorted_alphabetically, key=lambda s: len(s.hobbies), reverse=True)


def sort_by_least_hobbies(people_list: list) -> list:
    """Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_alphabetically = sorted(people_list, key=lambda p: sorted(p.full_name))
    return sorted(sorted_alphabetically, key=lambda s: len(s.hobbies), reverse=False)


def sort_people_and_hobbies(people_list: list) -> list:
    """Return a list of people but sorted alphabetically by their full name.

    Also sort their list of hobbies alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    for item in people_list:
        item.hobbies = sorted(item.hobbies)
    sorted_by_first_name = sorted(people_list, key=lambda p: p.first_name)

    return sorted_by_first_name


if __name__ == '__main__':
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    # person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    people = [person1, person2]

    # print(filter_by_hobby(people, "space"))  # -> [JeffBezos, ElonMusk]

    # print(sort_by_most_hobbies(people))  # -> [JeffBezos, ElonMusk, MariKukk]

    # print(sort_by_least_hobbies(people))   # -> [ElonMusk, MariKukk, JeffBezos]

    # print(sorted_by_first_name[2].hobbies)
    print(sort_people_and_hobbies(people))  # -> [ElonMusk, JeffBezos, MariKukk]
    print(person1.hobbies)  # -> ['biking', 'dancing', 'programming']
