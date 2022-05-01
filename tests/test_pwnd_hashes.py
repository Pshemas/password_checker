from passwordchecker.pwnd_hashes import SimilarPwndHashedPasswords


def test_pwnd_response(requests_mock):
    mocked_response = (
        "00379A168B381944900F4A1CA36E8FE52B3:2\n0043EC92D698C93FF11FF3B6DF93B17433E:2"
    )
    requests_mock.get(
        "https://api.pwnedpasswords.com/range/d1217", text=mocked_response
    )
    sample = SimilarPwndHashedPasswords("d1217")
    assert len(sample.similar) == 2
