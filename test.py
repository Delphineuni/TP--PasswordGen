import unittest
import os

class Test1(unittest.TestCase):

    def test_case1(self):
            expected_output = '2'
	            self.assertEqual(create_grid_and_calculate(2, 2), expected_output)
		            self.assertEqual(create_grid_and_calculate(int("R G B"), int("R G B")), expected_output)

			    if __name__ == '__main__':
			        unittest.main()
