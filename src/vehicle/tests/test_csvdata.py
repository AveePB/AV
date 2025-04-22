from vehicle.modules.csvdata import CSVManager
from vehicle.modules.flags import Maneuver
import unittest

class TestCSVManager(unittest.TestCase):

    TEST_TIME = 1 # seconds

    def test_create_record(self):
        # Initialize csv manager
        csv = CSVManager('./data/test.csv')
        size = csv.number_of_records()

        # Create new record
        csv.create_record(Maneuver.GO_FORWARD, [i for i in range(360)])
        self.assertIs(size + 1, csv.number_of_records())

if (__name__ == '__main__'):
    unittest.main()
