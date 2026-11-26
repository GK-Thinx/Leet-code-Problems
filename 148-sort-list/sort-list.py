class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        def split(start, size):
            cur = start
            for _ in range(size - 1):
                if cur:
                    cur = cur.next
                else:
                    break
            if not cur:
                return None
            nxt = cur.next
            cur.next = None
            return nxt
        def merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            while tail.next:
                tail = tail.next
            return dummy.next, tail
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step < n:
            prev = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = split(left, step)
                cur = split(right, step)
                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            step <<= 1
        return dummy.next