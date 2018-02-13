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

    def _get_parser(self):
        def validate_argument_scale(value):
            """Validate the scale command line argument as int > 0"""
            i = int(value)
            if i < 1:
                raise argparse.ArgumentTypeError("%s is an invalid value (allowed > 1)" % value)
            return i

        parser = argparse.ArgumentParser(description="Print numbers as LCD")
        parser.add_argument("number", help="number", type=int)
        parser.add_argument("-s", "--scale", type=validate_argument_scale,
                            default=2, help="Scale the numbers by number")
        return parser

    def get_arguments(self):
        return self._parser.parse_args()


class LcdDisplay(object):
    def __init__(self, scaling=1):
        resource_directory = Configuration.RESOURCE_DIRECTORY
        digits = DigitReader(resource_directory).read_digits(scaling)
        self._digits = digits
        self._scaling = scaling

    def display_numbers(self, numbers):
        self._digits.print_numbers(numbers, self.printer)

    def printer(self, data):
        print(data)



def main():
    args = ArgumentParser().get_arguments()
    lcd_display = LcdDisplay(args.scale)
    lcd_display.display_numbers(args.number)


if __name__ == "__main__":
    sys.exit(main())
