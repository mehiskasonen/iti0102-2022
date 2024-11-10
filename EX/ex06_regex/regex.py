"""Regex, yay."""
import re


def find_words(text: str) -> list:
    """
    Given string text, return all the words in that string.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string to find words from
    :return: list of words found in given string
    """
    return re.findall("[A-ZÜÕÖÄ][a-züõöä]+", text)
# v1.0 [A-Z][a-z]+


def find_words_with_vowels(text: str) -> list:
    """
    Given string text, return all the words in that string that start with a vowel.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string to find words from
    :return: list of words that start with a vowel found in given string
    """
    return re.findall("[AEIOUÕÄÖÜ][a-z]+", text)


def find_sentences(text: str) -> list:
    """
    Given string text, return all sentences in that string.

    A sentence always starts with a capital letter and ends with punctuation (.!?).
    Note that a sentence may also contain all the typical symbols (like commas, colons, numbers, etc.).
    A sentence may also end in multiple punctuation (example: "Wait...").

    Sentences must be found using regex.

    :param text: given string to find sentences from
    :return: list of sentences found in given string
    """
    return re.findall(r"[A-ZÜÕÖÄ0-9][A-ZÖÄÜÕa-zöäüõ0-9-,:;\s]+[.!?]+", text)
# [A-ZÜÕÖÄ][a-züõöä:;.,\s\]+[a-züõöä0-9.:;\-]+[.?!]?
# v1.1  [A-ZÜÕÖÄ]+[a-z]+[.:;\-\s0-9]+[A-ZÜÕÖÄa-züõöä0-9.:;\-\s]+[.?!](?=\s[^a-zA-Z0-9]*)?
# v1.2  [A-ZÜÕÖÄ][a-z]+[,.:;\-\s0-9]+[A-ZÜÕÖÄa-züõöä0-9,.:;\-\s]+[.?!](?=\s[^a-zA-Z0-9]*)?
# [A-Z][a-züõöä\-:;.,\s]+\b[.?!](?=\s[^a-zA-Z0-9]*) vana versioon


def find_words_from_sentence(sentence: str) -> list:
    """
    Given a sentence, return all words in that sentence.

    Here, a word is considered to be a normal word in a sentence,
    that is separated from other words by a whitespace (or commas, etc.).
    Note that numbers are also considered as words here, but commas, etc. are not
    a part of a word.

    Words must be found using regex.

    :param sentence: given sentence to find words from
    :return: list of words found in given sentence
    """
    return re.findall(r"[A-ZÜÕÖÄa-züõöä0-9]+", sentence)
# v1.0 [A-ZÜÕÖÄa-züõöä]+


def find_words_from_sentences_only(text: str) -> list:
    """
    Given string text, return all words in that string that are a part of a sentence in that string.

    A sentence is defined in function find_sentences().
    A word is defined in function find_words_from_sentence().

    :param text: given string to find words from
    :return: list of words found in sentences from given string
    """
    words_from = find_words_from_sentence(str(find_sentences(text)))
    return words_from


def find_years(text: str) -> list:
    """
    Given string text, return a list of all 4-digit numbers (years) in that string.

    Only 4-digit numbers are considered years here.
    If there is a 5-digit number then that is not considered a year,
    nor will it give two years. So you can not split them up.

    Years must be found using regex.

    Hint: use lookbehind and lookahead to check what comes before and after the numbers.

    :param text: given string to find years from
    :return: list of years (integers) found in given string
    """
    years = re.findall(r"(?<![0-9])\d{4}(?![0-9])", text)
    result = []
    for element in years:
        result.append(int(element))

    return result

# v1.0  (?<![0-9])\d{4}(?=[a-z])
# (?<![0-9,.:\-])(?=[0-9a-z,.:-])\d{4}


def find_phone_numbers(text: str) -> dict:
    """
    Given string text, return a dictionary of all the phone numbers in that text.

    Phone number might be preceded by area code. Area code is a combination of plus sign and three numbers.
    The phone number itself is a combination of 7-8 numbers.
    The phone number might be separated from the area code with a whitespace, but not necessarily.

    The function must return a dictionary where keys are the area codes
    and values are lists of the phone numbers with the corresponding area number.
    If a phone number does not have an area code given, its area code would be empty string,
    so in dictionary it would be like that: {"": ["56332456"]}.

    Phone numbers must be found using regex.

    :param text: given string to find phone numbers from
    :return: dict containing the numbers
    """
    phone_database = {}
    for match in re.findall(r"(\+\d{3}?)? ?(\d{7,8})", text):
        prefix = match[0]
        phone_number = match[1]
        if prefix not in phone_database:
            phone_database[prefix] = [phone_number]
        else:
            phone_database[prefix].append(phone_number)

    return phone_database


if __name__ == '__main__':
    print(find_words('KanaMunaPelmeen!!ApelsinÕunMandariinKakaoHernesAhven'))
    # ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']

    print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))
    # ['Apelsin', 'Õun', 'Ahven']

    print(find_sentences('See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))
    # ['See on esimene - lause.', 'See on ä teine lause!', 'Aga kas see on?']

    print(find_sentences('ei ole lause. See on!!! See ka...Ja see... See pole'))
    # ['See on!!!', 'See ka...', 'Ja see...']

    print(find_words_from_sentence("Super lause ää, sorry."))
    # ['Super', 'lause', 'ää', 'sorry']

    print(find_words_from_sentences_only(
        'See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))
    # ['See', 'on', 'esimene', 'ä', 'lause', 'See', 'on', 'teine', 'lause', 'Aga', 'kas', 'see', 'on']

    print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))
    # [1998, 7777]

    print(find_phone_numbers("+372 56887364  +37256887364  +33359835647  56887364 +11 1234567 +327 1 11111111"))
    # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364', '1234567', '11111111']}
