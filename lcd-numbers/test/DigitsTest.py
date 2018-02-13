import unittest
from parameterized import parameterized, param
import lcd.digits
from lcd.lcd import Configuration


class TestDigits(unittest.TestCase):
    def _get_digits(self, scaling=1):
        digit_reader = lcd.digits.DigitReader(Configuration.RESOURCE_DIRECTORY)
        digits = digit_reader.read_digits(scaling)
        return digits

    @parameterized.expand([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
    def test_digits_size(self, input_digit):
        digits = self._get_digits()
        digit = digits.get_digit(input_digit)
        digit_representation = digit.get_representation()
        line_count = len(digit_representation)
        self.assertEqual(line_count, 5)

        for line in digit_representation:
            self.assertEqual(len(line), 3)
            # for line in digit.get_representation():

    @parameterized.expand([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
    def test_get_digit(self, input_digit):
        digits = self._get_digits()
        self.assertIsInstance(digits.get_digit(input_digit), lcd.digits.Digit)

    # @parameterized.expand([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
    def test_digit_scaling(self, input_digit=5):
        digits = self._get_digits()
        digit = digits.get_digit(input_digit)
        scaled_digit = digit.scale(2).get_representation()
        resulting_digit = [" -- ",
                           "|   ",
                           "|   ",
                           " -- ",
                           "   |",
                           "   |",
                           " -- "]

        self.assertEquals(scaled_digit, resulting_digit, "Scaling 5 is wrong %s" % str(scaled_digit))

    def test_assemble_numbers(self):
        digits = self._get_digits(2)
        expected = [
            '     --  --      --  --  --  --  --  -- ',
            '   |   |   ||  ||   |      ||  ||  ||  |',
            '   |   |   ||  ||   |      ||  ||  ||  |',
            '     --  --  --  --  --      --  --     ',
            '   ||      |   |   ||  |   ||  |   ||  |',
            '   ||      |   |   ||  |   ||  |   ||  |',
            '     --  --      --  --      --  --  -- ',
        ]
        self.assertEquals(expected, digits.assemble_numbers('1234567890'))

