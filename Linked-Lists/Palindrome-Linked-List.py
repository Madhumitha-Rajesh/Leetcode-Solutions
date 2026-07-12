# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #  find middle
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse second half
        prev=None
        curr=slow

        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        #compare both halves
        first=head
        second=prev

        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True



        
