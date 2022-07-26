import unittest

from case_result import case_result_dct as c_dct
from solution import likes


class TestFn(unittest.TestCase):
    def test_case_result(self):
        for r, c in c_dct.items():
            self.assertEqual(
                likes(c), r, 'There is an error'
            )


if __name__ == '__main__':
    unittest.main()
