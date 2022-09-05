import unittest

from case_result import case_result_lst as c_dct
from solution import directions


class TestFn(unittest.TestCase):
    def test_case_result(self):
        for c, r, t in c_dct:
            self.assertEqual(
                directions(c), r, f'There is an error in {t.upper()}'
            )


if __name__ == '__main__':
    unittest.main()
