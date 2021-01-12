"""
LeetCode two sum test script.
"""

from unittest import TestCase

from kevin.leet import add_two_numbers


class TestAddTwoNumbers(TestCase):
    def check_add_two_numbers_numerical(self, v1, v2, expected):
        l1 = self.convert_number_to_linked_list(v1)
        l2 = self.convert_number_to_linked_list(v2)
        sol = add_two_numbers.Solution()
        result = sol.add_two_numbers(l1, l2)
        result_num = self.convert_linked_list_to_number(result)
        assert result_num == expected

    def convert_number_to_linked_list(self, val):
        """
        convert a numerical value to a reverse linked list representation
        """
        digits = [int(x) for x in str(val)][::-1]
        digit_first = digits[0]
        result = add_two_numbers.ListNode(digit_first)
        current = result
        for digit in digits[1:]:
            next = add_two_numbers.ListNode(digit)
            current.next = next
            current = next

        return result

    def convert_linked_list_to_number(self, l: add_two_numbers.ListNode):
        """
        convert a reverse linked list representation to a numerical value
        """
        result = 0
        current = l
        power = 0
        while current:
            result += current.val * (10 ** power)
            current = current.next
            power += 1

        return result

    def test_add_two_numbers_easy(self):
        self.check_add_two_numbers_numerical(342, 465, 807)

    def test_add_two_numbers_zero(self):
        self.check_add_two_numbers_numerical(0, 0, 0)

    def test_add_two_numbers_big(self):
        first = 9999999
        second = 9999
        result = 10009998
        self.check_add_two_numbers_numerical(first, second, result)
