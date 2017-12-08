import argparse
import random

class Map():
    def __init__(self, initialSizeX, initialSizeY):
        self.sizeX = initialSizeX
        self.sizeY = initialSizeY
        self.obstacles = []
    
    def addObstacle(self, positionX, positionY):
        self.obstacles.append([positionX, positionY])

    def randomizeObstacles(self, obstacleCount):
        for i in range(obstacleCount):
            positionX = random.randint(0, self.sizeX - 1)
            positionY = random.randint(0, self.sizeY - 1)
            self.addObstacle(positionX, positionY)

    def getSizeX(self):
        return self.sizeX

    def getSizeY(self):
        return self.sizeY

class MarsRover():
    allowedDirections = ['N', 'E', 'S', 'W']

    def __init__(self, map, startinPointX, startingPointY, initialDirection):
        self.map = map
        self.positionX = int(startinPointX)
        self.positionY = int(startingPointY)
        self._checkDirection(initialDirection)
        self.direction = initialDirection
    
    def _checkDirection(self, direction):
        if direction not in self.allowedDirections:
            raise Exception('UndefinedDirection')    

    def turnLeft(self):
        leftOf = {
            'N': 'W',
            'W': 'S',
            'S': 'E',
            'E': 'N'
        }
        self.direction = leftOf[self.direction]

    def turnRight(self):
        rightOf = {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        } 
        self.direction = rightOf[self.direction]

    def moveForward(self):
        self._moveStraight(1)

    def moveBackward(self):
        self._moveStraight(-1)

    def _moveStraight(self, distance):
        if self.direction == 'N':
            self.positionY += distance
        elif self.direction == 'S':
            self.positionY += -distance
        elif self.direction == 'E':
            self.positionX += distance
        elif self.direction == 'W':
            self.positionX += -distance

        self.positionX = self.positionX % self.map.getSizeX()
        self.positionY = self.positionY % self.map.getSizeY()


    def getPosition(self):
        return [self.positionX, self.positionY]

    def _executeCommand(self, command):
        if command == 'f':
            self.moveForward()
        elif command == 'b':
            self.moveBackward()
        elif command == 'l':
            self.turnLeft()
        elif command == 'r':
            self.turnRight()

    def executeCommands(self, commands):
        for command in commands:
            print self.getPosition()
            self._executeCommand(command)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('commands')
    args = parser.parse_args()
    
    marsRover = MarsRover(Grid(100,100), 0, 0, 'N')
    marsRover.executeCommands(args.commands)

    print marsRover.getPosition()