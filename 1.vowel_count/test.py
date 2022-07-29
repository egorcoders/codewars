import unittest

from case_result import case_result_dct as c_dct
from solution import get_count


class TestFn(unittest.TestCase):
    def test_case_result(self):
        for c, r in c_dct.items():
            self.assertEqual(
                get_count(c), r, 'There is an error'
            )


if __name__ == '__main__':
    unittest.main()
