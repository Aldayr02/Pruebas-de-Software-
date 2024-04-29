import unittest

from .code_to_test import (
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    check_number_status,
    validate_password,
)

# import re


# 1
class TestCheckNumberStatus(unittest.TestCase):

    def test_positive_number(self):
        """Test that the output is 'Positive' for positive numbers."""
        self.assertEqual(check_number_status(1), "Positive")

    def test_negative_number(self):
        """Test that the output is 'Negative' for negative numbers."""
        self.assertEqual(check_number_status(-1), "Negative")

    def test_zero(self):
        """Test that the output is 'Zero' for the number zero."""
        self.assertEqual(check_number_status(0), "Zero")

    def test_large_positive_number(self):
        """Test that the output is 'Positive' for large positive numbers."""
        self.assertEqual(check_number_status(1000000), "Positive")

    def test_large_negative_number(self):
        """Test that the output is 'Negative' for large negative numbers."""
        self.assertEqual(check_number_status(-1000000), "Negative")

    def test_positive_decimal_number(self):
        """Test that the output is 'Positive' for positive decimal numbers."""
        self.assertEqual(check_number_status(0.0001), "Positive")

    def test_negative_decimal_number(self):
        """Test that the output is 'Negative' for negative decimal numbers."""
        self.assertEqual(check_number_status(-0.0001), "Negative")


# 2
class TestValidatePassword(unittest.TestCase):

    def test_valid_password(self):
        """Test that a valid password passes all checks."""
        self.assertTrue(validate_password("Valid$Password1"))

    def test_short_password(self):
        """Test that a password too short is invalid."""
        self.assertFalse(validate_password("Sh0rt!"))

    def test_missing_uppercase(self):
        """Test that a password without an uppercase letter is invalid."""
        self.assertFalse(validate_password("no_uppercase1!"))

    def test_missing_lowercase(self):
        """Test that a password without a lowercase letter is invalid."""
        self.assertFalse(validate_password("NO_LOWERCASE1!"))

    def test_missing_digit(self):
        """Test that a password without a digit is invalid."""
        self.assertFalse(validate_password("NoDigits!!"))

    def test_missing_special_char(self):
        """Test that a password without a special character is invalid."""
        self.assertFalse(validate_password("NoSpecials1"))


# 3
class TestCalculateTotalDiscount(unittest.TestCase):

    def test_no_discount(self):
        """Test that no discount is applied for amounts less than 100."""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_ten_percent_discount(self):
        """Test that a 10% discount is applied for amounts between 100 and 500."""
        self.assertEqual(calculate_total_discount(250), 25)

    def test_twenty_percent_discount(self):
        """Test that a 20% discount is applied for amounts over 500."""
        self.assertEqual(calculate_total_discount(750), 150)

    def test_exact_no_discount_boundary(self):
        """Test that the boundary condition of 100 gives a 10% discount."""
        self.assertEqual(calculate_total_discount(100), 10)

    def test_exact_upper_discount_boundary(self):
        """Test that the boundary condition of 500 gives a 10% discount."""
        self.assertEqual(calculate_total_discount(500), 50)

    def test_above_upper_discount_boundary(self):
        """Test that amounts just above 500 receive a 20% discount."""
        self.assertEqual(calculate_total_discount(501), 100.2)


