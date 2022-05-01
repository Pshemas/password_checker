from passwordchecker.hashed_text import HashedText


def test_hashing():
    """tests hashing against known hash"""
    sample = HashedText("alamakota")
    known_sha1 = "D1217AEEB182C9106254D397BA743802C26D6AFE"
    assert sample.hashed.upper() == known_sha1.upper()


def test_get_five_digits():
    """tests whether get five digits indeed returns 5"""
    sample = HashedText("alamakota")
    assert len(sample.get_five_digits()) == 5
