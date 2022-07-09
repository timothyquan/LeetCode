# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rec_rev(head) if head else None
    
    def rec_rev(self, node, last=None):
        if node.next:
            head = self.rec_rev(node.next, last=node)
            node.next = last
            return head
        else:
            node.next = last
            return node 