import unittest

# Mock of the price management function
def calculate_price(base_price, discount, tax):
    """
    Calculate the final price after applying discount and tax.
    :param base_price: Original price of the item
    :param discount: Discount percentage to be applied
    :param tax: Tax percentage to be added
    :return: Final price
    """
    if base_price < 0 or discount < 0 or tax < 0:
        raise ValueError("Negative values are not allowed")
    discounted_price = base_price - (base_price * discount / 100)
    final_price = discounted_price + (discounted_price * tax / 100)
    return round(final_price, 2)

# Regression Test Suite
class TestPriceManagement(unittest.TestCase):
    
    def test_calculate_price_no_discount(self):
        # Base case: No discount
        self.assertEqual(calculate_price(100, 0, 10), 110.0)
    
    def test_calculate_price_with_discount(self):
        # Check calculation with a discount
        self.assertEqual(calculate_price(100, 10, 10), 99.0)
    
    def test_calculate_price_edge_case_zero_price(self):
        # Edge case: Zero base price
        self.assertEqual(calculate_price(0, 10, 10), 0.0)
    
    def test_calculate_price_large_values(self):
        # Check for large values
        self.assertEqual(calculate_price(100000, 20, 18), 94400.0)

    def test_negative_values(self):
        # Invalid input should raise an exception
        with self.assertRaises(ValueError):
            calculate_price(-100, 10, 10)

# Running the regression tests
if __name__ == '__main__':
    unittest.main()
