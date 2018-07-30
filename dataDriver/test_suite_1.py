import pytest


def test_one(config_data):
    assert config_data >= 0


def test_two(config_data):
    assert config_data == 'split'


def test_three(config_data):
    assert config_data['three'] == 3


def test_four(config_data):
    assert config_data['four'] == 4


if __name__ == '__main__':
    pytest.main(["-v", "test_suite_1.py"])
