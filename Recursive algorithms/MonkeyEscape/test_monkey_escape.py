import unittest
from monkey_escape import MonkeyEscape


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.monkey_escape = MonkeyEscape()

    def test_output_from_k3_d1(self):
        result = self.monkey_escape.monkey_from_the_zoo_get_data(True, 1, [3], [1])
        self.assertEqual(3, result)

    def test_output_from_k3_d2(self):
        result = self.monkey_escape.monkey_from_the_zoo_get_data(True, 1, [3], [2])
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()
