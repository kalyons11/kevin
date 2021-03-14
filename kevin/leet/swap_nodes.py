"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/
"""

from kevin.utils.link import ListNode


class SolutionFailure:
    def swap_nodes(self, head: ListNode, k: int) -> ListNode:
        # have to go through and compute length to be able to know
        # what is k from the end
        # store pointers to these nodes
        # then, perform the proper swaps of .next pointers
        # need to know the nodes BEFORE and AFTER these as well
        # O(1) space, O(n) runtime

        i = 1  # current index in list
        length = 0  # current computed length of list
        current = head  # current node in list
        prev = None  # previous node in list
        first_pre = None  # node before the kth node from start
        first = None  # node at kth from start
        first_post = None  # node after the kth node from start

        while True:  # first pass - compute length of list
            length += 1
            if i == k:
                first_pre = prev
                first = current
                first_post = current.next

            if current.next is None:
                break

            prev = current
            current = current.next
            i += 1

        # now, we have length - so can check again for the ending node
        i = 1  # reset index
        current = head  # reset current
        prev = None  # reset prev
        last_pre = None  # node before the kth node from end
        last = None  # node at kth from end
        last_post = None  # node after the kth node from end
        while True:
            if i == length - k + 1:
                last_pre = prev
                last = current
                last_post = current.next
                break  # no need to keep going

            prev = current
            current = current.next
            i += 1

        # perform the necessary swaps
        head_new = head

        if first_pre is None:
            # the head is being swapped
            head_new = last
        else:
            first_pre.next = last

        if last != first_post:  # handle weird cycle case with 2 nodes only
            last.next = first_post
        else:
            last.next = first

        if last_pre is not None:
            last_pre.next = first

        first.next = last_post

        return head_new

        # logic breaks down in the case where last is before first
        # we should just use an array formulation


class Solution:
    def swap_nodes(self, head: ListNode, k: int) -> ListNode:
        # convert to an array
        # then, do the swaps
        # then, update the pointers as you need to do
        arr = []
        current = head
        while current:
            arr.append(current)
            current = current.next

        length = len(arr)

        a = arr[k - 1]
        b = arr[length - k]
        arr[k - 1] = b
        arr[length - k] = a

        head_new = arr[0]
        for i in range(length - 1):
            current = arr[i]
            current.next = arr[i + 1]

        last = arr[-1]
        last.next = None

        return head_new


# inspired by:
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/discuss/1108911/Python-No-need-in-Two-Pointers-Explained
# very nice - just swap the values, don't worry about pointers
class SolutionOptimized:
    def swap_nodes(self, head: ListNode, k: int) -> ListNode:
        n = 0
        beg = head
        while beg:
            if n == k-1: l = beg
            beg = beg.next
            n += 1

        r = head
        for m in range(n-k):
            r = r.next

        l.val, r.val = r.val, l.val
        return head
