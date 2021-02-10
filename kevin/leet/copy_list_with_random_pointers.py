"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/
"""

class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copy_random_list(self, head: Node) -> Node:
        # I am aware this solution is not at all optimal in terms of
        # memory consumption
        # O(1) space is possible by cleverly linking old and new nodes in
        # an alternating fashion
        if head is None:
            return None

        # construct map from nodes to their random nodes
        current = head
        random = dict() # map from old node to old random node
        while current is not None:
            random[current] = current.random
            current = current.next

        # set up new nodes, with map from new to old
        current = head
        new = Node(current.val)
        new_head = new
        back = {new: head} # map back from new to old
        forward = {head: new} # map forward from old to new
        while current.next is not None:
            current = current.next
            new.next = Node(current.val)
            new = new.next
            back[new] = current
            forward[current] = new

        # add correct random pointers in new nodes
        current = new_head
        while current is not None:
            old = back[current]
            old_random = random[old]
            current.random = forward.get(old_random, None)
            current = current.next

        return new_head
