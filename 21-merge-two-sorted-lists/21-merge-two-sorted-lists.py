# Definition for singly-linked list. 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        marker = head = ListNode() 

        while list1 and list2:
            
            if list1.val <= list2.val:
                marker.next = list1
                marker,list1 = list1, list1.next                
            else:
                marker.next = list2
                marker,list2 = list2, list2.next
            
        marker.next = list1 if list1 else list2
        
        return head.next