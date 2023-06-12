import unittest
from datetime import datetime

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = OctoprimeTire([0.9,0.9,0.9,0.6])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = OctoprimeTire([0.1,0.01,0.7,0.6])
        self.assertTrue(tire.needs_service())
