import validate_credit_card
import unittest


class Test_TestValidate_Input(unittest.TestCase):
    def test_validate_negative_integer(self):
        self.assertFalse(
            validate_credit_card.validate_input("-1", True), False)

    def test_validate_zero(self):
        self.assertFalse(validate_credit_card.validate_input("0", True), False)

    def test_validate_hundred(self):
        self.assertFalse(
            validate_credit_card.validate_input("100", True), False)

    def test_validate_integer_one(self):
        self.assertTrue(validate_credit_card.validate_input("1", True), True)

    def test_validate_integer_ninety_nine(self):
        self.assertTrue(validate_credit_card.validate_input("99", True), True)


class HelperClass:

    cc_numbers = ["4123456789123456",
                  "5123-4567-8912-3456",
                  "3123356789123456",
                  "5123 - 3567 - 8912 - 3456",
                  "4123 - 3567 - 8912 -_3456",
                  "44244x4424442444",
                  "612-3567-8912-73456",
                  "5133-3367-8912-3456"]
    cc_iterator = iter(cc_numbers)


class Test_TestCreditCardNumbers(unittest.TestCase):

    def test_must_only_consists_of_digits_zero_to_nine(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertTrue(vcc.must_only_consist_of_digits_zero_to_nine(), True)

    def test_find_position_of_hyphen(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertTrue(vcc.find_position_of_hyphen, True)

    def test_must_start_with_four_five_six(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertTrue(vcc.must_start_with_four_five_six(), False)

    def test_separator_space_other_than_hyphen(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertFalse(vcc.find_position_of_hyphen(), False)

    def test_separator_underscore_other_than_hyphen(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertTrue(vcc.find_position_of_hyphen(), True)

    def test_non_digit_in_the_credit_card_input(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertFalse(vcc.must_only_consist_of_digits_zero_to_nine(), False)

    def test_groups_of_four(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertTrue(vcc.find_position_of_hyphen(), False)

    def test_four_consecutive_repeats(self):
        cc_number = next(HelperClass.cc_iterator)
        vcc = validate_credit_card.ValidateCreditCard(
            len(HelperClass.cc_numbers), cc_number)
        self.assertTrue(vcc.four_consecutive_repeats(), False)


if __name__ == '__main__':
    unittest.main()
