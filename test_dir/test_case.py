
def add(a, b):
    return a + b


def test_add():
    assert add(2, 2) == 4


def test_add2():
    assert add(2.1, 3.6) == 5.7
