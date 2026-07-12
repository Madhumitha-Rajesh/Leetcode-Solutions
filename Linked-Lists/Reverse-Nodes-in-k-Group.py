# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #check if there are at least k nodes

        temp=head
        count=0

        while temp and count<k:
            temp=temp.next
            count+=1
        
        if count<k:
            return head

        #reverse k nodes
        prev=None
        curr=head
        count=0
        
        while curr and count<k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count+=1
        
        #connect to the reversed remaining list
        if curr:
            head.next=self.reverseKGroup(curr,k)
        return prev
        
