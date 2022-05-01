"""Exceptions that validators can rise"""


class ValidationException(Exception):
    """general validation exception"""


class TooShort(ValidationException):
    """rised when text too short"""


class OnlyLowercase(ValidationException):
    """rised when text has only lowecase characters"""


class OnlyUppercase(ValidationException):
    """rised when text has only uppercase characters"""


class NoNumbers(ValidationException):
    """rised when text contains no numbers"""


class NoSpecialCharacters(ValidationException):
    """rised when text contains no special characters"""


class HasBeenPwnd(ValidationException):
    """rised when identical hash for the text has been found"""
