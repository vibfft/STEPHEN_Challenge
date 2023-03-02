import validate_credit_card
import unittest

class Test_TestValidate_Input(unittest.TestCase):
    def test_validate_negative_integer(self):
        self.assertFalse(validate_credit_card.validate_input("-1", True), False)

    def test_validate_zero(self):
        self.assertFalse(validate_credit_card.validate_input("0", True), False)

    def test_validate_hundred(self):
        self.assertFalse(validate_credit_card.validate_input("100", True), False)

    def test_validate_integer_one(self):
        self.assertTrue(validate_credit_card.validate_input("1", True), True)

    def test_validate_integer_ninety_nine(self):
        self.assertTrue(validate_credit_card.validate_input("99", True), True)

if __name__ == '__main__':
    unittest.main()