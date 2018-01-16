import unittest
from parameterized import parameterized, param
import lcd.digits
from lcd.lcd import Configuration

class TestDigitReader(unittest.TestCase):

    @parameterized.expand([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
    def test_digits_size(self, input_digit):
        digit_reader = lcd.digits.DigitReader(Configuration.RESOURCE_DIRECTORY)
        digits = digit_reader.read_digits()
        digit = digits.get_digit(input_digit)
        digit_representation = digit.get_representation()
        line_count = len(digit_representation)
        self.assertEqual(line_count, 5)

        for line in digit_representation:
            self.assertEqual(len(line), 3)
        #for line in digit.get_representation():
