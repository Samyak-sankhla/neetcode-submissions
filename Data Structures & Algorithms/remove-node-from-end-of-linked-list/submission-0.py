# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        size=1
        itr=head
        while(itr.next):
            itr=itr.next
            size+=1
        if size==1 and n==1:
            return None
        #nth element from the back, we can get the index of the element by len-n:
        indx = size - n
        itr=head
        if indx==0:
            head=head.next
            return head
        while(indx>1):
            itr=itr.next
            indx-=1
        if not itr.next.next:
            itr.next=None
            return head
        else:
            nxt=itr.next.next
            itr.next=nxt
            return head

        
        
