from typing import Any, List


class ListNode:
    def __init__(self, val: Any = 0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head


    @staticmethod
    def init_from_list(vals: List[Any]) -> 'LinkedList':
        assert len(vals) > 0, 'cannot init from empty list'
        head = ListNode(vals[0])
        current = head
        for i in range(1, len(vals)):
            current.next = ListNode(vals[i])
            current = current.next

        return LinkedList(head)


    def to_list(self) -> List[Any]:
        res = []
        current = self.head
        while current:
            res.append(current.val)
            current = current.next

        return res
