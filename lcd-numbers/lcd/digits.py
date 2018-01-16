class Digit(object):
    def __init__(self, digit, representation):
        self._digit = digit
        self._digit_representation = representation

    def scale(self, scale_factor=1):
        pass

    def get_representation(self):
        return self._digit_representation

    def get_line(self, index):
        return self._digit_representation[int(index)]


class Digits(object):
    def __init__(self, digit_representations):
        self._digits = [Digit(i, representation)
                        for i, representation in enumerate(digit_representations)]

    def get_digit(self, digit):
        return self._digits[int(digit)] #This is an indexed getter


class DigitReader(object):
    def __init__(self, resource_directory):
        self._resource_directory = resource_directory

    def read_digits(self):
        return Digits([self._read_digit_from_file(number) for number in xrange(10)])

    def _read_digit_from_file(self, digit):
        file_name = self._resource_directory + str(digit) + ".txt"
        with open(file_name) as file_handle:
            return [line.replace('\n', '') for line in file_handle.readlines()]
