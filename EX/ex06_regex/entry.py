"""Regex, I think."""
import re


class Entry:
    """Entry class."""

    def __init__(self, first_name: str, last_name: str, id_code: str, phone_number: str, date_of_birth: str,
                 address: str):
        """Init."""
        self.first_name = first_name
        self.last_name = last_name
        self.id_code = id_code
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.address = address

    def format_date(self):
        """
        Return the date in the following format: 'Day: {day}, Month: {month}, Year: {year}'.

        Just for fun, no points gained or lost from this.

        Example: 'Day: 06, Month: 11, Year: 1995'
        If the object doesn't have date of birth given, return None.
        :return:
        """
        return self.date_of_birth

    def __repr__(self) -> str:
        """Object representation."""
        return f"Name: {self.first_name} {self.last_name}\n" \
               f"ID code: {self.id_code}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"Date of birth: {self.format_date()}\n" \
               f"Address: {self.address}"

    def __eq__(self, other) -> bool:
        """
        Compare two entries.

        This method is perfect. Don't touch it.
        """
        return self.first_name == other.first_name and self.last_name == other.last_name and \
            self.id_code == other.id_code and self.phone_number == other.phone_number and \
            self.date_of_birth == other.date_of_birth and self.address == other.address


def parse(row: str) -> Entry:
    """
    Parse data from input string.

    :param row: String representation of the data.
    :return: Entry object with filled values
    """
    string = ""
    match = re.search(r"([A-Z][a-z]+)?([A-Z][a-z]+)?(\d{11})(\s)?(\+\d{3}\s)?(\d{7,8})?(\+\d{11})?(\d{8})?(\d{2}.\d{2}.\d{4})?([A-ZÜÕÖÄa-züõöä ]+[0-9-,A-ZÜÕÖÄa-züõöä]+)?", row)
    first_name = match.group(1)
    last_name = match.group(2)
    id_code = match.group(3)
    phone_number_to_edit = match.group(5, 6, 7)

    if match.group(7) is None:
        if match.group(5) is None:
            string = match.group(6)
        if match.group(5) and match.group(6) is None:
            string = None
        else:
            try:
                for item in phone_number_to_edit[:-1]:
                    string += item
            except TypeError:
                string = match.group(6)
    else:
        string = match.group(7)[:4] + match.group(7)[4:]

    phone_number = string
    date_of_birth = match.group(9)
    address = match.group(10)

    print(Entry)
    return Entry(first_name, last_name, id_code, phone_number, date_of_birth, address)


if __name__ == '__main__':
    print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: None None
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: None
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: None
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann39712047623+372 5688736402-12-1998'))
    """Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: None
    """
    print(parse('HeinoPlekk69712047623 5688736412-09-2020Tartu mnt 183,Tallinn,16881,Eesti'))
    """Name: Heino Plekk
    ID code: 69712047623
    Phone number: 56887364
    Date of birth: Day: 12, Month: 09, Year: 2020
    Address: Tartu mnt 183,Tallinn,16881,Eesti
    """
    print()
    print(parse('PriitTagumik59712047623+3725688736412-12-1978Oja 18-2,Pärnumaa,Are'))
    """Name: Priit Tagumik
    ID code: 59712047623
    Phone number: +37256887364
    Date of birth: 12-12-1978
    Address: Oja 18-2,Pärnumaa,Are
    """
