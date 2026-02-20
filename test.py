import unittest
import main as odd_even

class TestOddEven(unittest.TestCase):

    def test_even_number(self):
        result = odd_even.check_odd_even(10)
        self.assertEqual(result, "Even")

    def test_odd_number(self):
        result = odd_even.check_odd_even(7)
        self.assertEqual(result, "Odd")

    def test_zero(self):
        result = odd_even.check_odd_even(0)
        self.assertEqual(result, "Even")

    def test_negative_number(self):
        result = odd_even.check_odd_even(-3)
        self.assertEqual(result, "Odd")

    def test_invalid_input_string(self):
        result = odd_even.check_odd_even("Hello")
        self.assertEqual(result, "Invalid Input: Not an Integer")

    def test_invalid_input_float(self):
        result = odd_even.check_odd_even(5.5)
        self.assertEqual(result, "Invalid Input: Not an Integer")


if __name__ == "__main__":
    unittest.main()