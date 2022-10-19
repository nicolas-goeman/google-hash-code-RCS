from google_hash_code_rcs.classes import Binary, Feature, Engineer, Service

def test_classes() -> None:
    """Empty test function
    """
    b = Binary()
    e = Engineer(id=1)
    f = Feature(services=[], users=100, difficulty=3)
    s = Service(binary=[])

    assert 1 == 1
