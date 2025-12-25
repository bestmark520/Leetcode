# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head   # 慢指針，每次走一步
        fast = head   # 快指針，每次走兩步

        while fast and fast.next: # fast.next有東西的話，fast.next.next才有意義
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   # 相遇表示有 cycle
                return True

        return False