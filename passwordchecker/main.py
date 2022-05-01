from passwordchecker.validators import PasswordValidator
import logging

logging.basicConfig(level=logging.INFO)


def parse_from_file(input_file: str, output_file: str):
    """test multiple passwords taken from the input file against being pwnd. Save good passwords to the output file"""
    with open(input_file) as file, open(output_file, mode="w") as output:
        counter = 1
        for line in file:
            try:
                password = PasswordValidator(line)
                password.is_valid()
                output.write(line)
            except Exception as error:
                logging.info(f"Line {counter}: Bad password: {error=}")
            finally:
                counter += 1


def main():
    parse_from_file("passwords.txt", "bezpieczne.txt")


if __name__ == "__main__":
    main()
