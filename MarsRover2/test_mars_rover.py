import unittest
from parameterized import parameterized
import mock


class TestPlanetaryRovingVehicle(unittest.TestCase):

    @parameterized.expand([
        [{'start': [[0, 0], 'N'], 'step': 1, 'expected': [0, 1]}],
    ])
    def test_move_vehicle_forward(self, vehicle_test_parameters):
        vehicle_starting_position = vehicle_test_parameters['start'][0]
        vehicle_starting_direction = vehicle_test_parameters['start'][1]
        vehicle_distance_to_move = vehicle_test_parameters['step']
        vehicle_expected_position = vehicle_test_parameters['expected']
