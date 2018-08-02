import unittest
from ddt import ddt, data, file_data, unpack


@ddt
class FooTestCase(unittest.TestCase):

    @file_data("./test_data/test_ddt_file.json")
    def test_file_data_json_dict_dict(self, start, end, value):
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)


if __name__ == '__main__':
    unittest.main()
