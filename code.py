class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(-1)
        curr = head
        while curr:
            curr_next = curr.next
            prv, nxt = dummy, dummy.next
            while nxt:
                if nxt.val > curr.val: break
                prv = nxt
                nxt = nxt.next
                
            curr.next = nxt
            prv.next = curr
            curr = curr_next
        
        return dummy.next

    '''
    time complexity is O(n^2), as Insertion sort should be: we take O(n) loops with O(n) loop inside. Space complexity is O(1), because what we do is only change connections between our nodes, and do not create new data.
    '''

        
