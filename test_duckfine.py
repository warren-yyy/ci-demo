import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):

    def setUp(self):
        self.fine = DuckFine("member-001")

    def test_no_fee_when_not_late(self):
        self.assertEqual(self.fine.charge(0), 0.0)

    def test_grace_period_is_free(self):
        self.assertEqual(self.fine.charge(2), 0.0)

    def test_fee_is_charged_after_grace_period(self):
        self.assertEqual(self.fine.charge(3), 0.50)

    def test_deluxe_fee_is_doubled(self):
        self.assertEqual(self.fine.charge(3, deluxe=True), 1.00)

    def test_fee_does_not_exceed_maximum(self):
        self.assertEqual(self.fine.charge(20), 5.00)

    def test_total_owed_accumulates_fees(self):
        self.fine.charge(3)
        self.fine.charge(4)
        self.assertEqual(self.fine.total_owed, 1.00)

    def test_negative_days_late_raise_value_error(self):
        with self.assertRaises(ValueError):
            self.fine.charge(-1)


if __name__ == "__main__":
    unittest.main()