from vehicle.modules.v3hicle import Vehicle
from vehicle.modules.flags import Maneuver
import unittest

class TestVehicle(unittest.TestCase):

    def test_accessing_variables(self):
        # Initialize vehilce
        vehicle = Vehicle()

        # Set mode to autonomous
        vehicle.set_autonomous_mode()
        self.assertTrue(vehicle.is_autonomous())

        # Set mode to manual
        vehicle.set_manual_mode()
        self.assertFalse(vehicle.is_autonomous())

        # Set maneuver to go forwad
        self.assertTrue(vehicle.set_maneuver(Maneuver.GO_FORWARD))

        # Set invalid maneuver
        self.assertFalse(vehicle.set_maneuver(23))

if (__name__ == '__main__'):
    unittest.main()
