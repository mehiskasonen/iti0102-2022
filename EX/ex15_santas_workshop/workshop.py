"""EX15 - Santa's Workshop."""

import csv
import requests
import urllib
import operator
import ast
import base64
from cypher import encode


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


class InformationOffice:
    """Information office class."""

    def __init__(self):


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

    def get_production_data(self):
        """Get production data on Gift."""
        request_parameters = urllib.parse.urlencode({"name": self.name})
        url = f"http://api.game-scheduler.com:8089/gift?{request_parameters}"
        request = requests.get(url)
        data = request.json()
        try:
            self.production_time = data["production_time"]
            self.material_cost = data["material_cost"]
            self.weight_in_grams = data["weight_in_grams"]
        except KeyError:
            raise KeyError(f"Gift {self.name} not found in database.")


class Sleigh:
    """Sleigh class."""

    def __init__(self, destination: str, sleigh_index: int):
        """Sleigh constructor."""
        self.destination = destination
        self.sleigh_index = sleigh_index
        self.cargo = []
        self._remaining_weight = 50000

    @property
    def remaining_weight(self):
        """Get Sleigh.remaining_weight."""
        return self._remaining_weight

    @remaining_weight.setter
    def remaining_weight(self, value):
        """Set Sleigh.remaining_weight."""
        self._remaining_weight = value

    def write_manifest(self):
        """Write the cargo manifest of the Sleigh."""
        children = {}
        for gift in self.cargo:
            if gift.child.name not in children:
                children[gift.child.name] = [gift]
            else:
                children[gift.child.name].append(gift)
        f = open(f"manifest_{self.destination.lower()}_{self.sleigh_index}.txt", "w")
        header_1 = r"                        DELIVERY ORDER" + "\n"
        header_2 = r"                                                          _v" + "\n"
        header_3 = r"                                                     __* (__)" + "\n"
        header_4 = r"             ff     ff     ff     ff                {\/ (_(__).-." + "\n"
        header_5 = r"      ff    <_\__, <_\__, <_\__, <_\__,      __,~~.(`>|-(___)/ ,_)" + "\n"
        header_6 = r"""    o<_\__,  (_ ff ~(_ ff ~(_ ff ~(_ ff~~~~~@ )\/_;-"``     |""" + "\n"
        header_7 = r"      (___)~~//<_\__, <_\__, <_\__, <_\__,    | \__________/|" + "\n"
        header_8 = r"      // >>     (___)~~(___)~~(___)~~(___)~~~~\\_/_______\_//" + "\n"
        header_9 = r"                // >>  // >>  // >>  // >>     `'---------'`" + "\n"
        f.write(header_1 + header_2 + header_3 + header_4 + header_5 + header_6 + header_7 + header_8 + header_9)
        sender_line = "\nFROM: NORTH POLE CHRISTMAS CHEER INCORPORATED\n"
        f.write(sender_line)
        country_line = f"TO: {self.destination.capitalize()}\n\n"
        f.write(country_line)
        table_left_side = "//" + 11 * "="
        table_right_side = 18 * "=" + "\\\\\n"
        table_centre = "[]" + 42 * "=" + "[]"
        table_start_line = table_left_side + table_centre + table_right_side
        f.write(table_start_line)
        first_row = "||" + "Name".center(11) + "|"
        second_row = "|" + "Gifts".center(42) + "|"
        third_row = "|" + "Total Weight (kg)".center(18) + "||\n"
        content_line = first_row + second_row + third_row
        f.write(content_line)
        for child in children.keys():
            gift_names = ""
            gifts_total_weight = 0
            for gift in children[child]:
                gift_names += f"{gift.name}, "
                gifts_total_weight += gift.weight_in_grams
            gift_names = gift_names[:-2]
            gifts_total_weight = gifts_total_weight / 1000
            first_row = "||" + child + (" " * (11 - len(child))) + "|"
            third_row = "|" + (" " * (18 - len(str(gifts_total_weight)))) + str(gifts_total_weight) + "||\n"
            if len(gift_names) > 42:
                second_row = "|" + gift_names[:42] + "|"
                gift_names = gift_names[42:]
                content_line = first_row + second_row + third_row
                f.write(content_line)
                first_row = "||" + (" " * 11) + "|"
                third_row = "|" + (" " * 18) + "||\n"
                while len(gift_names) > 42:
                    second_row = "|" + gift_names[:42] + "|"
                    gift_names = gift_names[42:]
                    content_line = first_row + second_row + third_row
                    f.write(content_line)
            second_row = "|" + gift_names + (" " * (42 - len(gift_names))) + "|"
            content_line = first_row + second_row + third_row
            f.write(content_line)
        table_end_left_side = "\\\\" + 11 * "="
        table_end_right_side = 18 * "=" + "//\n"
        table_end_line = table_end_left_side + table_centre + table_end_right_side
        f.write(table_end_line)
        f.close()


