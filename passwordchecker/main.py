"""Main app exec"""
import logging
from passwordchecker.validators import PasswordValidator
from passwordchecker.validation_errors import ValidationException

logging.basicConfig(level=logging.INFO)


def parse_from_file(input_file: str, output_file: str):
    """test multiple passwords taken from the input file against being pwnd.
    Save good passwords to the output file"""
    with open(input_file, encoding="utf-8") as file, open(
        output_file, mode="w", encoding="utf-8"
    ) as output:
        counter = 1
        for line in file:
            try:
                password = PasswordValidator(line)
                password.is_valid()
                output.write(line)
            except ValidationException as error:
                logging.info(
                    "Line %s: Bad password: %s", counter, error.__class__.__name__
                )
            finally:
                counter += 1


def main():
    """main app call. Uses passwords.txt file as input and bezpieczne.txt as outpu"""
    parse_from_file("passwords.txt", "bezpieczne.txt")


if __name__ == "__main__":
    main()
