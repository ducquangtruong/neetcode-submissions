# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If we want to preserve original lists, use a wrapper
        heap = []
        for i in range(len(lists)):
            lst = lists[i]
            if lst:
                heapq.heappush(heap, (lst.val, i))
        dummy = ListNode()
        cur = dummy
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = lists[i]
            cur = cur.next
            nxt = lists[i].next
            if nxt:
                lists[i] = nxt
                heapq.heappush(heap, (nxt.val, i))

        return dummy.next