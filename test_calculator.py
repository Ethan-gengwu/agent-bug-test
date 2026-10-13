import unittest

from calculator import calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_issue_1_price_times_quantity(self):
        self.assertEqual(calculate_total(20, 3), 60)

    def test_zero_quantity(self):
        self.assertEqual(calculate_total(20, 0), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_total(0, 3), 0)

    def test_single_item(self):
        self.assertEqual(calculate_total(20, 1), 20)

    def test_fractional_price(self):
        self.assertAlmostEqual(calculate_total(19.99, 3), 59.97)


if __name__ == "__main__":
    unittest.main()
