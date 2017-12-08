import sys


class PlanetarySurfaceMap(object):

    def __init__(self, planet_surface_width, planet_surface_height):
        self.planet_surface_width = planet_surface_width
        self.planet_surface_height = planet_surface_height


class RovingVehiclePosition(object):
    pass


# SurfaceRovingVehicle(object):
class PlanetaryRovingVehicle(object):
    _vehicle_allowed_directions = ['N', 'S', 'E', 'W']

    def __init__(self, planetary_surface_map, vehicle_starting_horizontal_position, vehicle_starting_vertical_position, vehicle_starting_direction):
        self.planetary_surface_map = planetary_surface_map
        self.actual_horizontal_position = vehicle_starting_horizontal_position
        self.actual_vertical_position = vehicle_starting_vertical_position
        self.actual_vehicle_direction = vehicle_starting_direction

    def _move_vehicle_by_distance(self, distance_to_move_vehicle):
        direction_to_distance_mapping = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}


    def move_vehicle_forward(self, distance_to_move_forward):
        self._move_vehicle_by_distance(distance_to_move_forward)

    def move_vehicle_backwards(self, distance_to_move_backward):
        self._move_vehicle_by_distance(-distance_to_move_backward)

    def get_vehicle_position(self):
        return [self.actual_horizontal_position, self.actual_vertical_position]

    def get_actual_direction(self):
        return self.actual_vehicle_direction


def main():
    pass


if __name__ == '__main__':
    sys.exit(main())
