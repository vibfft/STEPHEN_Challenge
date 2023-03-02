import re
import sys
from collections import namedtuple


class ValidateCreditCard:

    re_must_start_with_four_five_six = re.compile(r"^[4-6]+")
    re_must_only_have_zero_nine = re.compile(r"[0-9]+")

    credit_card_nums = []
    all_namedtuples = []
    equal_groups_of_four = [4,9,14] # compare to see whether two lists are equal with == operator

    def __init__(self, total_credit_cards: int, credit_card_num: str) -> None:
        self.total_credit_cards = total_credit_cards
        self.credit_card_num = credit_card_num
        ValidateCreditCard.credit_card_nums.append(self.credit_card_num)

    def must_only_consist_of_digits_zero_to_nine(self):
        digits_only = re.sub(r"\D", "", self.credit_card_num)
        if len(digits_only) == 16:  # credit card number length is required to be 16
            return True
        return False

    def must_start_with_four_five_six(self):
        m = ValidateCreditCard.re_must_start_with_four_five_six.match(
            self.credit_card_num[0])
        if m:
            return True
        return False
    
    def find_position_of_hyphen(self):
        matched_pos_list = []
        for match in re.finditer('-',self.credit_card_num):
            matched_pos_list.append(match.start())
        
        # if there are no matched hyphen or hyphen divides the number string in a group of 4
        if len(matched_pos_list) == 0 or matched_pos_list == ValidateCreditCard.equal_groups_of_four:
            return True
        return False

def validate_input(total_credit_cards: str, debug: bool = False) -> bool:
    total_credit_cards_re = re.compile(r"\d+")
    m = total_credit_cards_re.match(total_credit_cards)

    if m:
        if int(total_credit_cards) > 0 and int(total_credit_cards) < 100:
            if debug:
                print(f"\t{total_credit_cards} is a valid input")
            return True
        else:
            if debug:
                print(f"""\t{total_credit_cards} is an invalid number of credit cards
                \tPlease enter an integer number in the range of 1 < N < 100""")
            return False
    else:
        if debug:
            print(f"""\t{total_credit_cards} is not a valid digit.
            \tPlease enter an integer number in the range of 1 < N < 100""")
        return False


def read_credit_cards(total_credit_cards: str) -> list:
    InputCreditCards = namedtuple('InputCreditCards',
                                  ['line',
                                   'space',
                                   'underscore',
                                   'hyphen',
                                   'all_zero_nine',
                                   'start_with_456'])

    cc_numbers = ["4123456789123456",
                  "5123-4567-8912-3456",
                  "61234-567-8912-3456",
                  "3123356789123456",
                  "5133-3367-8912-3456",
                  "5123 - 3567 - 8912 - 3456",
                  "4123 - 3567 - 8912 -_3456",
                  "6123 - 3567 - 8912 - 73456"]
    cc_iterator = iter(cc_numbers)
    for i in range(int(total_credit_cards)):
        try:
            # user_input = input()
            user_input = next(cc_iterator)
            if not user_input:
                break

            vcc = ValidateCreditCard(total_credit_cards, user_input.strip())
            vcc.all_namedtuples.append(InputCreditCards(
                line=user_input,
                space=(lambda s: " " not in s)(
                    user_input.strip()),  # true if no space
                underscore=(lambda s: "_" not in s)(
                    user_input.strip()),  # true if no underscore
                hyphen=vcc.find_position_of_hyphen(),
                all_zero_nine=vcc.must_only_consist_of_digits_zero_to_nine(),
                start_with_456=vcc.must_start_with_four_five_six()))

        except EOFError:
            break

    for each_tuple in vcc.all_namedtuples:
        print(each_tuple.line, end=",")
        print(each_tuple.space, end=",")
        print(each_tuple.underscore, end=",")
        print(each_tuple.hyphen, end=",")
        print(each_tuple.all_zero_nine, end=",")
        print(each_tuple.start_with_456, end="\n")


def main() -> None:

    total_credit_cards = input(
        "Enter number of credit cards to verify and then input credit card numbers:\n")
    debug = False
    if validate_input(total_credit_cards, debug):
        if debug:
            print(f"\t{total_credit_cards} is a valid number of credit cards")
        pass
    else:
        sys.exit(1)

    read_credit_cards(int(total_credit_cards))


if __name__ == "__main__":
    main()
