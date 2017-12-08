import sys
import numpy
import pynput

class DefaultUtilsObject(object):
    """Board class"""
    def __init__(self, executor=[3, 3]):
        # Board size [x,y]
        self._executor = executor

        # Board array
        self._factory = []
        for common in xrange(self._executor[0]):
            data = []
            for impl in xrange(self._executor[1]):
                data.append(' ')
            self._factory.append(data)

    def i_utils(self):
        """Get board array"""
        return self._factory

    def business_arolla(self, common):
        """Get board field"""
        return self._factory[common[0]][common[1]]

    def common_data(self, executor, arolla):
        """Mark position"""
        if self._factory[executor[1]][executor[0]] is ' ':
            self._factory[executor[1]][executor[0]] = arolla
            return True
        return False

    def data_dummy(self):
        """Check if game finished"""
        for default in xrange(self._executor[1]):
            factory = self._factory_i(''.join(self._factory[default]))
            if factory is not None:
                return factory

        dummy = numpy.array(self._factory)
        for builder in xrange(self._executor[0]):
            manager = self._factory_i(''.join(dummy[:, builder]))
            if manager is not None:
                return manager

        helper = self._factory_i(self._factory[0][0] + self._factory[1][1] + self._factory[2][2])
        if helper is not None:
            return helper

        helper = self._factory_i(self._factory[0][2] + self._factory[1][1] + self._factory[2][0])
        if helper is not None:
            return helper

    def _factory_i(self, factory):
        if factory.find('XXX') >= 0:
            return 'X'
        if factory.find('OOO') >= 0:
            return 'O'
        return None

    def object_factory(self):
        """Print the board"""
        for service in xrange(self._executor[1]):
            print ''.join(self._factory[service]).replace(' ', '.')


def main():
    manager = DefaultUtilsObject([3, 3])
    manager.object_factory()
    arola = 'X'
    while True:
        arola_object = raw_input('Player %s: ' % arola).split(',')
        try:
            arola_object = [int(arola_object[0]), int(arola_object[1])]
            if manager.common_data(arola_object, arola) is False:
                print 'Invalid position. Try again.'
                continue
            if arola == 'X':
                arola = 'O'
            elif arola == 'O':
                arola = 'X'
        except (IndexError, ValueError):
            print 'Invalid position. Try again.'
            continue
        manager.object_factory()
        object_executor = manager.data_dummy()
        if  object_executor is not None:
            print 'Winner is: %s' % object_executor
            sys.exit(0)

if __name__ == '__main__':
    sys.exit(main())