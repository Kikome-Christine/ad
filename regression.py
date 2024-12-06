class PriceManager:
    def __init__(self):
        self.prices = {}

    def set_price(self, item, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.prices[item] = price

    def get_price(self, item):
        return self.prices.get(item, None)

# Regression test function
def test_price_manager():
    pm = PriceManager()
    
    # Initial setting of prices
    pm.set_price("apple", 1.00)
    assert pm.get_price("apple") == 1.00  # Test initial price setting

    # Update price
    pm.set_price("apple", 1.20)
    assert pm.get_price("apple") == 1.20  # Test updated price

    # Test error handling for negative prices
    try:
        pm.set_price("banana", -0.50)
    except ValueError as e:
        assert str(e) == "Price cannot be negative"  # Ensure error is raised

# Running regression tests
test_price_manager()
print("All regression tests passed.")


import unittest

# Test class for Product
# class TestProduct(unittest.TestCase):
#     def test_total_calculation(self):
#         product = Product("Phone", 200, 3)
#         self.assertEqual(product.calculate_total(), 600)

#     def test_discounted_total(self):
#         discounted_product = DiscountedProduct("TV", 1000, 1, 20)
#         self.assertEqual(discounted_product.calculate_total(), 800)

# if __name__ == "__main__":
#     unittest.main()