import json
import pathlib
import pytest


@pytest.fixture(scope="class")
def test_config(request):
    f = pathlib.Path(request.node.fspath.strpath)
    config = f.with_name("login_data.json")
    with config.open() as fd:
        testdata = json.loads(fd.read())
    yield testdata


@pytest.fixture(scope="function")
def config_data(request, test_config):
    testdata = test_config
    test = request.function.__name__
    if test in testdata:
        test_args = testdata[test]
        yield test_args
    else:
        yield {}


def pytest_generate_tests(metafunc):
    if 'config_data' not in metafunc.fixturenames:
        return
    config = pathlib.Path(metafunc.module.__file__).with_name('login_data.json')
    testdata = json.loads(config.read_text())
    param = testdata.get(metafunc.function.__name__, None)
    if isinstance(param, list):
        metafunc.parametrize('config_data', param)