import unittest
import decimal

from mock import MagicMock
from mock import patch
from parameterized import parameterized
from tire_pressure_monitoring import Alarm
from tire_pressure_monitoring import Sensor

class AlarmTest(unittest.TestCase):

    @parameterized.expand([
        [15, 16, True],
        [17, 21, False],
        [22, 30, True]
    ])
    def test_alarm(self, pressure_start, pressure_stop, is_alarm_on):
        for pressure in xrange(pressure_start, pressure_stop, 1):
            with patch.object(Sensor, 'pop_next_pressure_psi_value', return_value=pressure) as mock_method:
                alarm = Alarm()
                alarm.check()
                alarm_status = alarm.is_alarm_on
            mock_method.assert_called_once()
            self.assertEqual(alarm_status, is_alarm_on, "Blabla %s" % pressure)
'''
    def test_alarm_check(self):
            alarm = Alarm()
        with patch.object(Sensor, 'pop_next_pressure_psi_value', return_value=pressure) as mock_method:

            alarm.check()
            alarm_status = alarm.is_alarm_on
        mock_method.assert_called_once()
        self.assertEqual(alarm_status, is_alarm_on, "Blabla %s" % pressure)
'''

if __name__ == "__main__":
	#unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(AlarmTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
