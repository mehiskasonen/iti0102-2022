"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    if all_cars == "":
        return []
    split_car_list = all_cars.split(",")
    return split_car_list


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    split_car_list = list_of_cars(all_cars)
    every_mark = []

    for car in split_car_list:
        car_make = car.split()[0]
        if car_make not in every_mark:
            every_mark.append(car_make)
    return every_mark


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    if all_cars == "":
        return []

    split_car_list = all_cars.split(",")
    every_mark = []
    for car in split_car_list:
        first_word = car.split(" ", 1)[1]
        if first_word not in every_mark:
            every_mark.append(first_word)
    return every_mark


def search_by_make(all_cars: str, search_by: str) -> list:
    """
    Return list of cars (make and model).

    :param all_cars:
    :param search_by:
    :return:
    """
    result_list = []
    search_string = all_cars.split(",")
    for element in search_string:
        car = element.split(" ", 1)
        if search_by.upper() in car[0].upper():
            result_list.append(element)

    return result_list


def search_by_model(all_cars: str, search_by: str) -> list:
    """
    Return list of cars (make and model).

    :param all_cars:
    :param search_by:
    :return:
    """
    result_list = []
    search_string = all_cars.split(",")
    for element in search_string:
        car = element.split()
        for model in car[1:]:
            print(model)
            if search_by.upper() == model.upper():
                result_list.append(element)
    return result_list


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).
    No duplicate makes or models should be in the output.
    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5"

    =>

    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]

    :param all_cars:
    :return:
    """
    result_list = []
    if all_cars == "":
        return []

    car_list = list_of_cars(all_cars)
    structured_list_make = car_makes(all_cars)

    for i in structured_list_make:
        result_list.append([i, []])

    for i in result_list:
        for a in car_list:
            entry = a.split(" ", 1)
            car_make = entry[0]
            car_model = entry[1]
            if i[0] == car_make and car_model not in i[1]:
                i[1].append(car_model)

    return result_list


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    ['Audi', ['A6', 'A4'], 'BMW', ['A']]

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]

    :param car_list:
    :param all_cars:
    :return:
    """
    if not all_cars:
        return car_list

    if not car_list:
        result = car_make_and_models(all_cars)
        return result
    if not all_cars and not car_list:
        return []
    else:
        car_list_string = car_list_as_string(car_list)
        total_string = car_list_string + ',' + all_cars
        result = car_make_and_models(total_string)
        return result


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.

    :param all_cars:
    :return:
    """
    result_list = []
    quantity = []

    all_car_list = list_of_cars(all_cars)
    structured_list_make = car_makes(all_cars)

    for element in all_car_list:
        make = element.split(" ")
        result_list.append(make[0])

    for car in structured_list_make:
        count = result_list.count(car)
        quantity.append(count)

    return list(zip(structured_list_make, quantity))


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    input_into_string = ""
    sub_string = ""

    for element in cars:
        for item in element:
            if type(item) == str:
                sub_string = item + ' '
            if type(item) is list:
                for one_model in item:
                    input_into_string += sub_string + one_model + ','
    result_string = input_into_string.rstrip(',')

    return result_string


if __name__ == '__main__':
    # print(list_of_cars("Audi A4,Skoda Superb,Audi A4,BMW A B C"))  # ["Audi A4", "Skoda Superb",
    # "Audi A4", "BMW A B C"]
    # print(list_of_cars(""))   # []
    # print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5,BMW A B C"))
    # ['Audi', 'Skoda', 'BMW', 'Seat']

    # print(car_makes( "Mazda 6,Mazda 6,Mazda 6,Mazda 6")) # ['Mazda']

    # print(car_makes(""))  # []

    # print(car_models("Audi A4,Skoda Superb,Audi A4,Audi A6,BMW A B C"))  # ["A4", "Superb", "A6", "A B C"]

    # print(search_by_make("Audi A4,Audi a4,BMW x5,", "Audi A4"))  # ["Audi A4", "Audi a4"]  []

    # print(search_by_model("Audi A4,Audi a4 2021,Audi A40,Skoda Super Lux", "A4"))
    # search by A4 or a4 - ["Audi A4", "Audi a4 2021"]
    # print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a4"))  # search by A4 or a4 - ["Audi A4", "Audi a4 2021"]
    # print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "202"))  # search by "202" - []
    # print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a4 2021"))  #  - []
    # print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a"))  # - []
    # print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "Audi"))  #  - []
    # print(search_by_model("Audi A4,Audi a4 2021,Audi A40,Skoda Super Lux", "2021"))  # - ["Audi a4 2021"]
    # print(car_make_and_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,
    # BMW A B C"))
    # [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'A B C']], ['Seat', ['Leon']]]
    # print(car_make_and_models("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [['Mazda', ['6']]]
    # print(car_make_and_models(""))  # []

    print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]], "Audi A6,BMW A B C,Audi A4"))
    # [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    print(add_cars([], "Audi A6,BMW A B C,Audi A4"))
    print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]], ""))
    print(add_cars([], ""))
    # print(number_of_cars("Audi A4,Skoda Superb,Seat Leon,Audi A6"))  # [('Audi', 2), ('Skoda', 1), ('Seat', 1)]
    # print(number_of_cars("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [('Mazda', 4)]

    # print(number_of_cars(""))  # []

    # print(car_list_as_string([['Audi', ['A4']], ['Skoda', ['Superb']]]))  # "Audi A4,Skoda Superb"
