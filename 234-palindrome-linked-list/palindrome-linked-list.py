class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        left = head
        right = prev
        ans = True
        while right:
            if left.val != right.val:
                ans = False
                break
            left = left.next
            right = right.next
        return ans