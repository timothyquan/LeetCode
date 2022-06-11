# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.head = head
        self.pal = True 
        
        def detect_palindrome(current_node = self.head):
            if current_node.next:                
                detect_palindrome(current_node.next)
                
            if not (current_node.val == self.head.val): self.pal = False
            self.head = self.head.next 
            return self.pal
                
                
        
        
        return detect_palindrome(head)