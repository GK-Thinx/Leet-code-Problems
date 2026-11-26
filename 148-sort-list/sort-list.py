class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        dummy = ListNode(0, head)
        size = 1
        while size < length:
            prev = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = self._split(left, size)
                curr = self._split(right, size)
                merged_head, merged_tail = self._merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1
        return dummy.next
    def _split(self, head, size):
        if not head:
            return None
        for i in range(size - 1):
            if head.next:
                head = head.next
            else:
                break
        nxt = head.next
        head.next = None
        return nxt
    def _merge(self, l1, l2):
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