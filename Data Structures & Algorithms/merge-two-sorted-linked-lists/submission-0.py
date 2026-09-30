# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        head = None
        curr_node = None

        while True:
            if list1 is None:
                curr_node.next = list2
                break
            elif list2 is None:
                curr_node.next = list1
                break

            if list1.val < list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next

            if head is None:
                curr_node = next_node
                head = curr_node
            else:
                curr_node.next = next_node
                curr_node = next_node

        return head