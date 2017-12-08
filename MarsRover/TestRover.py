import unittest
from parameterized import parameterized
from MarsRover import Map
from MarsRover import MarsRover

class TestStringMethods(unittest.TestCase):

    def test_turn_right(self):
        marsRover = MarsRover(Map(100,100), 0, 0, 'N')
        marsRover.turnRight()
        self.assertEqual(marsRover.direction, 'E')
        marsRover.turnRight()
        self.assertEqual(marsRover.direction, 'S')
        marsRover.turnRight()
        self.assertEqual(marsRover.direction, 'W')
        marsRover.turnRight()
        self.assertEqual(marsRover.direction, 'N')

    def test_turn_left(self):
        marsRover = MarsRover(Map(100,100), 0, 0, 'N')
        marsRover.turnLeft()
        self.assertEqual(marsRover.direction, 'W')
        marsRover.turnLeft()
        self.assertEqual(marsRover.direction, 'S')
        marsRover.turnLeft()
        self.assertEqual(marsRover.direction, 'E')
        marsRover.turnLeft()
        self.assertEqual(marsRover.direction, 'N')

    @parameterized.expand([
        ["N", 10, 11],
        ["E", 11, 10],
        ["W",  9, 10],
        ["S", 10, 9],
    ])
    def test_move_forward(self, direction, positionX, positionY):
        marsRover = MarsRover(Map(100,100), 10, 10, direction)
        marsRover.moveForward()
        self.assertEqual(marsRover.getPosition(), [positionX, positionY])

    @parameterized.expand([
        ["N", 10, 9],
        ["E", 9,  10],
        ["W", 11, 10],
        ["S", 10, 11],
    ])
    def test_move_backward(self, direction, positionX, positionY):
        marsRover = MarsRover(Map(100,100), 10, 10, direction)
        marsRover.moveBackward()
        self.assertEqual(marsRover.getPosition(), [positionX, positionY])

    @parameterized.expand([
        ["N", [0, 0], [0, 9]],
        ["E", [0, 0], [9, 0]],
        ["S", [9, 9], [9, 0]],
        ["W", [9, 9], [0, 9]],        
    ])
    def test_move_over_grid_boundary(self, direction, initialPosition, expectedPosition):
        marsRover = MarsRover(Map(10,10), initialPosition[0], initialPosition[1], direction)
        marsRover.moveBackward()
        self.assertEqual(marsRover.getPosition(), [expectedPosition[0], expectedPosition[1]])

    

'''
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)