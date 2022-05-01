from abc import ABC, abstractmethod
from passwordchecker.validation_errors import (
    HasBeenPwnd,
    TooShort,
    NoNumbers,
    NoSpecialCharacters,
    OnlyUppercase,
    OnlyLowercase,
    BadPassword,
)
from passwordchecker.hashed_text import HashedText
from passwordchecker.pwnd_hashes import SimilarPwndHashedPasswords


class Validator(ABC):
    @abstractmethod
    def __init__(self, text: str) -> None:
        pass

    @abstractmethod
    def is_valid(self):
        pass


class LengthValidator(Validator):
    """checks whether text has more than 8 characters"""

    def __init__(self, text: str) -> None:
        self.text = text

    def is_valid(self, length=8):
        """raise TooShort exception is text is shorter than specified length (default 8)"""
        if len(self.text) < length:
            raise TooShort


class HasNumberValidator(Validator):
    """checks whether text includes numbers"""

    def __init__(self, text: str) -> None:
        self.text = text

    def is_valid(self):
        if not any(character in "1234567890" for character in self.text):
            raise NoNumbers


class HasSpecialCharactersValidator(Validator):
    """checks whether text includes special characters"""

    def __init__(self, text: str) -> None:
        self.text = text

    def is_valid(self):
        if not any(
            character in "`~!@#$%^&*()_-+=[]}{|\\;:'\",./<>?" for character in self.text
        ):
            raise NoSpecialCharacters


class HasLowerAndUppercaseValidator(Validator):
    """check whether text has both upper and lowercase chars"""

    def __init__(self, text: str) -> None:
        self.text = text

    def is_valid(self):
        if self.text.upper() == self.text:
            raise OnlyUppercase
        elif self.text.lower() == self.text:
            raise OnlyLowercase


class NotPwndValidator(Validator):
    """checks whether text has been listed as pwnd"""

    def __init__(self, text: str) -> None:
        self.text = text

    def is_valid(self):
        to_validate = HashedText(self.text)
        pwnd = SimilarPwndHashedPasswords(to_validate.get_five_digits())
        for item in pwnd.similar:
            if to_validate.hashed.upper() == item.upper():
                raise HasBeenPwnd


class PasswordValidator(Validator):
    """Validate your password using known validators"""

    def __init__(self, password: str) -> None:
        self.password = password
        self.known_validators = (
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharactersValidator,
            HasLowerAndUppercaseValidator,
            NotPwndValidator,
        )

    def is_valid(self):
        try:
            for class_name in self.known_validators:
                validate = class_name(self.password)
                validate.is_valid()
        except Exception:
            raise BadPassword
