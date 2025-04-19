import argparse

parser = argparse.ArgumentParser(description="Username generator")
parser.add_argument(
    "-fn", "--first_name", help="First name of the user (required)", required=True
)
parser.add_argument(
    "-ln", "--last_name", help="Last name of the user (required)", required=True
)
parser.add_argument(
    "-n",
    "--number",
    help="single number or a range of numbers separated by a comma (e.g. 0,10). Optionnal, will append number(s) to username",
    required=False,
)
parser.add_argument(
    "-o",
    "--output",
    help="Output file name (default : 'usernames.txt'). Should end with .txt",
    required=False,
)
parser.add_argument(
    "-l",
    "--leet",
    help="Specify letters (lowercase or uppercase) to apply leetspeak transformation without any separator (e.g. 'aEi' -> '431'). Optional, if no specified letters, full leet dictionary will apply (see code)",
    required=False,
)

args = parser.parse_args()


def basic(first_name, last_name):
    basics = []
    separators = ["", ".", "-", "_"]
    for seperator in separators:
        basics.extend(
            [
                first_name + seperator + last_name,
                last_name + seperator + first_name,
                first_name[0] + seperator + last_name,
                last_name[0] + seperator + first_name,
                last_name + seperator + first_name[0],
                first_name + seperator + last_name[0],
            ]
        )
    return basics


def solo_number(first_name, last_name, number):
    numbered_emails = [i + str(number) for i in basic(first_name, last_name)]
    return numbered_emails


def numbers(first_name, last_name, number_range):
    number_range = [int(i) for i in number_range]
    usernames = []
    for i in range(number_range[0], number_range[1] + 1):
        usernames.extend(solo_number(first_name, last_name, i))
    return usernames


def leet(usernames: list, user_letters=None):
    leet_dict = {
        "a": "4",
        "A": "4",
        "b": "8",
        "B": "8",
        "e": "3",
        "E": "3",
        "g": "6",
        "G": "6",
        "h": "#",
        "H": "#",
        "i": "1",
        "I": "1",
        "l": "1",
        "L": "1",
        "o": "0",
        "O": "0",
        "s": "5",
        "S": "5",
        "t": "7",
        "T": "7",
        "z": "2",
        "Z": "2",
    }
    if user_letters:
        user_dict = {}
        for letter in user_letters:
            if letter in leet_dict:
                user_dict[letter] = leet_dict[letter]
            else:
                print(f"No leet version for the letter '{letter}'")
    else:
        user_dict = leet_dict

    leet_table = str.maketrans(user_dict)

    return [username.translate(leet_table) for username in usernames]


def result():
    result = basic(args.first_name, args.last_name)
    if args.number:
        user_numbers = args.number.split(",")
        if len(user_numbers) == 1:
            result.extend(solo_number(args.first_name, args.last_name, user_numbers[0]))
        elif len(user_numbers) == 2:
            result.extend(numbers(args.first_name, args.last_name, user_numbers))
        else:
            print("Error : 1 or 2 numbers only")
    if args.leet:
        result.extend(leet(result, args.leet))
    return result


if args.output:
    if args.output.endswith(".txt"):
        filename = args.output
    else:
        filename = "usernames.txt"
        print("Extension problem : default file created (usernames.txt)")
else:
    filename = "usernames.txt"

with open(filename, "w", encoding="utf-8") as output_file:
    for username in result():
        output_file.write(username + "\n")
    print(f"Completed in file {filename}")
