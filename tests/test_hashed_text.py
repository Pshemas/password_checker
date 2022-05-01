from passwordchecker.hashed_text import HashedText


def test_hashing():
    sample = HashedText("alamakota")
    known_sha1 = "D1217AEEB182C9106254D397BA743802C26D6AFE"
    assert sample.hashed.lower() == known_sha1.lower()


def test_get_five_digits():
    sample = HashedText("alamakota")
    assert len(sample.get_five_digits()) == 5
