"""Reading and writing to and from files."""

import csv
from csv import DictReader
from csv import DictWriter


def read_file_contents(filename: str) -> str:
    """Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read()
    return data


def read_file_contents_to_list(filename: str) -> list:
    r"""Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    result = []
    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            result.append(line.strip("\n"))
        return result


def read_csv_file(filename: str) -> list:
    """Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    result = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            result.append(row)
        return result


def write_contents_to_file(filename: str, contents: str) -> None:
    """Write contents to file.

    If the file does not exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    f = open(filename, "w", encoding="utf-8")
    f.write(contents)
    f.close()


def write_lines_to_file(filename: str, lines: list) -> None:
    """Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w", encoding='utf-8', newline="\n") as fout:
        fout.write("\n".join(lines))
        # for line in lines:
        # fout.write(line + "\n")
    fout.close()
    # write_lines_to_file("file.txt", ["hello", "world"])


def write_csv_file(filename: str, data: list) -> None:
    """Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in data:
            writer.writerow(row)
        csvfile.close()


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    result = [["name", "town", "date"]]
    dates = []
    towns = []
    towns2 = []

    input_dates = read_file_contents_to_list(dates_filename)
    input_towns = read_file_contents_to_list(towns_filename)

    for element in input_dates:
        b = element.split(":")
        dates.append(b)
    for element in input_towns:
        b = element.split(":")
        towns.append(b)

    for line in towns:
        towns2.append([line[0], line[1], '-'])
    for line in dates:
        result.append([line[0], "-", line[1]])

    for name_town_date in result:
        for name_town in towns2:
            print(name_town)
            if name_town_date[0] in name_town:
                name_town_date[1] = name_town[1]
                towns2.remove(name_town)

    for remaining in towns2:
        result.append(remaining)

    write_csv_file(csv_output_filename, result)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """Read csv file into list of dictionaries.

    Header line will be used for dict keys.
    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example(s):

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    result = []
    with open(filename, newline='') as csvfile:
        csv_reader = DictReader(csvfile, delimiter=',')
        for row in csv_reader:
            # print(row)
            result.append(row)
        return result


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    with open(filename, "w", newline='') as csvfile:
        fieldnames = []
        for dic in data:
            for key in dic:
                if key not in fieldnames:
                    fieldnames.append(key)
        if len(data) != 0:
            csv_writer = DictWriter(csvfile, delimiter=",", fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str, **col_conversions) -> list:
    """Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    pass
    """
    res = read_csv_file_into_list_of_dicts(filename)
    print(res)
    for k, v in res:
    """


if __name__ == '__main__':
    # print(read_file_contents("towns"))
    # print(read_csv_file_into_list_of_dicts("input"))
    # print(merge_dates_and_towns_into_csv("dates", "towns", "output"))
    # print(read_csv_file_into_list_of_dicts_different_delimiter("dates"))
    # print(read_csv_file_into_list_of_dicts("input.csv"))
    # print(write_list_of_dicts_to_csv_file("output.csv", [{"name": "john", "age": "23"}, {"name": "mary", "age": "44"}]))
    # print(write_list_of_dicts_to_csv_file("output.csv",     [{"name": "john", "age": "12"}, {"name": "mary", "town": "London"}]))
    # print(write_list_of_dicts_to_csv_file("output.csv", []))

    # [{"name": "john", "age": "12"}, {"name": "mary", "town": "London"}]))
    read_csv_file_into_list_of_dicts_using_datatypes("input.csv")
