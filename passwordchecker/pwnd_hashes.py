"""tools for handling pwndpassords.com"""

from requests import get


class SimilarPwndHashedPasswords:
    """create container for a list of pwnd hashes similar to the one provided"""

    def __init__(self, five_hash_digits: str) -> None:
        self.similar = self.get_similar(five_hash_digits)

    @staticmethod
    def get_similar(five_hash_digits: str):
        """get generator of similar passwords hashes found on pwnedpasswords.com"""
        response = get("https://api.pwnedpasswords.com/range/" + five_hash_digits)
        response = response.text.splitlines()
        for element in response:
            yield element.split(":")[0]
