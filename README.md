Username Generator
Description

This Python script generates a list of possible usernames based on a given first name and last name. Users can specify additional options such as including numbers, applying leetspeak transformations, and saving the results to a specified output file.
Features

    Generate usernames by combining first name and last name with various separators (., -, _).

    Append numbers to usernames from a specified range or single value.

    Apply leetspeak transformations to characters in the usernames.

    Output the results to a text file with a customizable name.

Installation

This project requires Python 3.x.

    Clone the repository:

git clone https://github.com/yourusername/username-generator.git
cd username-generator

Install dependencies (if any):

    pip install -r requirements.txt

Usage

To use the username generator, run the script from the command line with the following arguments:
Command Line Arguments

    -fn, --first_name (required): The first name of the user.

    -ln, --last_name (required): The last name of the user.

    -n, --number (optional): A single number or a range of numbers (e.g., 0,10) to append to the username.

    -o, --output (optional): The name of the output file (default: usernames.txt). The file should end with .txt.

    -l, --leet (optional): Specify letters to apply leetspeak transformations (e.g., aEi -> 431). If not provided, the full leet dictionary is applied.

Example

python username_generator.py -fn John -ln Doe -n 0,10 -o john_doe_usernames.txt -l aEi

This will generate usernames based on the first and last names, append numbers from 0 to 10, apply leetspeak transformations for a, E, and i, and save the results in a file named john_doe_usernames.txt.
Code Structure
Functions

    basic(first_name, last_name): Generates basic username variations using different separators (., -, _).

    solo_number(first_name, last_name, number): Appends a single number to the generated usernames.

    numbers(first_name, last_name, number_range): Appends a range of numbers to the generated usernames.

    leet(usernames, user_letters=None): Applies leetspeak transformations to the usernames based on a predefined dictionary. If no letters are specified, the full dictionary is applied.

    result(): Aggregates the results from the basic, number, and leetspeak functions based on the provided arguments.

Example Output

For the input John and Doe, the script will generate a list of usernames such as:

john.doe
doe.john
j.doe
doe.j
john_doe0
john_doe1
...
john_doe_431

License

This project is licensed under the MIT License - see the LICENSE file for details.
