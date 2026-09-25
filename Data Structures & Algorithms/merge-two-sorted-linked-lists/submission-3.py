# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy ndoe.
        # This gives us a starting point for out merged list.
        dummy = ListNode()

        # curr will point to the last node in our merged list.
        curr = dummy

        while list1 and list2:
            
            if list1.val <= list2.val:
                curr.next = list1

                list1 = list1.next
            
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2
            
        
        return dummy.next