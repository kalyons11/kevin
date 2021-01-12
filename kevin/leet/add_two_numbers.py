"""
https://leetcode.com/problems/add-two-numbers/description/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode, carry: int = 0) \
                        -> ListNode:
        # idea: do this recursively
        # don't forget about our constraints
        # 0 <= Node.val <= 9
        # It is guaranteed that the list represents a number that does not have leading zeros.
        # here we go
        v1 = l1.val
        v2 = l2.val
        s = v1 + v2 + carry
        v = s % 10
        c = (s - v) // 10
        
        n1 = l1.next
        n2 = l2.next
        if n1 and n2:
            return ListNode(v, self.add_two_numbers(n1, n2, c))
        
        if n1:
            return ListNode(v, self.add_two_numbers(n1, ListNode(), c))
        
        if n2:
            return ListNode(v, self.add_two_numbers(ListNode(), n2, c))
        
        # handle end case properly if we still have a digit to carry
        if c > 0:
            return ListNode(v, ListNode(c))
        
        return ListNode(v)
