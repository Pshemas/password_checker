import pytest
from passwordchecker.validators import *


def test_length():
    with pytest.raises(TooShort):
        validate = LengthValidator("aaa")
        validate.is_valid()


def test_nonumber():
    with pytest.raises(NoNumbers):
        validate = HasNumberValidator("aaa")
        validate.is_valid()


def test_no_special_character():
    with pytest.raises(NoSpecialCharacters):
        validate = HasSpecialCharactersValidator("aaa")
        validate.is_valid()


def test_has_special_character():
    validate = HasSpecialCharactersValidator("aaa@")
    try:
        validate.is_valid()
    except NoSpecialCharacters as exception:
        assert False, f"aaa@ raised an exception: {exception}"


def test_onlylowercase():
    with pytest.raises(OnlyLowercase):
        validate = HasLowerAndUppercaseValidator("aaa")
        validate.is_valid()


def test_onlyuppercase():
    with pytest.raises(OnlyUppercase):
        validate = HasLowerAndUppercaseValidator("AAA")
        validate.is_valid()


def test_pwnd_false(requests_mock):
    mocked_response = (
        "00379A168B381944900F4A1CA36E8FE52B3:2\n0043EC92D698C93FF11FF3B6DF93B17433E:2"
    )
    requests_mock.get(
        "https://api.pwnedpasswords.com/range/d1217", text=mocked_response
    )
    validate = NotPwndValidator("alamakota")
    try:
        validate.is_valid()
    except HasBeenPwnd:
        assert False


def test_pwnd_true(requests_mock):
    # alamakota
    # full hash: D1217AEEB182C9106254D397BA743802C26D6AFE
    mocked_response = (
        "AEEB182C9106254D397BA743802C26D6AFE:2\n0043EC92D698C93FF11FF3B6DF93B17433E:2"
    )
    requests_mock.get(
        "https://api.pwnedpasswords.com/range/d1217", text=mocked_response
    )
    validate = NotPwndValidator("alamakota")
    with pytest.raises(HasBeenPwnd):
        validate.is_valid()
