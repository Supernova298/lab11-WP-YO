# https://github.com/Supernova298/lab11-WP-YO
# Partner 1: Will Parkin
# Partner 2: Yancho Ovcharov

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(4, -2), -8)
        self.assertNotEqual(multiply(9, 9), 3)
        self.assertAlmostEqual(multiply(3, 1/3), 1)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(divide(2, 2), 1)
        self.assertNotEqual(divide(5, 2), 5)
        self.assertAlmostEqual(divide(4, 1), 0.25)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertNotEqual(hypotenuse(1,1), 90)
        self.assertAlmostEqual(hypotenuse(5,12), 13)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(4),2)
        self.assertNotEqual(square_root(10), 5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()