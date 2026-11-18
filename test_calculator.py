# https://github.com/avnithaathoppae/lab11-AT-JZ
# Partner 1: Avnithaa Thoppae
# Partner 2: Jessica Zhang
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(15, 2), 17)
        self.assertEqual(add(4, 2), 6)
        self.assertEqual(add(35, 10), 45)
    #     fill in code


    def test_subtract(self):
        self.assertEqual(subtract(15, 2), 13)
        self.assertEqual(subtract(4, 2), 2)
        self.assertEqual(subtract(14, 11), 3)
    #     fill in code
    # ##########################


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 4), 8)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 10), 0)
    #  # 3 assertions
    #     fill in code


    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-1, 5), -5)
        self.assertEqual(div(2, 9), 4.5)
    #  # 3 assertions
    #     fill in code
    # ##########################


    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code


    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(3, 81), 4)
    #     fill in code


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
   
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
       
        # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code


    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertEqual(hypotenuse(-3, -4), 5)
        # 3 assertions
    #     fill in code


    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)


         # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()

