# Definition for singly-linked list.
#   class ListNode:
#       def __init__(self, val=0, next=None):
#           self.val = val
#           self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        curr_node = head
        new_next_node = None
        
        while True:
            old_next_node = curr_node.next

            curr_node.next = new_next_node
            new_next_node = curr_node

            if old_next_node == None:
                return curr_node
            curr_node = old_next_node
            