class PostOffice:
    """Post Office class for processing incoming mail."""

    def __init__(self):
        """PostOffice constructor."""
        self.letters = []
        self.normal_letters = []
        self.letters_in_caesar_cipher = []
        self.letters_in_base64 = []
        self.wishes = []

    def get_letters(self, times: int):
        """Read the incoming letters for the prescribed number of times."""
        for i in range(times):
            response = urllib.request.urlopen("http://api.game-scheduler.com:8089/letter")
            letter = response.read()
            letter = letter.decode("UTF-8")
            letter_as_dict = ast.literal_eval(letter)
            self.letters.append(letter_as_dict["letter"])

    def categorize_letters_by_type(self):
        """Run self.identify_letter_type() on all letters."""
        for letter in self.letters:
            self.identify_letter_type(letter)

    def identify_letter_type(self, letter):
        """Identify whether the letter is normal, ciphered or encoded into base64."""
        """If the letter is ciphered or encoded into base64, run corresponding code."""

        keywords = ["Dear", "Hi", "Hello", "Welcome", "Santa", "Greetings"]
        decoding_required = True
        for word in keywords:
            if word in letter:
                self.normal_letters.append(letter)
                decoding_required = False
                break
        if decoding_required is True:
            if letter.find(",") != -1:
                self.check_caesar_chipher(letter)
            else:
                self.check_base64(letter)

    def find_wishes(self):
        """Identify whether the letter includes gift wishes and add them to self.wishes if yes."""
        keywords = ["I want", "I wish for", "wishlist", "i want", "i wish for"]
        for letter in self.normal_letters + self.letters_in_base64 + self.letters_in_caesar_cipher:
            for word in keywords:
                start_of_wishlist = letter.find(word)
                if start_of_wishlist != -1:
                    cropped_letter = letter[start_of_wishlist + len(word) + 1:]
                    end_of_wishlist = cropped_letter.find(".")
                    wishlist = cropped_letter[:end_of_wishlist]
                    child_data = cropped_letter.split("\n")[-1].split(", ")
                    wishlist_as_dict = {
                        "name": child_data[0],
                        "country": child_data[1],
                        "wishes": wishlist
                    }
                    self.wishes.append(wishlist_as_dict)

    def check_caesar_chipher(self, letter):
        """Run cypher.encode() with all possible key variations in Caesar cipher."""
        """If a key proves to be a match, add the encoded letter to self.letters_in_caesar_cipher."""
        for x in range(0, 26):
            encrypted_message = [encode(letter[0:20].lower(), x), x]
            keywords = ["hi,", "hi santa", "hello", "welcome", "santa", "greetings"]
            for word in keywords:
                index_found = encrypted_message[0].find(word)
                if index_found != -1:
                    self.letters_in_caesar_cipher.append((encode(letter.lower(), x)))

    def check_base64(self, letter):
        """Dencode letter from base64 and add to self.letters_in_base64."""
        base64_in_bytes = base64.b64decode(letter)
        decoded_letter = base64_in_bytes.decode("utf-8")
        self.letters_in_base64.append(decoded_letter)

    def write_post_office_data_to_files(self):
        """Write the data in self.wishes to two separate csv files: first file for children, second for their wishlist."""
        wishlist_file = open("post_office_wishlist.csv", "w")
        children_file = open("post_office_nice_list.csv", "w")
        for wishlist in self.wishes:
            children_file.write(wishlist["name"] + ", " + wishlist["country"] + "\n")
            wishlist_file.write(wishlist["name"] + ", " + wishlist["wishes"] + "\n")
        wishlist_file.close()
        children_file.close()


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

    @property
    def children(self):
        """Get self.children."""
        return self._children

    @children.setter
    def children(self, value):
        """Set self.children."""
        self._children = value

    def read_children_data(self, file, is_nice):
        """Create instance of Child from each entry in input file and add them to self.children."""
        """If Child already exists in self.children, do not create a new Child."""
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                name = row[0]
                country = row[1].strip()
                if self.check_if_child_already_in_database(name) is not True:
                    child = Child(name, country, is_nice)
                    self.children.append(child)

    def create_gifts_from_wishlist(self, file):
        """Create instance of Gift for each gift in the wishlist linked to the correct child."""
        """If the wishlist of a Child has already been read, do not create Gift."""
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                child_name = row[0]
                wishes = row[1:]
                child = self.check_if_child_wishlist_is_already_read(child_name)
                if child is not False:
                    for wish in wishes:
                        wish = wish.strip()
                        gift = Gift(wish, child)
                        child.wishlist.append(gift)

    def check_if_child_already_in_database(self, child_name):
        """Check if Child with that name already exists in database."""
        for child in self.children:
            if child.name == child_name:
                return True

    def check_if_child_wishlist_is_already_read(self, child_name):
        """Check if Child with that name has already been given gifts to their wishlist."""
        for child in self.children:
            if child.name == child_name and len(child.wishlist) == 0:
                return child
        return False

    def produce_one_gift_per_child(self):
        """Produce a single Gift for all self.children as per configuraiton and calculate production metrics."""
        for child in self.children:
            child.wishlist.sort(key=operator.attrgetter("weight_in_grams"), reverse=True)
            if child.is_nice is True and len(child.wishlist) > 0:
                produced_gift = child.wishlist.pop(0)
                self.produced_gifts.append(produced_gift)
                self.production_metrics["material_spent"] += produced_gift.material_cost
                self.production_metrics["material_spent"] = round(self.production_metrics["material_spent"], 2)
                self.production_metrics["time_spent"] += produced_gift.production_time
                self.production_metrics["time_spent"] = round(self.production_metrics["time_spent"], 2)
                self.production_metrics["total_weight_of_gifts"] += produced_gift.weight_in_grams

    def produce_gifts(self, threshold, metric="total_weight_of_gifts"):
        """Produce gifts as per the chosen metric."""
        """If the threshold for the metric is reached, stop producing."""
        while self.production_metrics[metric] < threshold:
            metric_before_production = self.production_metrics[metric]
            self.produce_one_gift_per_child()
            metric_after_production = self.production_metrics[metric]
            if metric_before_production == metric_after_production:
                break

    def put_gifts_on_sleighs_per_country(self):
        """Put all gifts belonging to a single country on sleighs."""
        """If the weight limit of Sleigh is reached, make new instance of Sleigh and write the manifest of the previous sleigh."""
        destination = ""
        gifts_to_be_shipped = []
        sleighs = []
        sleigh_index = 1
        for gift in self.produced_gifts:
            if destination == "":
                destination = gift.child.country
            if gift.child.country == destination:
                gifts_to_be_shipped.append(gift)
        new_sleigh = Sleigh(destination, sleigh_index)
        sleigh_index += 1
        sleighs.append(new_sleigh)

        for gift in gifts_to_be_shipped:
            self.produced_gifts.remove(gift)

        while len(gifts_to_be_shipped) > 0:
            if sleighs[-1].remaining_weight - gifts_to_be_shipped[0].weight_in_grams < 0:
                sleighs[-1].write_manifest()
                new_sleigh = Sleigh(destination, sleigh_index)
                sleigh_index += 1
                sleighs.append(new_sleigh)
            gift_put_on_sleigh = gifts_to_be_shipped.pop(0)
            sleighs[-1].cargo.append(gift_put_on_sleigh)
            sleighs[-1].remaining_weight -= gift_put_on_sleigh.weight_in_grams
        self.loaded_sleighs.append(sleighs[-1])
        sleighs[-1].write_manifest()

    def loading_sleighs(self):
        """Create and ship new sleighs until all produced gifts have been delivered."""
        while len(self.produced_gifts) > 0:
            self.put_gifts_on_sleighs_per_country()
