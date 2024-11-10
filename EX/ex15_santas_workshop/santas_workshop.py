"""EX15 - Santa's Workshop."""
import csv


class Child:
    """Child class."""

    def __init__(self, name: str, country: str, is_nice: bool):
        """Child constructor."""
        self.name = name
        self.country = country
        self.is_nice = is_nice
        self.wishlist = []

    def __repr__(self):
        """Child representation for development purposes."""
        return f"Child({self.name}, {self.country}, {self.is_nice}, {self.wishlist})"


class Gift:
    """Gift class."""

    def __init__(self, name: str, child: Child):
        """Gift constructor."""
        self.name = name
        self.child = child
        self.production_time = 0
        self.material_cost = 0
        self.weight_in_grams = 0
        self.get_production_data()


class Factory:
    """Factory class.

    Process incoming data from .csv files, produces gifts as per configuration and ships them out in sleighs.
    """

    def __init__(self):
        """Factory constructor."""
        self._children = []
        self.produced_gifts = []
        self.production_metrics = {
            "material_spent": 0.0,
            "time_spent": 0.0,
            "total_weight_of_gifts": 0
        }
        self.loaded_sleighs = []


def read_children_data(self, filename: str, is_nice):
    """Create instance of Child from each entry in input file and add them to self.children."""
    """If Child already exists in self.children, do not create a new Child."""
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            name = row[0]
            country = row[1].strip()
            if self.check_if_child_already_in_database(name) is not True:
                child = Child(name, country, is_nice)
                self.children.append(child)

def check_if_child_exists(self, name, country):


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make child objects and add the children into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    mid_list = []
    clients = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            mid_list.append(row)
    for element in mid_list:
        clients += [Client(name=element[0], bank=element[1], account_age=int(element[2]),
                           starting_amount=int(element[3]), current_amount=int(element[4]))]
    return clients