"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/
"""

from typing import List


class TrieNode:
    def __init__(self, val=''):
        self._val = val
        self._parent = None
        self._children = set()

    def add_child(self, child: 'TrieNode'):
        self._children.add(child)
        child.set_parent(self)

    def set_parent(self, parent: 'TrieNode'):
        self._parent = parent

    @property
    def val(self):
        if self._parent is None:
            return self._val

        return self._parent.val + self._val

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children


class Solution:
    def letter_case_permutation(self, S: str) -> List[str]:
        # if letter, can map to lower or upper
        # if number, can map to self
        # then, just have to consider all the possible mappings at each step
        # exponential numbner of results, depending on how many letters
        # could construct a trie and traverse it to get the result list
        # could do some other bruter force approach which would have
        #   equivalent runtime

        root = TrieNode()
        current_nodes = [root]
        next_nodes = []
        for c in S:
            # get all the possible next values of c
            if c.isdigit():
                next_vals = [c]
            else:
                next_vals = [c.lower(), c.upper()]

            # for each of our current nodes, append next_vals as children
            for node in current_nodes:
                for val in next_vals:
                    child = TrieNode(val)
                    node.add_child(child)
                    next_nodes.append(child)

            # update current nodes to be the next level
            current_nodes = next_nodes
            next_nodes = []

        # do a traversal to get final result
        result = []
        queue = [root]
        while queue:
            current = queue.pop()
            if len(current.children) == 0:
                # leaf node - yield its full chain
                result.append(current.val)
            else:
                # append all children to queue
                queue.extend(list(current.children))

        return result
