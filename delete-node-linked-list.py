class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # change the value of current value to next node, then delete next node
    def deleteNode(self, node):
        if not node:
            return None
        
        node.val = node.next.val
        node.next = node.next.next

