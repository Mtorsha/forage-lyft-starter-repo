import unittest
from datetime import datetime

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = CarriganTire([0.1,0.01,0.9,0.6])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = CarriganTire([0.1,0.01,0.7,0.6])
        self.assertTrue(tire.needs_service())
