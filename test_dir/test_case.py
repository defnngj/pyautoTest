
def add(a, b):
    return a + b


def test_add():
    assert add(2, 2) == 4


def test_add2():
    assert add(2.1, 3.6) == 5.7


def test_add3():
    assert add(0.1, 3.6) == 3.7


def test_add4():
    assert add(0.1, 3.6) == 3.7
