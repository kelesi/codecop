class Digit(object):
    def __init__(self, digit, representation):
        self._digit = digit
        self._digit_representation = representation

    def scale(self, scale_factor=1):
        scaled_lines = []
        for line in self._digit_representation:
            scaled_lines.append(line[0] + line[1]*scale_factor + line[2])

        scaled_digit = []
        scaled_digit.append(scaled_lines[0])
        for i in xrange(scale_factor):
            scaled_digit.append(scaled_lines[1])
        scaled_digit.append(scaled_lines[2])
        for i in xrange(scale_factor):
            scaled_digit.append(scaled_lines[3])
        scaled_digit.append(scaled_lines[4])

        return scaled_digit

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