# 4
class TestCalculateOrderTotal(unittest.TestCase):

    def test_empty_order(self):
        """Test that an empty order totals 0."""
        self.assertEqual(calculate_order_total([]), 0)

    def test_no_discount(self):
        """Test that an order with a quantity of 1 to 5 items does not apply discount."""
        items = [{"quantity": 5, "price": 10}]
        self.assertEqual(calculate_order_total(items), 50)

    def test_five_percent_discount(self):
        """Test that an order with a quantity of 6 to 10 items applies a 5% discount."""
        items = [{"quantity": 7, "price": 10}]
        self.assertEqual(calculate_order_total(items), 66.5)

    def test_ten_percent_discount(self):
        """Test that an order with a quantity above 10 items applies a 10% discount."""
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 135)

    def test_multiple_items(self):
        """Test that an order with multiple items calculates the correct total."""
        items = [
            {"quantity": 2, "price": 10},
            {"quantity": 7, "price": 20},
            {"quantity": 11, "price": 30},
        ]
        # Expected: (2*10) + (7*20*0.95) + (11*30*0.9) = 20 + 133 + 297 = 450
        self.assertEqual(calculate_order_total(items), 450)

    def test_single_item_edge_case(self):
        """Test that an order with a single item is not discounted."""
        items = [{"quantity": 1, "price": 10}]
        self.assertEqual(calculate_order_total(items), 10)

    def test_edge_case_no_discount_to_five_percent(self):
        """Test edge case transition from no discount to 5% discount."""
        items = [{"quantity": 5, "price": 10}]  # Should not get a discount
        self.assertEqual(calculate_order_total(items), 50)
        items = [{"quantity": 6, "price": 10}]  # Should get a 5% discount
        self.assertEqual(calculate_order_total(items), 57)

    def test_edge_case_five_percent_to_ten_percent(self):
        """Test edge case transition from 5% discount to 10% discount."""
        items = [{"quantity": 10, "price": 10}]  # Should get a 5% discount
        self.assertEqual(calculate_order_total(items), 95)
        items = [{"quantity": 11, "price": 10}]  # Should get a 10% discount
        self.assertEqual(calculate_order_total(items), 99)

    def test_invalid_quantity(self):
        """Test that an invalid (negative) quantity results in an appropriate response."""
        items = [{"quantity": -1, "price": 10}]
        with self.assertRaises(ValueError):
            calculate_order_total(items)

    def test_invalid_price(self):
        """Test that an invalid (negative) price results in an appropriate response."""
        items = [{"quantity": 1, "price": -10}]
        with self.assertRaises(ValueError):
            calculate_order_total(items)

    def test_zero_quantity(self):
        """Test that an item with zero quantity does not affect the total price."""
        items = [{"quantity": 0, "price": 10}, {"quantity": 5, "price": 10}]
        self.assertEqual(calculate_order_total(items), 50)

    def test_zero_price(self):
        """Test that an item with zero price does not affect the total price."""
        items = [{"quantity": 5, "price": 0}, {"quantity": 5, "price": 10}]
        self.assertEqual(calculate_order_total(items), 50)


# 5
class TestCalculateItemsShippingCost(unittest.TestCase):

    def test_standard_shipping_under_5(self):
        """Test standard shipping costs for items with total weight <= 5."""
        items = [{"weight": 2}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_up_to_10(self):
        """Test standard shipping costs for items with total weight > 5 and <= 10."""
        items = [{"weight": 3}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_above_10(self):
        """Test standard shipping costs for items with total weight > 10."""
        items = [{"weight": 8}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_under_5(self):
        """Test express shipping costs for items with total weight <= 5."""
        items = [{"weight": 2}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_up_to_10(self):
        """Test express shipping costs for items with total weight > 5 and <= 10."""
        items = [{"weight": 3}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_above_10(self):
        """Test express shipping costs for items with total weight > 10."""
        items = [{"weight": 8}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        """Test that an invalid shipping method raises a ValueError."""
        items = [{"weight": 2}, {"weight": 3}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "pigeon")

    def test_standard_shipping_exact_weight_5(self):
        """Test standard shipping cost for items with total weight exactly 5."""
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_exact_weight_10(self):
        """Test standard shipping cost for items with total weight exactly 10."""
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_express_shipping_exact_weight_5(self):
        """Test express shipping cost for items with total weight exactly 5."""
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_exact_weight_10(self):
        """Test express shipping cost for items with total weight exactly 10."""
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)


if __name__ == "__main__":
    unittest.main()
