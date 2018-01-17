from __future__ import print_function
import argparse
import sys
import os

from digits import DigitReader


class Configuration(object):
    RESOURCE_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + "/resources/"


class ArgumentParser(object):
    def __init__(self):
        parser = self._get_parser()
        self._parser = parser

    def _validate_argument_scale(self, value):
        """Validate the scale command line argument as int > 0"""
        i = int(value)
        if i < 1:
            raise argparse.ArgumentTypeError("%s is an invalid value (allowed > 1)" % value)
        return i

    def _get_parser(self):
        parser = argparse.ArgumentParser(description="Print numbers as LCD")
        parser.add_argument("number", help="number", type=int)
        parser.add_argument("-s", "--scale", type=self._validate_argument_scale,
                            default=1, help="Scale the numbers by number")
        return parser

    def get_arguments(self):
        return self._parser.parse_args()


class LcdDisplay(object):
    def __init__(self, scaling=1):
        resource_directory = Configuration.RESOURCE_DIRECTORY
        digits = DigitReader(resource_directory).read_digits()
        self._digits = digits
        self._scaling = scaling

    def display_numbers(self, numbers):
        lcd_number = self.assemble_numbers(numbers)
        for line in lcd_number:
            print(line)

    def assemble_numbers(self, numbers):
        lcd_number = []
        for index in xrange(3+2*self._scaling):
            lcd_number.append(self._assemble_line(index, numbers))
        return lcd_number

    def _assemble_line(self, index, numbers):
        line = ""
        for number in str(numbers):
            digit = self._digits.get_digit(number)
            line += digit.scale(self._scaling)[index]
        return line


def main():
    args = ArgumentParser().get_arguments()
    lcd_display = LcdDisplay(args.scale)
    lcd_display.display_numbers(args.number)


if __name__ == "__main__":
    sys.exit(main())
