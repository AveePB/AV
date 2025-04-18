from vehicle.modules.v3hicle import Vehicle
import unittest

class TestMotorSystem(unittest.TestCase):

    def test_accessing_variables(self):
        # Initialize vehilce
        vehicle = Vehicle()

        # Set mode to autonomous
        vehicle.set_autonomous_mode()
        self.assertTrue(vehicle.is_autonomous())

        # Set mode to manual
        vehicle.set_manual_mode()
        self.assertFalse(vehicle.is_autonomous())

        # Access detection system
        self.assertIsNotNone(vehicle.detection_system())

        # Access drive system
        self.assertIsNotNone(vehicle.drive_system())

if (__name__ == '__main__'):
    unittest.main()
