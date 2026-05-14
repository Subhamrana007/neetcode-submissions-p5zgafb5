# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for n in lists:
            curr = n
            while curr:
                arr.append(curr.val)
                curr = curr.next

        dummy = ListNode(0)
        curr = dummy

        for n in sorted(arr):
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next