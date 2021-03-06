"""Tools for hashing the text"""

from hashlib import sha1


class UnknownHashingAlgorithm(Exception):
    pass


class HashedText:
    def __init__(self, text: str, hashing_algorithm=sha1) -> None:
        self.known_algorithms = (sha1,)
        self.hashed = self._do_hashing(text, hashing_algorithm)

    def _do_hashing(self, text: str, hashing_algorithm) -> str:
        """Hash text using algorithm that must be a member of self.known_algorithms (defaults to sha1)"""
        if hashing_algorithm in self.known_algorithms:
            return hashing_algorithm(text.encode("utf-8")).hexdigest()
        else:
            raise UnknownHashingAlgorithm

    def get_five_digits(self) -> str:
        """get first five digits of hashed text"""
        return self.hashed[:5]
